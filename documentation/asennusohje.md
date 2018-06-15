# Asennusohje

### Esivaatimukset

Sovelluksen esivaatimukset on kuvattu kurssin työvälineet -sivulla [Työvälineet ja niiden asentaminen](https://materiaalit.github.io/tsoha-18/tyovalineet/).

### Ohjelman lataus

Lataa ohjelmakoodi itsellesi GitHubista, osoitteesta: https://github.com/eevalaiho/tsoha18 haluamaasi asennuskansioon. Jos lataat koodin zipattuna, pura zip latauksen jälkeen.

### Virtuaaliympäristön pystytys

Avaa komentokehoite ja mene sovelluksen asennuskansioon. Luo sovellukselle virtuaaliympäristö komennolla:
```
$ python3 -m venv venv
```
Ota virtuaaliympäristö käyttöön komennolla:
```
$ source venv/bin/activate
```
Asenna sovelluksen vaatimat ohjelmistokirjastot komennolla:
```
$ pip install -r requirements.txt
```
Käynnistä python komentotulkki komennolla:
```
$ python3
```
Lataa NLTK:n käyttämät resurssit komennolla (lisätietoa [Installin NLTK](https://www.nltk.org/install.html)):
```
>>> import nltk
>>> nltk.download()
```

### Ohjelman käynnistys

Käynnistä web-sovellus komennolla:
```
$ python3 run.py
```
Komennon ajaminen luo sovelluksen application-kansioon SQLite-tietokannan ja käynnistää web-sovelluksen osoitteeseen [http://127.0.0.1:5000](http://127.0.0.1:5000).