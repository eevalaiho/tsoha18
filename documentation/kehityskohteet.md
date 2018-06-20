# Kehityskohteet ja rajoitukset

### Rajoitukset

Sovelluksen alikohteet on rajattu kahteen (kovakoodattu rajaus). Pääkohteitakaan ei kannattane 
määrittää kuin muutama yhteen raporttiajoon.

Sovellus tukee vain html-dokumenttien analysointia. 

### Kehityskohteita

NLTK:n laajempi hyödyntäminen jäi sovelluksessa oikeastaan pintaraapaisuksi, sillä harjoitustyön
pakollisten vaatimusten toteuttaminen vei kuitenkin paljon aikaa. NLTK-analyysin laajentaminen ja 
tulosten esittämisen toteutus onnistuisi nähdäkseni kohtuullisen vähällä vaivalla, esimerkiksi 
yhden lisäviikon aikana.

Toteutuksen näkökulma on ollut tekninen ja sovellusta pitäisikin miettiä käyttäjän näkökulmasta:  mitä 
käyttäjä haluaisi analysoitavan ja/tai analyysin tuloksena tietää? 

Kehityskannaksi pitäisi vaihtaa PostgreSQL - nyt turhaa säätöä Postge:n ja SQLiten välillä.

NLTK-raporttien ajo pitäisi erottaa erilliseksi web-sovelluksesta riippumattomaksi sovellukseksi. 
Raporttiajoa pitäisi myös refaktoroida ja selvittää hyvät tehokkaat toteutustavat ja ohjelmistokirjastot. 
Nyt toteutus on POC-tasoinen.


