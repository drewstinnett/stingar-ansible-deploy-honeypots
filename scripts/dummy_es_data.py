from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    'fluentd_host': '10.99.0.27',
    'sshd_port': 22,
    'cowrie': 'drews_funky_cow_moooo',
    'ip': '127.0.0.1',
    'host': 'Custom_cowrie_host',
    'tags': {
        'foo': 'bar',
        'purpose': 'testing',
        'porpose': 'dolphin'
    },
    'timestamp': datetime.now(),
}
index = "config"
res = es.index(index=index, doc_type='cowrie', id=1, body=doc)
es.indices.refresh(index=index)

res = es.search(index=index, body={"query": {"match_all": {}}})
for hit in res['hits']['hits']:
    print(hit)
