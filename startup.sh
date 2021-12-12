#!/bin/bash

precreate-core news

# Start Solr in background mode so we can use the API to upload the schema
solr start

sleep 30

curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema.json \
    http://localhost:8983/solr/news/schema

# Populate collection
bin/post -c news ./data/fake_clean.json

sleep 5



# Restart in foreground mode so we can access the interface
solr restart -f