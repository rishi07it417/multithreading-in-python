from time import sleep

class Producer:
    def __init__(self,items):
        self.items = 10
        pass

    def refill(self):
        self.items = 10
        print("Producer: Stock refilled. Total items : ", self.items,end="\n")

    def run(self):
        while True:
            sleep(1)
            if (self.items <= 0):
                print("Producer: out of stock.",end="\n")
                break
            else:
                print("Producer: stock left : ", self.items,end="\n")


        print("*********Producer Task Completed*********")

    def sell(self):
        if self.items > 0:
            self.items -= 1
            print("Producer: Sold one item. Stock left : ", self.items,end="\n")
            return True
        else:
            print("Producer: No more items left in stock.",end="\n")
            return False

