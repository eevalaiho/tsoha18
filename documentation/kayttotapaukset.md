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

avainsanalista

get_keywords

avainsanakohtaiset osumat

get_targets_by_keyword
