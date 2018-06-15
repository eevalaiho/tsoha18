# Käyttöohje


### Yleistä 

Sovellus on asennettu Herokussa osoitteeseen: [https://shielded-brook-33904.herokuapp.com/](https://shielded-brook-33904.herokuapp.com/)

Käyttäjätunnukset: 
* Sähköposti: paivio@tsoha18, salasana: salainen (pääylläpitäjä)
* Sähköposti: aukusti@asianajotoimisto, salasana: salainen (asiakas)
* Sähköposti: ida@ideahautomo, salasana: salainen (asiakas)


### Tunnistamattoman käyttäjän toiminnot

#### Kirjautuminen

Palveluun kirjaututaan [aloitussivun](https://shielded-brook-33904.herokuapp.com) kirjautumislomakkeelta. 

Lomakkeelle täytetään 
* sähköposti (käyttäjätunnus) ja
* salasana ja
* "muista minut" -kenttä.

Sähköposti ja salasana ovat pakolliset.

Palveluun kirjaudutaan klikkaamalla "Kirjaudu"-painiketta. Jos käyttäjä on valinnut "Muista minut" -kentän, kirjautumistiedot tallennetaan kirjautumisen yhteydessä selaimen tunnistautumistietoihin. 

Jos lomakkeella on virheitä, kuten puuttuvia tietoja tai virheelliset tunnukset, käyttäjälle näytetään ilmoitus.
Kun kirjautuminen onnistuu, käyttäjä ohjataan palvelun etusivulle. 


#### Rekisteröityminen

Käyttäjä voi pyytää palveluun käyttöoikeutta [rekisteröitymislomakkeella](https://shielded-brook-33904.herokuapp.com/auth/register). 
Palvelun käyttö edellyttää, että palvelun ylläpitäjä aktivoi käyttöoikeuden rekisteröitymisen jälkeen.

Rekisteröitymislomakkeelle täytetään:
* Sähköpostiosoite (toimii käyttäjätunnuksena)
* Etunimi
* Sukunimi
* Salasana ja salasanan vahvistus

Kaikki tiedot ovat pakollisia. 

Rekisteröitymislomake lähetetään klikkaamalla Lähetä-painiketta. 

Jos lomakkeella on virheitä kuten puuttuvia tietoja, käyttäjälle näytetään ilmoitus ja pyydetään korjaamaan virheelliset tiedot. 
Kun lomakkeen tallentaminen onnistuu, käyttäjälle näytetään ilmoitus.


### Kirjautuneen käyttäjän toiminnot

#### Sivujen yhteiset toiminnot

##### Yläpalkki

Yläpalkissa näytetään palvelun logo (linkki etusivulle), käyttäjän nimi, linkki omien tietojen muokkaussivulle ja kirjaudu ulos -linkki. 

##### Vasen valikko

Vasemmassa valikossa näytetään linkki etusivulle, linkit käyttäjän yrityksen raportteihin. 
Ylläpitäjälle näytetään lisäksi linkit ylläpitotoimintoihin (käyttäjät, analyysit).

#### Etusivu

##### Uusin raportti -lohko

Uusin raportti -lohkossa näytetään yhteenveto käyttäjän yritykselle viimeksi valmistuneesta raportista. 
Katso tiedot -linkkiä klikkaamalla pääsee raportin tarkempiin tietoihin.  

#### Omien tietojen muuttaminen

Omien tietojen muutoslomakkeelle pääsee yläpalkin Omat tiedot -linkin kautta. 

Lomakkeella voi muuttaa etu- ja sukunimeä. Molemmat tiedot ovat pakolliset. Sähköpostiosoite toimii käyttäjätunnuksena, joten sitä ei voi muuttaa. 

Muutokset tallennetaan Tallenna -painiketta klikkaamalla. Muutokset voi perua Peruuta -painiketta klikkaamalla.

Jos lomakkeella on virheitä, käyttäjälle näytetään ilmoitus ja pyydetään korjaamaan virheelliset tiedot.
Kun lomakkeen tallentaminen onnistuu, käyttäjälle näytetään ilmoitus.
Jos käyttäjä klikkaa Peruuta-painiketta, selain ohjataan etusivulle. 

#### Salasanan vaihto

Salasanan vaihtolomakkeelle pääsee yläpalkin Omat tiedot -linkin kautta. 

Lomakkeelle annetaan salasana ja salasanan vahvistus. Molemmat tiedot ovat pakolliset ja niiden tulee olla samat.

Muutokset tallennetaan Tallenna -painiketta klikkaamalla. Muutoksen voi perua Peruuta -painiketta klikkaamalla.

Jos lomakkeella on virheitä, käyttäjälle näytetään ilmoitus ja pyydetään korjaamaan virheelliset tiedot.
Kun lomakkeen tallentaminen onnistuu, käyttäjälle näytetään ilmoitus. 
Jos käyttäjä klikkaa Peruuta-painiketta, selain ohjataan etusivulle. 

#### Raportin katselu

#### Kirjautuminen ulos

Palvelusta kirjaudutaan ulos yläpalkin Kirjaudu ulos -linkkiä klikkaamalla. 
Uloskirjautumisen jälkeen selain ohjataan palvelun aloitussivulle.

### Ylläpitäjän toiminnot

#### Käyttäjät

##### Käyttäjien selaus

##### Käyttäjän lisäys

##### Käyttäjän muokkaus

##### Käyttäjän tietojen katselu

##### Käyttäjän poisto

#### Analyysit

##### Analyysien selaus

##### Analyysin lisäys

##### Analyysin muokkaus

##### Analyysin tietojen katselu

##### Analyysin poisto

##### Raportin teko / katselu