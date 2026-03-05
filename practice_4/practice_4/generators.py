# Example 1: iter() and next()
a = [1, 2, 3, 4, 5]
it = iter(a)

print(next(it))
print(next(it))


# Example 2: Custom iterator
class MyNumbers:
    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= 5:
            x = self.n
            self.n += 1
            return x
        else:
            raise StopIteration

obj = MyNumbers()
for x in obj:
    print(x)


# Example 3: Simple generator
def gen(n):
    for i in range(n):
        yield i

for x in gen(5):
    print(x)


# Example 4: Generator squares
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

for x in squares(1, 5):
    print(x)


# Example 5: Generator expression
g = (i * 2 for i in range(5))

for x in g:
    print(x)
