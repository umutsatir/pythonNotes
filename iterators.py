## Iterators

liste = [1,2,3,4,5]

print(dir(liste)) # listler __iter__ metodu içerdiği için iterable objedir.
iterator = iter(liste)

print(next(iterator)) # 1 çıktısı alır.
print(next(iterator)) # 2 çıktısı alır.


# for döngüsünün arkaplanı
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break


# iterable class oluşturma
class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

list = MyNumbers(10,20)

for x in list: # MyNumbers iterable olduğu için for döngüsüne girebilir.
    print(x)
