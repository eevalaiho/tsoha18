from flask import Flask, render_template
#from boilerpipe.extract import Extractor
import requests
import justext

app = Flask(__name__)

class Item:
    def __init__(self, name):
        self.name = name


nimi = "Essi Esimerkki"

lista = [1, 1, 2, 3, 5, 8, 11]

esineet = []
esineet.append(Item("Eka"))
esineet.append(Item("Toka"))
esineet.append(Item("Kolmas"))
esineet.append(Item("Neljäs"))



@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/demo")
def content():
    return render_template("demo.html", nimi=nimi, lista=lista, esineet=esineet)


@app.route("/article")
def article():
    # extractor = Extractor(extractor='ArticleExtractor', url='https://yle.fi/uutiset/3-10213120')
    response = requests.get("https://fi.wikipedia.org/wiki/Kurt_G%C3%B6del")
    paragraphs = justext.justext(response.content, justext.get_stoplist("Finnish"))
    return render_template("article.html", paragraphs=paragraphs)


if __name__ == "__main__":
    app.run(debug=True)