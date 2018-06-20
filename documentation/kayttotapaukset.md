# Käyttötapaukset

Tähän dokumenttiin on kirjattu järjestelmän keskeiset käyttötapaukset. Järjestelmän 
perustoiminnallisuudet on kuvattu [käyttöohjeessa](./documentation/kayttoohje.md).

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


### Käyttäjän raporttinäkymä

##### Avainsanapilvi

Valmistuneella raportilla näytetään sanapilvi analyysin tuloksena löydetyistä 
avainsanoista. 

Sanapilven data haetaan sql:llä:

```
select key, sum(cast(cast(value as varchar) as integer)) as _count
from (
    select data.value as keywords
    from ttarget, json_each(ttarget.nltk_analysis) as data
    where key = 'key_words' and ttarget.analysis_id= <ANALYYSIN_ID>  and lang is not null
) as subq, json_each(subq.keywords)
group by key
order by key
```
, missä analyysin id välitetään parametrina. Tässä kyselyssä SQLiten ja PostgreSQL:n 
JSON toteutukset eroavat toisistaan ja Postgrea varten avainsanaosumien määrä täytyy
castata integeriksi näin ```sum(cast(cast(value as varchar) as integer))```. Tämä muoto 
kelpaa myös SQLite:lle, kun nätimpää ```sum(value::varchar::int)``` SQLite ei hyväksy.

Sanapilvi tyylitellään javascriptin ja css:n avulla niin, että avainsanat saavat 
painoarvonsa mukaisen värin ja tekstikoon. Kunkin avainsanan yksilöllinen painoarvo 
lasketaan osumamäärän osuutena eniten osumia saaneen avainsanan osumamäärästä. 
Painoarvo muutetaan kokonaisluvuksi niin että "painavimmat" avainsanat saavat arvon 4 
(jakopisteet 5%, 50%, 95%). Avainsanan css-tyyli asetetaan saadun kokonaislukuarvon
mukaan.


##### Kohteet avainsanoittain

Kohteet avainsanoittain -luettelossa näytetään luettelo kaikista löytyneistä avaisanoista 
ja niihin liittyvät kohteet ja avainsanojen määrät niistä. Luettelo muodostetaan niin, että 
ensin haetaan avainsanat ja sen jälkeen kohteet jokaiselle avainsanalle. 

Avainsanat haetaan sql-llä:
```
SELECT DISTINCT key
FROM (
    SELECT data.value AS keywords
    FROM ttarget, json_each(ttarget.nltk_analysis) AS data
    WHERE key = 'key_words' AND ttarget.analysis_id= <ANALYYSIN_ID>
) AS subq, json_each(subq.keywords)
ORDER BY key
```
, missä analyysin id välitetään parametrina. 

Avainsanakohtaisten kohteiden haussa SQLiten ja PostgreSQL:n JSON-toteutukset poikkeavat
niin merkittävästi toisistaan, että eri ympäristöihin on täytynyt tehdä eri kyselyt:

SQLite-tietokannasta tiedot haetaan sql:llä:
```
SELECT ttarget.*, json_extract(ttarget.nltk_analysis, <POLKU>) AS kw_count
FROM ttarget
WHERE analysis_id= <ALAYYSIN_ID> AND json_extract(ttarget.nltk_analysis, <POLKU>) IS NOT NULL
ORDER BY kw_count DESC
```

, missä analyysin id ja JSON-datan polku välitetään parametreina. Polkuparametri on merkkijono ja 
muotoa ```$.key_words.<AVAINSANA>```.

Postgre-tietokannasta tiedot haetaan sql:llä
```
SELECT ttarget.*, COALESCE(data.kw_count, 0) as kw_count
FROM ttarget 
INNER JOIN (SELECT ttarget.id AS ttarget_id, SUM((key_words->><AVAINSANA>)::int) AS kw_count
            FROM ttarget, json_extract_path(ttarget.nltk_analysis, 'key_words') AS key_words
            GROUP BY ttarget.id
            HAVING SUM((key_words->><AVAINSANA>)::int) > 0) AS data ON data.ttarget_id = ttarget.id
WHERE ttarget.analysis_id = <ANALYYSIN_ID>
```
, missä analyysin id ja avainsana välitetään parametreina. 

### Ylläpitäjän raporttinäkymä

TULOSSA