# Käyttötapaukset

Tähän dokumenttiin on kirjattu järjestelmän keskeiset käyttötapaukset. Järjestelmän 
perustoiminnallisuudet (kuten rekisteröityminen, kirjautuminen ja käyttäjähallinta) on 
kuvattu lisäksi [käyttöohjeessa](./documentation/kayttoohje.md).


### Uusin raportti -lohko

Uusin raportti -lohkossa näytetään yhteenveto käyttäjän yritykselle viimeksi valmistuneesta raportista. 
Raportin tiedot haetaan kyselyllä:
```
SELECT Analysis.id, Analysis.name, SUM(Ttarget.key_word_count), Analysis.date_crawled
FROM Analysis
INNER JOIN Ttarget ON Analysis.id = Ttarget.analysis_id
GROUP BY Analysis.id, Analysis.name, Analysis.date_crawled 
HAVING Analysis.id = :id
ORDER BY Analysis.date_crawled desc
```
, missä analyysin id välitetään parametrina :id.

Lohko näytetään sivuston etusivulla, kun käyttäjän yritykselle on valmistunut raportteja. 


### Avainsanaosumat / avainsanapilvi

Avainsanaosumat / avainsanapilvi on luettelo analyysin tuloksena löydetyistä avainsanoista ja
avainsanaosumien määrä. 

Avainsanat ja osumat haetaan kyselyllä:

```
SELECT key, SUM(CAST(CAST(value AS VARCHAR) AS INTEGER)) AS _count
FROM (
    SELECT data.value AS keywords
    FROM ttarget, JSON_EACH(ttarget.nltk_analysis) AS data
    WHERE key = 'key_words' AND ttarget.analysis_id= :id AND lang IS NOT NULL
) AS subq, JSON_EACH(subq.keywords)
GROUP BY key
ORDER BY key
```
, missä analyysin id välitetään parametrina :id. 

Kyselyyn tuo moninmutkaisuutta se, että SQLiten ja PostgreSQL:n JSON toteutukset 
eroavat toisistaan. PostgreSQL:ssä avainsanaosumien määrän tietytyyppi on JSON 
ja se täytyy castata integeriksi, että voidaan laskea summa. Castaus täytyy vieläpä tehdä 
merkkijonon kautta, sillä JSONia ei voi castata integeriksi suoraan.
Muoto ```SUM(CAST(CAST(value AS VARCHAR) AS INTEGER))``` kelpaa SQLite:lle. 
PostgreSQL:lle kelpaavaa nätimpää muotoa ```SUM(value::varchar::int)``` SQLite ei hyväksy.

Avainsanaosumat näytetään ylläpitäjän raportilla.

Avainsanapilvi näytetään kirjautuneen käyttäjän raportilla.

Avainsanapilvi tyylitellään javascriptin ja css:n avulla niin, että avainsanat saavat 
painoarvonsa mukaisen värin ja tekstikoon. Kunkin avainsanan yksilöllinen painoarvo 
lasketaan osumamäärän osuutena eniten osumia saaneen avainsanan osumamäärästä. 
Painoarvo muutetaan kokonaisluvuksi niin että "painavimmat" avainsanat saavat arvon 4 
(jakopisteet 5%, 50%, 95%). Avainsanan css-tyyli asetetaan saadun kokonaislukuarvon
mukaan.


### Kohteet avainsanoittain

Kohteet avainsanoittain -luettelossa näytetään cd luettelo kaikista löytyneistä avaisanoista 
ja niihin liittyvät kohteet ja avainsanojen määrät niistä. Luettelo muodostetaan niin, että 
ensin haetaan avainsanat ja sen jälkeen kohteet jokaiselle avainsanalle. 

Avainsanat haetaan sql-llä:
```
SELECT DISTINCT key
FROM (
    SELECT data.value AS keywords
    FROM ttarget, JSON_EACH(ttarget.nltk_analysis) AS data
    WHERE key = 'key_words' AND ttarget.analysis_id= :id
) AS subq, JSON_EACH(subq.keywords)
ORDER BY key
```
, missä analyysin id välitetään parametrina :id. 

Avainsanakohtaisten kohteiden haussa SQLiten ja PostgreSQL:n JSON-toteutukset poikkeavat
niin merkittävästi toisistaan, että eri ympäristöihin on omat kyselyt:

SQLite-tietokannasta data haetaan kyselyllä:
```
SELECT ttarget.*, JSON_EXTRACT(ttarget.nltk_analysis, :path) AS kw_count
FROM ttarget
WHERE analysis_id= :id AND JSON_EXTRACT(ttarget.nltk_analysis, :path) IS NOT NULL
ORDER BY kw_count DESC
```

, missä analyysin id välitetään parametrina :id ja JSON-datan polku parametreina :path. 
Polkuparametri on merkkijono ja sen tulee olla muotoa ```'$.key_words."<string>"'```, siis esimerkiksi
```'$.key_words."ilma"'```, kun haetaan sanan ilma esiintymiä.

PostgreSQL-tietokannasta data haetaan kyselyllä:
```
SELECT ttarget.*, COALESCE(data.kw_count, 0) as kw_count
FROM ttarget 
INNER JOIN (SELECT ttarget.id AS ttarget_id, SUM((key_words->>:keyword)::int) AS kw_count
            FROM ttarget, JSON_EXTRACT_PATH(ttarget.nltk_analysis, 'key_words') AS key_words
            GROUP BY ttarget.id
            HAVING SUM((key_words->>:keyword)::int) > 0) AS data ON data.ttarget_id = ttarget.id
WHERE ttarget.analysis_id = :id
```
, missä analyysin id välitetään parametrina :id ja avainsana parametrina :keyword. 

Avainsanapilvi näytetään kirjautuneen käyttäjän raportilla.


