from time import sleep
from producer import Producer


def purchase(producer):
        isMoreItemsAvailable = producer.sell()
        return isMoreItemsAvailable


class Consumer:
    def __init__(self,producer):
        self.items = 0
        self.producer = producer

    def run(self):
        while True:
            sleep(1)
            isMoreItemsAvailable = purchase(self.producer)

            if isMoreItemsAvailable:
                self.items += 1
                print("Consumer: item purchased : ", self.items)
            else:
                print("Consumer: No more items available to purchase., try again later.")
                break


        print("Total itme purchased : ", self.items)
        print("*********Consumer Task Completed*********")


