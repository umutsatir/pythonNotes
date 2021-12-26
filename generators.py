## Generators

# Bellekte yer işgal etmeyen bir iterator üretir.

def cube():
    for i in range(5):
        yield i ** 3 # Bu değer bir kere üretilir, belleğe kaydolmaz. Bir daha kullanılamaz.

generator = cube()
print(next(generator)) # Generator iterable obje ürettiği için direk olarak next yapabiliriz.

for i in cube():
    print(i)


liste = [i**3 for i in range(5)] # bu normal bir liste üretir.
liste2 = (i**3 for i in range(5)) # bu generator objesi üretir. (normal parantez kullanılır)
