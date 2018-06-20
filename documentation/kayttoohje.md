# Käyttöohje


### Yleistä 

Sovellus on asennettu Herokussa osoitteeseen: [https://shielded-brook-33904.herokuapp.com/](https://shielded-brook-33904.herokuapp.com/)

Käyttäjätunnukset: 
* Sähköposti: paivio@tsoha18, salasana: salainen (pääylläpitäjä)
* Sähköposti: aukusti@asianajotoimisto, salasana: salainen (asiakas)
* Sähköposti: ida@ideahautomo, salasana: salainen (asiakas)


### Tunnistamattoman käyttäjän toiminnot

#### Kirjautuminen

Palveluun kirjaudutaan [aloitussivun](https://shielded-brook-33904.herokuapp.com) kirjautumislomakkeelta. 

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

Lomakkeella voi muuttaa etu- ja sukunimeä. Molemmat tiedot ovat pakolliset. Sähköpostiosoite toimii käyttäjätunnuksena ja sitä ei voi muuttaa. 

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

Raportin katselunäkymään pääsee vasemman valikon raportit-kohdan linkeistä ja etusivun uusin raportti -lohkon linkistä.

Raportin katselunäkymässä näytetään raportin tiedot: valmistumisaika ja analyysissä käytetyt avainsanat, 
sanapilvi löydetyistä avainsanoista ja kohteiden luettelo avainsanoittain. Kohdeluettelossa näytetään 
löydetyt yksittäiset avainsanat kohteittain. 

#### Kirjautuminen ulos

Palvelusta kirjaudutaan ulos yläpalkin Kirjaudu ulos -linkkiä klikkaamalla. 
Uloskirjautumisen jälkeen selain ohjataan palvelun aloitussivulle.



### Ylläpitäjän toiminnot

#### Käyttäjät

##### Käyttäjien selaus

Käyttäjien selausnäkymään pääsee vasemman valikon Ylläpito-kohdan Käyttäjät-linkin kautta. 

Käyttäjien selausnäkymässä näytetään listaus sovelluksen käyttäjistä. 
Käyttäjistä näytetään tiedot id-tunniste, etunimi, sukukunimi, yrityksen nimi ja hyväksytty-tieto ja 
toimintopainikkeet käyttäjän tietojen katseluun, muokkaamiseen ja poistamiseen. 

Listauksen alapuolella näytetään linkkipainike uuden käyttäjän lisäykseen. 
Painikkeen klikkaa ohjaa uuden käyttäjän lisäyslomakkeelle. 

##### Käyttäjän lisäys

Käyttäjän lisäyslomakkeelle pääsee käyttäjän selausnäkymästä. Lisäyslomakkeelle annetaan 
käyttäjän tiedot: sähköposti (toimii käyttäjätunnuksena), yritys, etunimi, sukunimi ja salasana, 
valitaan käyttäjäryhmät ja hyväksytty -tieto. 

Käyttäjän tiedot tallennetaan tallenna-painikkeesta. Kun lomake tallennetaan, se validoidaan. 
Jos lomakkeella on virheitä, järjestelmä pyytää korjaamaan ne.

Toiminto peruutetaan Peruuta-painiketta klikkaamalla.

##### Käyttäjän tietojen katselu

Käyttäjän tietojen katselunäkymään pääsee käyttäjän selausnäkymästä. Näkymässä näytetään 
kaikki käyttäjän tiedot. Näkymältä pääsee takaisin käyttäjäluetteloon Takaisin-painiketta
klikkaamalla.

##### Käyttäjän muokkaus

Käyttäjän muokkauslomakkeelle pääsee käyttäjän selausnäkymästä. Muokkauslomakkeelle annetaan 
käyttäjän tiedot: yritys, etunimi, sukunimi, valitaan käyttäjäryhmät ja hyväksytty -tieto. 

Käyttäjän tiedot tallennetaan tallenna-painikkeesta. Kun lomake tallennetaan, se validoidaan. 
Jos lomakkeella on virheitä, järjestelmä pyytää korjaamaan ne.

Toiminto peruutetaan Peruuta-painiketta klikkaamalla.

##### Käyttäjän poisto

Käyttäjä voidaan poistaa käyttäjän selaus- ja muokkausnäkymästä. Poistamiseen pyydetään vahvistus.


#### Analyysit

##### Analyysien selaus

Analyysien selausnäkymään pääsee vasemman valikon Ylläpito-kohdan Analyysit-linkin kautta. 

Analyysien selausnäkymässä näytetään listaus analyyseistä. 
Analyysistä näytetään tiedot id-tunniste, yrityksen nimi, analyysin nimi, avainsanat ja lukittu-tieto sekä
toimintopainikkeet analyysin tietojen katseluun, muokkaamiseen ja poistamiseen sekä painike raportin tekemiseen. 

Listauksen alapuolella näytetään linkkipainike uuden analyysin lisäykseen. 
Painikkeen klikkaaminen ohjaa uuden analyysin lisäyslomakkeelle. 

##### Analyysin lisäys / muokkaus

Analyysin lisäyslomakkeelle pääsee analyysien selausnäkymästä. Lisäyslomakkeelle annetaan 
analyysin tiedot: yritys, nimi, avainsanat pilkkueroteltuna listana, kohteet rivinvahdolla 
eroteltuna ja lukittu-tieto.

Analyysin tiedot tallennetaan tallenna-painikkeesta. Kun lomake tallennetaan, se validoidaan. 
Jos lomakkeella on virheitä, järjestelmä pyytää korjaamaan ne.

Toiminto peruutetaan Peruuta-painiketta klikkaamalla.

Tee raportti -painikkeesta (vain muokkaus) pääsee raportinluomisnäkymään.

##### Analyysin tietojen katselu

Analyysin katselunäkymään pääsee analyysien selausnäkymästä. Näkymässä näytetään 
kaikki analyysin tiedot. 

Näkymältä pääsee takaisin anayysiluetteloon Takaisin-painiketta klikkaamalla.

Tee raportti -painikkeesta (vain muokkaus) pääsee raportinluomisnäkymään.

##### Analyysin poisto

Analyysi voidaan poistaa analyysin selaus- ja muokkausnäkymästä. Poistamiseen pyydetään vahvistus.

##### Raportin teko / katselu

Raportin tekoon pääsee analyysin listaus-, katselu- ja muokkausnäkymien kautta.

Raporttiajon käynnistetään "Käynnistä raporttiajo" -painikkeella. Raporttiajo:
* kerää analyysin kohteiksi annetuilta sivuilta url-osoitteita,
* hakee löydettyjen ensimmäisen ja toisen tason sivujen palauttaman html:n
* parseroi ja siivoaa niistä html:n, css:n ja skriptin (boilerplate)
* analysoi NLTK:n avulla sivujen sisältöjä ja
* koostaa raporttitietoja. 

Analysoitavien toisen tason sivujen määrä on rajoitettu 5:n alisivuun (koska demo). 
Raporttiajo kestää kuitenkin varsin kauan eikä sitä kannatakaan kokeilla kovin monella kohteella, 
esim 2 kohdetta demonstroinee sovelluksen toimintaa riittävästi.

Kun raporttiajo on mennyt läpi, sivulla näytetään raporttiajon tulokset: kohteet ja niiden alikohteet. 
Alikohteen otsikon klikkaaminen avaa sivulle alikohteen tarkemmat tiedot. 
Näytä yksityiskohtaiset tiedot -linkki avaa NLTK-analyysin raakadatan näkymälle.

Raporttiajon voi tehdä uudestaan. Tämä tyhjentää aiemmin tehdyn raportin tiedot. Käyttäjältä
pyydetään ensin varmistus.

Raportilta pääsee pois Takaisin -painikkeella.