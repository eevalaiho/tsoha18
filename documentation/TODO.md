# TODO

### Dokumentaatio

### Navi
* <del>Raporttien piilottaminen, jos yrityksellä ei ole raporttia</del>

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

* <del>Pitäisikö ohjata etusivulle rekisteröitymisen jälkeen ja antaa Kiitos rekisteröitymisestä -ilmoitus</del>

### Käyttäjät

* <del>Käyttäjän poistamisesta tulee virhe, jos on rivejä UserRoles -taulussa</del> 
* Mikä merkitys on Ylläpitäjä -roolilla
* <del>Roolien nimet</del>
* <del>Roolit on kovakoodattu käyttäjälomakkeelle - voisi varmaan hakea kannasta (choises)</del>
* <del>Rekisteröitymisen jälkeen ei pitäisi päästä suoraan kirjautumaan</del>

### Analyysi

* <del>Tee raportti / katso raporttia painikkeiden nimet</del>
* <del>Raportin voi ajaa uudestaan, kun käy poistamassa raportilta lukittu -täpän OK</del>
* <del>Varmistus raportin tekemiseen, jos jo tehty</del>
* Tallennukseen kohteiden tarkistus, että ovat valideja urleja ja että yksittäisen urlin pituus on korkeintaan 256 merkkiä

### Kohde, Ttarget

* <del>Foreign key ttargetid => ttarget.id - luominen ei onnistu initissä</del>

### Uusin raportti -lohko

* <del>Tsekkaa keyword count - ei ole oikein</del> 

### Raportti

* <del>Mitä loppukäyttäjä tässä voisi haluta nähdä - käyttäjätarinat</del>
* Graafit - jos on aikaa
* Etusivun uusin raportti -> uusimmat raportit ja sql:n rajaus top 3

### Roolit - toimivatko oikein / fiksusti???


### Vasen valikko
* Alikohteet auki
* Raportit myös ylläpitäjälle???


###  Arvosanalle 5 on lisäksi seuraavat minimivaatimukset.

* OK Toimiva tietokantaa käyttävä web-sovellus.
* OK Vähintään kolme tietokohdetta, eli vähintään 3 tietokantataulua sekä mahdolliset liitostaulut.
* OK Kirjautumisen lisäksi käyttäjä on yhdistetty tietokannassa johonkin tietokohteeseen, eli käyttäjien tietoja ei tule käyttää pelkästään kirjautumisen osana.
* OK Vähintään kahdesta tietokohteesta täysi CRUD (käyttäjät, analyysit).
* OK Yksi tai useampi monesta moneen -suhde (kayttäjä - käyttäjärooli - rooli)
* OK Vähintään kaksi monimutkaisempaa useampaa tietokantataulua käyttävää yhteenvetokyselyä. Yhteenvetokyselyt ovat perustellusti (järkevä) osa sovelluksen käyttötapauksia ja toimintaa.

* PUUTTUU Käyttötapaukset perusteltuja sekä hyvin dokumentoituja, 
* PUUTTUU Käyttötapausten yhteydessä myös niihin liittyvät SQL-kyselyt.
* PUUTTUU Asennusohje


* Kuvia käyttöohjeeseen

### Poista

<del>JSON beautifier jquery kirjasto</del>

### Misc

* Miksi get_report_data:aa kutsutaan käyttäjän raportin katselussa - lienee vanhaa jäännettä
* Kohteet avainsanoittain ORDER BY kw_count DESC
* Indeksi käyttöohjeeseen