#!/bin/bash

precreate-core news

# Start Solr in background mode so we can use the API to upload the schema
solr start

sleep 10

# Populate collection
bin/post -c news ./data/fake_clean.json

sleep 3

# Restart in foreground mode so we can access the interface
solr restart -f
