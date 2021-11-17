x = 50
def test():
    global x
    print(f"x: {x}")
    x = 100
    print(f"x changed to: {x}")
test()
print(x)