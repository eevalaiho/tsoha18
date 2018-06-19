# Asennusohje

### Asennus tuotantoympäristöön

Tässä ohjeessa on kuvattu sovelluksen tuotantoasennus Heroku-pilviympäristöön.

##### Esivaatimukset

* Tili [Herokussa](https://devcenter.heroku.com/)
* Heroku CLI [asennettuna](https://devcenter.heroku.com/articles/heroku-cli).
* Git client [asennettuna](https://gist.github.com/derhuerst/1b15ff4652a867391f03).

##### Asennus

Avaa komentokehoite ja siirry hakemistoon, mihin haluat ladata sovelluksen tiedostot. 
Lataa sovelluksen koodit työasemalle komennolla:
```
$ git clone https://github.com/eevalaiho/tsoha18
```
Siirry nyt sovelluksen hakemistoon:
```
$ cd tsoha18
```
Kirjaudu Herokuun komennolla:
```
$ heroku login
```
Luo Heroku-sovellus komennolla:
```
$ heroku apps:create JOKUNIMI --region eu
```
Liitä sovellukseen PostgreSQL-lisäosa komennolla:
```
$ heroku addons:add heroku-postgresql:hobby-dev
```
Vie sovellus Herokuun komennolla:
```
$ git push heroku master
```
Kun komento on valmistunut, sovellus on käytössä Herokussa osoitteessa http://JOKUNIMI.herokuapp.com.

### Kehitysympäristön pystytys

##### Esivaatimukset

Sovelluksen esivaatimukset on kuvattu kurssin sivulla [Työvälineet ja niiden asentaminen](https://materiaalit.github.io/tsoha-18/tyovalineet/).

##### Ohjelman lataus

Lataa ohjelmakoodi itsellesi GitHubista, osoitteesta: 
[https://github.com/eevalaiho/tsoha18](https://github.com/eevalaiho/tsoha18) 
haluamaasi asennuskansioon. Jos lataat koodin zipattuna, pura zip latauksen jälkeen.

##### Virtuaaliympäristön pystytys

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

##### Ohjelman käynnistys

Sovelluksen käynnistäminen luo sovelluksen application-kansioon SQLite-tietokannan. 
Web-sovellus käynnistyy osoitteeseen [http://127.0.0.1:5000](http://127.0.0.1:5000).
Käynnistä sovellus komennolla:
```
$ python3 run.py
```