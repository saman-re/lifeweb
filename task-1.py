import json
import time

from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'kafka'})

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

data = [
    {"id": "123", "full_name": "Ali", "timestamp": "2025/01/31 12:34:56", "active": "true"},
    {"id": "124", "full_name": " ", "timestamp": "2025-01-31T14:20:00Z", "active": "false",
     "extra_field": "i should be removed!"}
]

time.sleep(60)

for d in data:
    p.poll(0)

    p.produce('test_pipeline', json.dumps(d).encode('utf-8'), callback=delivery_report)

p.flush()