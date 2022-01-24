# Create Iterator object
class MyGenType:
    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        if self.a <= 33:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration



iterable = iter(MyGenType())

# this will run the iterable 33 times and wont rise StopIteration
for x in iterable:
    print(x)

# this will rise StopIteration since it will turn "a" value to 34
try:
    next(iterable)
except StopIteration:
    print("Stop Iteration caught!")

