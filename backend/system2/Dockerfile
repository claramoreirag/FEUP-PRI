FROM solr:8.10

COPY fake_clean.json data/fake_clean.json

COPY schema.json /data/schema.json

COPY stopwords.txt /data/stopwords.txt

COPY synonyms.txt /data/synonyms.txt

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
