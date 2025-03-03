import json
import time

from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'kafka'})

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def read_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

data = read_json_file('sample-data.json')

time.sleep(30)

for d in data:
    p.poll(0)

    p.produce('test_pipeline', json.dumps(d).encode('utf-8'), callback=delivery_report)

p.flush()