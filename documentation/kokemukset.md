# Kokemukset

Harjoitustyön työvälineet eivät olleet Git:iä ja GitHub:ia lukuunottamatta ennalta tuttuja, joten projektissa
oli kivasti uuden oppimista. 

### Python

Python-kieleen tutustuminen on ollut "listallani" ja tässä opiskelu hoitui mukavassa kontekstissa. 

Huomioita: 
* kiva, tuottelias, helppo omaksua (ainakin enemmän koodanneelle)
* paljon ohjelmistokirjastoja saatavilla, 
* aktiivinen ja laajasti käytössä oleva kieli => paljon artikkeleita, vinkkkejä, ongelmien ratkaisuja netissä => helppo ja nopea kehittää
* googlaamalla on löytynyt (kohtuullisen) helposti vinkkejä eri ongelmatilanteisiin
* visuaalisen hahmottamisen kannalta vähän ärsyttävä syntaksi, koska koodilohkolle ei lopetusmerkkiä 
* dynaaminen tyypitys hankaloitti välillä devausta, kun IDE:n intellisense-tyyppinen tuki 
saattoi puuttua (minulla oli käytössä PyCharm)

### SQLAlchemy
* Kätevä SQLite-integraatio
* Helpottaa ja nopeuttaa tietokantapohjaisen sovelluksen kehitystä mainiolla tavalla

### Flask
* Vaikuttaa tuotteliaalta frameworkiltä, tosin ei kokemusta muista fx:istä pythonin päälle

### WTForms
* Helpottaa kyllä mahtavasti lomakekäsittelyä
* Laajennettavissa, tätä varmaan tarvitsee, jos/kun enemmän tekee

### Jinja2
* Ihan ok UI framework (tai mikä?)
* Vähän kökköä kun ei voi käyttää python-syntaksia kaikkialla vaan metodit pitää putkittaa

### BeautifilSOAP
* Parseroi kätevän oloisesti html:ää, tosin käyttökokemus aika suppea ja käyttötapaukset ilmeisen simppeleitä

### NLTK
* Mielenkiintoinen, paljon esimerkkejä netissä
* En ehtinyt ihan niin paljon tutustua, kuin olisin alunperin ajatus

### SQLite
* Kiva ja nopea ad hoc –väline
* Tuntuu että ei tarkista mitään tiedon eheyksiä, mikä aiheutti vähän ylimääräistä vaivaa tuotantoonasennuksissa
* Palauttaa raaka-sql-kyselyissä päivämäärän merkkijonona -> päänvaivaa
* JSON-tuki asentui Ubuntulle automaattisesti, kiva

### Postgre
* Kiva tutustua tähänkin tuotteeseen
* JSON-tuki on, mutta en ehtinyt kovin hyvin tutustua.
* Osa JSON-funktioista erejä, kuin SQLitessa => devissä pitäisi ottaa käyttöön PostgreSQL

### Heroku
* Ihan ok, välillä hidas

###SchemaCrawler
* Käytin SchemaCrawler –kirjastoa tietokantakaavion tekemiseen – kätevää (kun ei tarvinnut viedä kantaa esim SQL Serveriin ja generoida kuvaa sieltä)
