# TODO

### Dokumentaatio

### Navi
* Raporttien piilottaminen, jos yrityksellä ei ole raporttia

### Näkymien järjestäminen

Oletusjärjestys eri SQLitella ja Postgresillä

### Sivutus ????
[Flask SQL Alchemy pagination](http://flask-sqlalchemy.pocoo.org/2.1/api/?highlight=pagination#flask.ext.sqlalchemy.Pagination)
[Jinja2 pagination macro](https://gist.github.com/allhailwesttexas/8c7fe8f8b53190c2ad8a)
* Käyttäjät
* Analyysit

### Liian ison syötteen tarkistus lomakkeilla

* <del>Kirjautuminen</del>
* <del>Rekisteröityminen</del>
* <del>Profiili</del>
* <del>Salasana</del>
* <del>Käyttäjä</del>
* <del>Analyysi</del>

### Kantavirheiden try-catch ja käsittely (lokitus, ilmoitus käyttäjälle)

* Kirjautuminen
* Rekisteröityminen
* Profiili
* Salasana
* Käyttäjä
* Analyysi

### Kirjautuminen
* <del>Puuttuvista tiedoista ei tule ilmoitusta - tsekkaa onko lomaketta ja validointia</del>

### Rekisteröityminen

* <del>Pitäisikö ohjata etusivulle rekisteritymisen jälkeen ja antaa Kiitos rekisteröitymisestä -ilmoitus</del>

### Käyttäjät

* <del>Käyttäjän poistamisesta tulee virhe, jos on rivejä UserRoles -taulussa</del> 
* Mikä merkitys on Ylläpitäjä -roolilla
* <del>Roolien nimet</del>
* Roolit on kovakoodattu käyttäjälomakkeelle - voisi varmaan hakea kannasta (choises)

### Analyysi

* Tee raportti / katso raporttia painikkeiden nimet
* Varoitus raportin tekemiseen, jos jo tehty
* Kohteiden tarkistus, että ovat valideja urleja ja että yksittäisen urlin pituus on korkeintaan 256 merkkiä

### Kohde, Ttarget

* <del>Foreign key ttargetid => ttarget.id - luominen ei onnistu initissä</del>

### Uusin raportti -lohko

* Tsekkaa keyword count - ei ole oikein 

### Raportti

* Mieti ja tsekkaa koko juttu - mitä loppukäyttäjä tässä voisi haluta nähdä - käyttäjätarinat????
* Graafit

### Roolit - toimivatko oikein / fiksusti???

* Ylläpitäjärooli?

###  Arvosanalle 5 on lisäksi seuraavat minimivaatimukset.

* OK Toimiva tietokantaa käyttävä web-sovellus.
* OK Vähintään kolme tietokohdetta, eli vähintään 3 tietokantataulua sekä mahdolliset liitostaulut.
* OK Kirjautumisen lisäksi käyttäjä on yhdistetty tietokannassa johonkin tietokohteeseen, eli käyttäjien tietoja ei tule käyttää pelkästään kirjautumisen osana.
* OK Vähintään kahdesta tietokohteesta täysi CRUD (käyttäjät, analyysit).
* OK Yksi tai useampi monesta moneen -suhde (kayttäjä - käyttäjärooli - rooli)
* TOINEN PUUTTUU Vähintään kaksi monimutkaisempaa useampaa tietokantataulua käyttävää yhteenvetokyselyä. Yhteenvetokyselyt ovat perustellusti (järkevä) osa sovelluksen käyttötapauksia ja toimintaa.
* PUUTTUU Käyttötapaukset perusteltuja sekä hyvin dokumentoituja, 
* PUUTTUU Käyttötapausten yhteydessä myös niihin liittyvät SQL-kyselyt.
