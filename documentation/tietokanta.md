# Tietokanta

### Tieto-olioita (pohdintaa)
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
       
### Tietokantakaavio

![Tietokantakaavio](./graph.png)

### Yhteenvetokyselyt

Käyttäjälle näytetään etusivulla yhteenveto uusimmasta analyysistä:
* Kuinka monta kohdetta (url) analyysiin otettiin mukaan
* Kuinka monta avainsanamainintaa analyysissä löydettiin

Samat tiedot myös analyysin omalle sivulle.

Analyysien listaus
* Näytetään analyysiin löydettyjen kohteiden määrä

### Raporttidatan tallennusmuoto

Raporttidata tallennetaan json-muodossa, sillä datan käsittely on silloin helpompaa 
[Realpython.com: Python Supports JSON Natively!](https://realpython.com/python-json/#python-supports-json-natively)