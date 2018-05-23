#Käyttäjätarinat

##Käyttäjä

Käyttäjänä haluan, että:
* voin kirjautua sovellukseen tunnus-salasanaparilla
* voin katsella käyttäjätietojani ja muokata nimi- ja yhteystietojani
* voin vaihtaa salasanani
* voin katsella yritykselleni tehtyjä analyysejä
* analyysit on luokitelty asian ja kohteen mukaan
* voin suodattaa analyysien näkymän asian ja/tai tyypin mukaan
* (saan tallennettua raportit ja analyysit pdf-muodossa omalle työasemalleni)
* muiden yritysten käyttäjät eivät voi katsella yritykseni tietoja 

##Ylläpitäjä

Ylläpitäjänä haluan että:
* voin katsella asiakkainen analyysejä juuri sellaisina, kuin asiakkaat itse ne näkevät
* pääsen sovelluksen ylläpitonäkymään
* voin lisätä, muokata ja poistaa sovelluksen käyttäjiä
* voin luoda, muokata ja poistaa raportteja asiakkaan nettinäkyvyydestä

##Pääylläpitäjä

Pääylläpitäjänä haluan, että:
* voin lisätä, muokata ja poistaa sovelluksen ylläpitäjiä
(* voin lisätä sovellukseen asiakkaita)

##Vahingoittava käyttäjä

Vahingoittava käyttäjänä haluan, että:
* pääsen katsomaan sovelluksen tietoja mihin minulla ei ole oikeutta
* pääsen muuttamaan tai poistamaan sovelluksen tietokannan sisältöä

## Vanhaa pohdintaa - POISTA

Ks mallia esim (Tarkennetut käyttäjätarinat)[https://confluence.csc.fi/pages/viewpage.action?pageId=33525302]


Ajatuksia / käyttötapauksia
* Asiakas voi tilata itselleen tiivisteitä nettinäkyvyydestään. 
    * Sopimusasiakas, anonyymille käyttäjälle näytetään infosivu
* Seurattavia asioita voi olla useita
* Asiakohtaisesti määritellään seurattavat kohteet (esim uutissivustot, sosiaalisen median feedit, haku) ja avainsanat (asiakkaan nimi, toimialue, tuotteet jne)
* Asiakkuustasoja voisi olla useita riippuen siitä mitä seurataan
    * Asioiden määrä
    * Kanavien määrä ja laatu (esim vain uutissisältö, uutis- ja sosiaalisen median kanavat, jne)
    * Analyysin taso
    * Jatkuva analyysi / kerta-analyysi
* Määritellyt seurattavat kohteet "skannataan" ja ne analysoidaan NLTK:n (tai vastaavan) avulla
    * Suomen kielen tuki pitää tarkistaaa ja mahdollisesti pitää käyttää englanninkielisiä lähteitä ja avainsanoja
* Tehdyn analyysin perusteella tuotetaan raportti näkyvyydestä
    * Mainintojen määrä ja laatu 
    * Lyhennelmä / lyhennelmät
    * Graafit
* Ei avointa rekisteröitymistä, ylläpitäjä luo asiakkaat tai ne on valmiina järjestelmässä 
* Ylläpitäjä liittää asiakkaaseen seurattavat kohteet ja seurantaaikataulun
    * Palvelun laajuus on "sopimus"asia
* Asiakkaalla on etusivu, mistä pääsee seuraamaan raportteja
    * mm Voyant-garfiikaa?