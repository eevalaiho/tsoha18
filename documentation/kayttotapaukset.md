# Käyttötapaukset

Tähän dokumenttiin on kirjattu järjestelmän keskeiset käyttötapaukset. Järjestelmän perus-
toiminnallisuudet on kuvattu [käyttöohjeessa](./documentation/kayttoohje.md).

### Uusin raportti -lohko

Kirjautuneelle käyttäjälle näytetään etusivulla Uusin raportti -lohko, kun käyttäjän
yritykselle on valmistunut raportteja. 

Lohkossa näytetään yhteenveto käyttäjän yritykselle viimeksi valmistuneesta raportista. 
Raportin tiedot haetaan sql:llä:
```
SELECT Analysis.id, Analysis.name, SUM(Ttarget.key_word_count), Analysis.date_crawled
FROM Analysis
INNER JOIN Ttarget ON Analysis.id = Ttarget.analysis_id
GROUP BY Analysis.id, Analysis.name, Analysis.date_crawled 
HAVING Analysis.id = <ANALYYSIN_ID>
ORDER BY Analysis.date_crawled desc
```
, missä analyysin id välitetään parametrina.

Katso tiedot -linkkiä klikkaamalla pääsee katsomaan raportin tarkempia tietoja.

### Ylläpitäjän raporttinäkymä

### Käyttäjän raporttinäkymä

