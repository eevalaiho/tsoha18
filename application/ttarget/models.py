from application import db
from application.models import Base

class Ttarget(Base):
    __tablename__ = "ttarget"

    analysisid = db.Column(db.Integer, db.ForeignKey('analysis.id'), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    # The following data is to be filled through crawling and analyzing the data
    title = db.Column(db.String(255))
    keywordmentioncount = db.Column(db.Integer)
    keywordmentions = db.Column(db.String(8000)) # json data

    def __init__(self, analysisid, url):
        self.analysisid = analysisid
        self.url = url

