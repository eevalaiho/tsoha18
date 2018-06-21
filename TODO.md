# Tee vielä

### TODO

* <del>Salasanojen kryptaus</del>
* Tsekkaa asennusohje
* <del>Analyysin tallennukseen kohteiden tarkistus, että ovat valideja urleja ja että yksittäisen urlin pituus on korkeintaan 256 merkkiä</del>
* Käyttäjälle tulee virhe ei-ajetun raportin sivulla, kun yritykselle ei ole ajettu yhtän raporttia:
```
    sqlalchemy.exc.DataError: (psycopg2.DataError) cannot deconstruct a scalar
    
    2018-06-21T02:45:53.605094+00:00 app[web.1]:  [SQL: "select distinct key from ( select data.value as keywords from ttarget, json_each(ttarget.nltk_analysis) as data where key = 'key_words' and ttarget.analysis_id= %(id)s ) as subq, json_each(subq.keywords) order by key"] [parameters: {'id': 1}] (Background on this error at: http://sqlalche.me/e/9h9h)
```
### Kehityskohteet / rajoitukset

* Graafit raportille - jos on aikaa
* Kuvia käyttöohjeeseen
* Etusivun uusin raportti -> uusimmat raportit ja sql:n rajaus top 3
* Sivutus ????
    * [Flask SQL Alchemy pagination](http://flask-sqlalchemy.pocoo.org/2.1/api/?highlight=pagination#flask.ext.sqlalchemy.Pagination)
    * [Jinja2 pagination macro](https://gist.github.com/allhailwesttexas/8c7fe8f8b53190c2ad8a)

    
# Tehdyt / ei tehdä

### <del>Dokumentaatio</del>
* <del>Kuvia käyttöohjeeseen</del>

### Navi
* <del>Raporttien piilottaminen, jos yrityksellä ei ole raporttia</del>

### Listausnäkymien järjestäminen

<del>Oletusjärjestys eri SQLitella ja Postgresillä</del>

### Liian ison syötteen tarkistus lomakkeilla

* <del>Kirjautuminen</del>
* <del>Rekisteröityminen</del>
* <del>Profiili</del>
* <del>Salasana</del>
* <del>Käyttäjä</del>
* <del>Analyysi</del>

### Kirjautuminen
* <del>Puuttuvista tiedoista ei tule ilmoitusta - tsekkaa onko lomaketta ja validointia</del>

### Rekisteröityminen

* <del>Pitäisikö ohjata etusivulle rekisteröitymisen jälkeen ja antaa Kiitos rekisteröitymisestä -ilmoitus</del>

### Käyttäjät

* <del>Käyttäjän poistamisesta tulee virhe, jos on rivejä UserRoles -taulussa</del> 
* <del>Mikä merkitys on Ylläpitäjä -roolilla?</del>
* <del>Roolien nimet</del>
* <del>Roolit on kovakoodattu käyttäjälomakkeelle - voisi varmaan hakea kannasta (choises)</del>
* <del>Rekisteröitymisen jälkeen ei pitäisi päästä suoraan kirjautumaan</del>

### Analyysi

* <del>Tee raportti / katso raporttia painikkeiden nimet</del>
* <del>Raportin voi ajaa uudestaan, kun käy poistamassa raportilta lukittu -täpän OK</del>
* <del>Varmistus raportin tekemiseen, jos jo tehty</del>

### Kohde, Ttarget

* <del>Foreign key ttargetid => ttarget.id - luominen ei onnistu initissä</del>

### Uusin raportti -lohko

* <del>Tsekkaa keyword count - ei ole oikein</del> 

### Raportti

* <del>Mitä loppukäyttäjä tässä voisi haluta nähdä - käyttäjätarinat</del>

### Roolit - toimivatko oikein / fiksusti???


### Vasen valikko
* <del>Alikohteet auki</del>
* <del>Raportit myös ylläpitäjälle???</del>


###  Arvosanalle 5 on lisäksi seuraavat minimivaatimukset.

* <del>OK Toimiva tietokantaa käyttävä web-sovellus.
* OK Vähintään kolme tietokohdetta, eli vähintään 3 tietokantataulua sekä mahdolliset liitostaulut.
* OK Kirjautumisen lisäksi käyttäjä on yhdistetty tietokannassa johonkin tietokohteeseen, eli käyttäjien tietoja ei tule käyttää pelkästään kirjautumisen osana.
* OK Vähintään kahdesta tietokohteesta täysi CRUD (käyttäjät, analyysit).
* OK Yksi tai useampi monesta moneen -suhde (kayttäjä - käyttäjärooli - rooli)
* OK Vähintään kaksi monimutkaisempaa useampaa tietokantataulua käyttävää yhteenvetokyselyä. Yhteenvetokyselyt ovat perustellusti (järkevä) osa sovelluksen käyttötapauksia ja toimintaa.

* OK Käyttötapaukset perusteltuja sekä hyvin dokumentoituja, 
* OK Käyttötapausten yhteydessä myös niihin liittyvät SQL-kyselyt.
* OK Asennusohje</del>

### Poista turhat viittaukset

* <del>jsonpickle</del>
* <del>JSON beautifier jquery kirjasto</del>

### Misc

* <del>Miksi get_report_data:aa kutsutaan käyttäjän raportin katselussa - onko vanhaa jäännettä</del>
* <del>Kohteet avainsanoittain ORDER BY kw_count DESC</del>
* <del>Indeksi käyttöohjeeseen?</del>
* <del>Tietokanta-dokumentti - yhteenvetokyselyt - pitäisikö olla käyttötapauksissa vai tässä??????</del>
* <del>Raportin teon prosessi - toimiiko fiksusti?</del>


### Virhekäsittely
* <del>Tsekkaa että on toteutuettu kantavirheiden try-catch ja käsittely (lokitus / ilmoitus käyttäjälle)
* Kirjautuminen
* Rekisteröityminen
* Profiili
* Salasana
* Käyttäjä
* Analyysi</del>