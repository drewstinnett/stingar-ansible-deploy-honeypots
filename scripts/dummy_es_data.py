from datetime import datetime
from elasticsearch import Elasticsearch
import socket
from faker import Faker
es = Elasticsearch()
faker = Faker()


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


doc = {
    'fluentd_host': get_ip_address(),
    'sshd_port': 22,
    'cowrie': faker.hostname(),
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
