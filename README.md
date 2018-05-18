# Aineopintojen harjoitustyö: tietokantasovellus, kesä 2018
Eeva-Maria Laiho

## Julkisuusseuranta valitun avainsanan / avainsanojen ympäriltä

Aiheen motivaationa on NLTK:n ominaisuuksiin tutustuminen ja mielekäs hyödyntäminen tietokantaprojektissa sekä mahdollisesti data-analyysin graafisiin työkaluihin tutustuminen. 

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

Tieto-olioita
* Asiakas (customer)
    * customer_id, name
* Asia (subject)
    * subject_id, title, keywords
* Seurattavat kohteet (target)
    * target_id, title, type, uri
* Asian seurattavat kohteet (subject_target)
    * subject_id, target_id
* Työ (job)
    * subject, status, start_time, finnish_time, analysis_id
* Analysis
    * analysis_id