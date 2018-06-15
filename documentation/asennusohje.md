# Asennusohje

### Esivaatimukset

Sovelluksen esivaatimukset on kuvattu kurssin sivulla [Työvälineet ja niiden asentaminen](https://materiaalit.github.io/tsoha-18/tyovalineet/).

### Ohjelman lataus

Lataa ohjelmakoodi itsellesi GitHubista, osoitteesta: 
[https://github.com/eevalaiho/tsoha18](https://github.com/eevalaiho/tsoha18) 
haluamaasi asennuskansioon. Jos lataat koodin zipattuna, pura zip latauksen jälkeen.

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
Lataa NLTK:n käyttämät resurssit komennolla (ks [Installing NLTK](https://www.nltk.org/install.html)):
```
>>> import nltk
>>> nltk.download()
```

### Ohjelman käynnistys

Sovelluksen käynnistäminen luo sovelluksen application-kansioon SQLite-tietokannan. 
Web-sovellus käynnistyy osoitteeseen [http://127.0.0.1:5000](http://127.0.0.1:5000).
Käynnistä sovellus komennolla:
```
$ python3 run.py
```