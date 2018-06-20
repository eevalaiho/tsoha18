# Tietokanta

### Tietokantakaavio

![Tietokantakaavio](./graph.png)

##### NLTK-analyysin tulosten tallennusmuoto

NLTK-analyysin tulokset tallennetaan Ttarget-taulun nltk_analysis-kenttään JSON-muodossa. 
Koska kehitysympäristössä on käytössä SQLite, kentän tietotyyppi on tietokannassa TEXT ja myös kaaviossa näin. 
Sovelluksen puolella käytetään sqlalchemy_utils -kirjaston JSONType -tietotyyppiä.

### Tietokannan luontilauseet

```
BEGIN TRANSACTION;
CREATE TABLE company (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(50) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE role (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(100) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	firstname VARCHAR(50) NOT NULL, 
	lastname VARCHAR(50) NOT NULL, 
	username VARCHAR(254) NOT NULL, 
	password VARCHAR(50) NOT NULL, 
	company_id INTEGER, 
	active BOOLEAN, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	FOREIGN KEY(company_id) REFERENCES company (id), 
	CHECK (active IN (0, 1))
);
CREATE TABLE accountrole (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	role_id INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(role_id) REFERENCES role (id) ON DELETE CASCADE, 
	FOREIGN KEY(account_id) REFERENCES account (id) ON DELETE CASCADE
);
CREATE TABLE analysis (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	company_id INTEGER NOT NULL, 
	name VARCHAR(50) NOT NULL, 
	keywords VARCHAR(150) NOT NULL, 
	locked BOOLEAN NOT NULL, 
	date_crawled DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(company_id) REFERENCES company (id), 
	CHECK (locked IN (0, 1))
);
CREATE TABLE ttarget (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	analysis_id INTEGER NOT NULL, 
	url VARCHAR(255) NOT NULL, 
	ttarget_id INTEGER, 
	title VARCHAR(255), 
	lang VARCHAR(2), 
	word_count INTEGER, 
	key_word_count INTEGER, 
	nltk_analysis TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(analysis_id) REFERENCES analysis (id), 
	FOREIGN KEY(ttarget_id) REFERENCES ttarget (id)
);
COMMIT;
```

### Kehitystietokannan populointi
```
BEGIN TRANSACTION;

INSERT INTO company (id,date_created,date_modified,name) VALUES (1,'2018-06-19 15:49:40','2018-06-19 15:49:40','Tsoha 18');
INSERT INTO company (id,date_created,date_modified,name) VALUES (2,'2018-06-19 15:49:40','2018-06-19 15:49:40','Aukustin asianajotoimisto Ky');
INSERT INTO company (id,date_created,date_modified,name) VALUES (3,'2018-06-19 15:49:40','2018-06-19 15:49:40','Idan ideahautomo');

INSERT INTO role (id,date_created,date_modified,name) VALUES (1,'2018-06-19 15:49:40','2018-06-19 15:49:40','Pääylläpitäjä');
INSERT INTO role (id,date_created,date_modified,name) VALUES (2,'2018-06-19 15:49:40','2018-06-19 15:49:40','Ylläpitäjä');
INSERT INTO role (id,date_created,date_modified,name) VALUES (3,'2018-06-19 15:49:40','2018-06-19 15:49:40','Asiakas');

INSERT INTO account (id,date_created,date_modified,firstname,lastname,username,password,company_id,active) VALUES (1,'2018-06-19 15:49:40','2018-06-19 15:49:40','Päiviö','Pääkäyttäjä','paivio@tsoha18','salainen',1,1);
INSERT INTO account (id,date_created,date_modified,firstname,lastname,username,password,company_id,active) VALUES (2,'2018-06-19 15:49:40','2018-06-19 15:49:40','Yngve','Ylläpitäjä','yngve@tsoha18','salainen',1,1);
INSERT INTO account (id,date_created,date_modified,firstname,lastname,username,password,company_id,active) VALUES (3,'2018-06-19 15:49:40','2018-06-19 15:49:40','Aukusti','Asiakas','aukusti@asianajotoimisto','salainen',2,1);
INSERT INTO account (id,date_created,date_modified,firstname,lastname,username,password,company_id,active) VALUES (4,'2018-06-19 15:49:40','2018-06-19 15:49:40','Akuliina','Asiakas','akuliina@asianajotoimisto','salainen',2,1);
INSERT INTO account (id,date_created,date_modified,firstname,lastname,username,password,company_id,active) VALUES (5,'2018-06-19 15:49:40','2018-06-19 15:49:40','Ida','Asiakas','ida@ideahautomo','salainen',3,1);

INSERT INTO accountrole (id,date_created,date_modified,role_id,account_id) VALUES (1,'2018-06-19 15:49:40','2018-06-19 15:49:40',1,1);
INSERT INTO accountrole (id,date_created,date_modified,role_id,account_id) VALUES (2,'2018-06-19 15:49:40','2018-06-19 15:49:40',2,1);
INSERT INTO accountrole (id,date_created,date_modified,role_id,account_id) VALUES (3,'2018-06-19 15:49:40','2018-06-19 15:49:40',2,2);
INSERT INTO accountrole (id,date_created,date_modified,role_id,account_id) VALUES (4,'2018-06-19 15:49:40','2018-06-19 15:49:40',3,3);
INSERT INTO accountrole (id,date_created,date_modified,role_id,account_id) VALUES (5,'2018-06-19 15:49:40','2018-06-19 15:49:40',3,4);
INSERT INTO accountrole (id,date_created,date_modified,role_id,account_id) VALUES (6,'2018-06-19 15:49:40','2018-06-19 15:49:40',3,5);

INSERT INTO analysis (id,date_created,date_modified,company_id,name,keywords,locked,date_crawled) VALUES (1,'2018-06-19 15:49:40','2018-06-19 15:49:40',3,'Idan tiedeuutiset','luontopaneeli,ilmastonmuutos,aranda,uv-säteily,ilmakehä',0,NULL);
INSERT INTO analysis (id,date_created,date_modified,company_id,name,keywords,locked,date_crawled) VALUES (2,'2018-06-19 15:49:40','2018-06-19 15:49:40',3,'Idan keskeneräinen analyysi','',0,NULL);
INSERT INTO analysis (id,date_created,date_modified,company_id,name,keywords,locked,date_crawled) VALUES (3,'2018-06-19 15:49:40','2018-06-19 15:49:40',2,'Aukustin asianajotoimiston ilmastopoiminnat','revontulet,arktinen,meteorologi,itämeri',0,NULL);

INSERT INTO ttarget (id,date_created,date_modified,analysis_id,url,ttarget_id,title,lang,word_count,key_word_count,nltk_analysis) VALUES (1,'2018-06-19 15:49:40','2018-06-19 15:49:40',1,'https://www.aka.fi/fi/tietysti/tiedeuutiset/tiedeuutisia-suomesta1/',NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO ttarget (id,date_created,date_modified,analysis_id,url,ttarget_id,title,lang,word_count,key_word_count,nltk_analysis) VALUES (2,'2018-06-19 15:49:40','2018-06-19 15:49:40',1,'https://ilmastotieto.wordpress.com/ilmastouutiset/',NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO ttarget (id,date_created,date_modified,analysis_id,url,ttarget_id,title,lang,word_count,key_word_count,nltk_analysis) VALUES (3,'2018-06-19 15:49:40','2018-06-19 15:49:40',3,'http://ilmatieteenlaitos.fi/tiedeuutisten-arkisto',NULL,NULL,NULL,NULL,NULL,NULL);

COMMIT;

```

### Yhteenvetokyselyt

Yhteenvetokyelyt on kuvattu käyttötapauksittain dokumentissa [Käyttötapaukset](./documentation/kayttotapaukset.md).
