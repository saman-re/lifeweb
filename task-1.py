import json
from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost'})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

data = [
    {"id": "123", "full_name": "Ali", "timestamp": "2025/01/31 12:34:56", "active": "true"},
    {"id": "124", "full_name": " ", "timestamp": "2025-01-31T14:20:00Z", "active": "false",
     "extra_field": "i should be removed!"}
]

for d in data:
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)

    # Asynchronously produce a message. The delivery report callback will
    # be triggered from the call to poll() above, or flush() below, when the
    # message has been successfully delivered or failed permanently.
    p.produce('mytopic', json.dumps(d).encode('utf-8'), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()