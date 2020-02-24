#Integer Examples

def intExample():
    x = 10
    print(x)
    x = 20
    print(x)

intExample()

#Float Examples

def floatExample():
    x = 10.0
    print(x)
    print(type(x)) 
    x = 20.0
    print(x)
    print(type(x)) 

floatExample()

#complex number example

def complexNumber():
    x = 3 + 2j
    print(type(x))

complexNumber()

#Swapping integers
def swapInt(x, y):
    temp = x
    x = y
    y = temp
    return (x,y)

print(swapInt(1,2))

#perform Arithmetic operation
def doArithmeticOperation(x, y, operator):
    switcher = {
        "+" :  x + y,
        "-" :  x - y,
        "*" :  x * y,
        "/" :  x / y,
        "%" :  x % y,
    }
    return switcher.get(operator, "undefined operator") 

print(doArithmeticOperation(10, 2, "/"))





