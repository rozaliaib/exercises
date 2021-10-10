class Counter:
    counter=0
    def start_from(self, counter=0):
        self.counter = counter

    def increment(self):
        self.counter = self.counter + 1#self.counter+=1

    def display(self):
        print('Текущее значение счетчика =', self.counter)

    def reset(self):
        self.counter=0

c1 = Counter()
c1.start_from()
c1.increment()
c1.display()#печатает "Текущее значение счетчика = 1"
c1.increment()
c1.display()
c1.reset()
c1.display()

