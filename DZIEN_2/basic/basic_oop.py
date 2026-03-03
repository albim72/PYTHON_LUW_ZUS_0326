class Counter:

    def __init__(self,start=0):
        self.value = start

    # def __new__(cls, *args, **kwargs):
    #     print("Creating new instance of Counter")
    #     return super().__new__(Counter)

    def __repr__(self):
        return f"Counter({self.value})"

    def __call__(self, k):
        return (self.value + k)*10

    def increment(self):
        self.value += 1

    def show(self):
        return self.value

c  = Counter(10)
c.increment()
print(c.show())
print(c)
print(c(101))
