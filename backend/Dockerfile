FROM solr:8.10

COPY fake_clean.json data/fake_clean.json

COPY schema1.json /data/schema1.json

COPY schema2.json /data/schema2.json

COPY schema3.json /data/schema3.json

COPY stopwords.txt /data/stopwords.txt

COPY synonyms.txt /data/synonyms.txt

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
