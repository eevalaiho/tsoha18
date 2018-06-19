--# https://www.sqlite.org/json1.html

--select json_extract(ttarget.nltk_analysis, '$.lang') from ttarget
--select json_extract(ttarget.nltk_analysis, '$.key_words') from ttarget
--select sum(json_extract(ttarget.nltk_analysis, '$.key_words."Ilmasto"')) from ttarget


select key, sum(value) as count
from  (
		select  data.value as keywords 
		from ttarget, json_each(ttarget.nltk_analysis) as data
		where key = "key_words" and ttarget.analysis_id=1
	) as subq, json_each(subq.keywords)
group by key
order by key