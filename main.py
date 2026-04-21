from shlex import join

from consumer import Consumer
from producer import Producer
from time import sleep
from threading import Thread

producer = Producer(5)
consumer = Consumer(producer)

producer = Thread(target=producer.run)
producer.start()
sleep(1)

consumer = Thread(target=consumer.run)
consumer.start()


producer.join()
consumer.join()

print("*********Main Task Completed*********")
