# Below is the multiply function implementation
def multiply(X):
    aux = 5*X
    return aux

def printHelloWorld(X):
    return print("Hello world", X)


def printHelloWorld1(X):
    return print(f"Hello world {X}")


def printHelloWorld2(X):
    return print("Hello world {}".format(X))



# And here is the function being called with an input parameter 70
a = multiply(70)
print(a)

printHelloWorld("elias")
printHelloWorld1("elias 1")
printHelloWorld2("elias 2")