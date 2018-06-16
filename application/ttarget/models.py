import urllib, re, nltk, datetime, jsonpickle, sys

from flask import flash
from sqlalchemy import text

from application import db
from application.library import is_valid_url
from application.models import Base

from langdetect import detect_langs
from bs4 import BeautifulSoup
from stop_words import get_stop_words
from collections import Counter


class Ttarget(Base):
    __tablename__ = "ttarget"

    analysisid = db.Column(db.Integer, db.ForeignKey('analysis.id'), nullable=False)
    url = db.Column(db.String(255), nullable=False)

    # The following data is to be filled through NLTK and other analyses
    ttargetid = db.Column(db.Integer)#, db.ForeignKey('ttarget.id'))
    title = db.Column(db.String(255))
    lang = db.Column(db.String(2))
    word_count = db.Column(db.Integer)
    key_word_count = db.Column(db.Integer)
    nltk_analysis_json = db.Column(db.Text) # json data

    def __init__(self, analysisid, url):
        self.analysisid = analysisid
        self.url = url

    def ttargets(self):
        return Ttarget.query.filter(Ttarget.ttargetid.__eq__(self.id)).all()

    def nltk_analysis(self):
        if not self.nltk_analysis_json is None:
            return jsonpickle.decode(self.nltk_analysis_json)
        return None

    def processWebContent(self, keywords):

        # Check that url is valid - I guess this check should be moved to saving targets
        if (not is_valid_url(self.url)):
            flash('Virheellinen osoite ' + self.url, 'analysis')
            return False

        # Get the content
        try:
            res = urllib.request.urlopen(self.url)
        except (Exception) as ex:
            flash('Ei voitu lukea osoitetta ' + self.url, 'analysis')
            return False

        # Parse HTML
        try:
            soup = BeautifulSoup(res, "html.parser")
            for tag in ['script', 'link', 'style', 'input']:
                [x.extract() for x in soup.findAll(tag)]
            self.raw = soup.getText()

            # Get NLTK analysis
            obj_nltk_analysis = NltkAnalysis(self.raw, keywords)
            self.title = obj_nltk_analysis.title
            self.lang = obj_nltk_analysis.lang
            self.word_count = sum(obj_nltk_analysis.no_stop_words.values())
            self.key_word_count = sum(obj_nltk_analysis.key_words.values())

            # Serialize to json
            self.nltk_analysis_json = jsonpickle.encode(obj_nltk_analysis)

        except (Exception) as ex:
            flash('Virhe NLTK analyysissä ' + self.url + ", " + ex, 'analysis')
            sys.stdout.write(ex)
            return False

        return True


class NltkAnalysis(object):

    def __init__(self, raw, keywords):
        self.date_created = datetime.datetime.now()

        # Tokenize
        nltk.data.path.append('./nltk_data/')
        tokens = nltk.word_tokenize(raw)
        text = nltk.Text(tokens)
        self.title = text.name

        # Remove punctuation
        non_punct = re.compile('.*[A-Za-z].*')

        # Detect language
        self.lang = detect_langs(raw)[0].lang

        # Stop words
        stops = get_stop_words(self.lang)
        raw_words_match = [w for w in text if non_punct.match(w)]

        no_stop_words_match = [w for w in raw_words_match if w.lower() not in stops and len(w) > 3]
        self.no_stop_words = Counter(no_stop_words_match)

        key_words_match = [w for w in no_stop_words_match if w.lower() in keywords]
        self.key_words = Counter(key_words_match)


