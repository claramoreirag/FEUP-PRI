#!/bin/bash
precreate-core system0
precreate-core system1
precreate-core system2
precreate-core system3

# Start Solr in background mode so we can use the API to upload the schema
solr start

sleep 10

cat /data/stopwords.txt > /opt/solr/example/files/conf/stopwords.txt
cat /data/stopwords.txt > /opt/solr-8.10.1/example/files/conf/stopwords.txt
cat /data/stopwords.txt > /var/solr/data/system2/conf/stopwords.txt
cat /data/stopwords.txt > /var/solr/data/system3/conf/stopwords.txt

cat /data/synonyms.txt > /opt/solr/example/files/conf/synonyms.txt
cat /data/synonyms.txt > /opt/solr-8.10.1/example/files/conf/synonyms.txt
cat /data/synonyms.txt > /var/solr/data/system2/conf/synonyms.txt
cat /data/synonyms.txt > /var/solr/data/system3/conf/synonyms.txt

curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema1.json \
    http://localhost:8983/solr/system1/schema

curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema2.json \
    http://localhost:8983/solr/system2/schema

curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema3.json \
    http://localhost:8983/solr/system3/schema


# Populate collection
bin/post -c system0 ./data/fake_clean.json
bin/post -c system1 ./data/fake_clean.json
bin/post -c system2 ./data/fake_clean.json
bin/post -c system3 ./data/fake_clean.json


sleep 3

# Restart in foreground mode so we can access the interface
solr restart -f
