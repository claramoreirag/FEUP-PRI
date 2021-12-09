FROM solr:8.10

COPY fake_clean.json data/fake_clean.json

COPY schema.json /data/schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
