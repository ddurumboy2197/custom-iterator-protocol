class MyRange:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            value = self.start
            self.start += self.step
            return value
        else:
            raise StopIteration
```

Kodni ishlatish uchun misol:
```python
for i in MyRange(1, 10, 2):
    print(i)
```

Bu kod 1 dan 10 gacha 2 ga teng bo'lgan sonlarni chiqaradi.
