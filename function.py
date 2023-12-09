###def calculator(x, y):
  ##return x * y 

##land = calculator(3,5)
##print(land)###


###///
####def calLand():
    ##width = float(input('Enter width: '))
    ##height = float(input('Enter height: '))
    ##result = width * height
    ##print('Result:', result)
###
###calLand()

def square(long, high, colour=9991):
    cal = long * high
    print(f"Area: {cal}, Colour: {colour}")

square(20, 15)

def triangle(base,high):
    cal = base * high * 0.5
    print(f"triangle: {cal}")

triangle(20,40)