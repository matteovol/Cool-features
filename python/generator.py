#!/usr/bin/env python3

class FirstN():

    def __init__(self, n):
        self.max = n
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            self.n += 1
            return self.n
        else:
            raise StopIteration()

def firstn(m):
    n = 0
    while n < m:
        yield n
        n += 1

def main():
    for i in FirstN(10):
        print(i)
    for i in FirstN(10):
        print(i)

if __name__ == "__main__":
    main()
