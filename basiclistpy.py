## ตัวแปร = 9
## list = [] 
## dictionary = {}
## tuple = ()
## Set = {}
## function 
## class function (method)
### module 
### package 
cars = ['toyota','honda','benz']
cars.append('byd')
print(cars)
cars.remove('byd')
print(cars)
cars.insert(0,'tesla')
print(cars)
print(cars[1])
for c in cars:
  print(c)

for i,c in enumerate (cars, start=1):
  print('ลำกับที่ {} {}'.format(i,c))
cars[1] = 'isuzu'
print (cars)
del cars[1]
print(cars)

import turtle
tao = turtle.Pen()
tao.shape('turtle')
tao1 = {'color' : 'green','dis' : 100}
tao.color(tao1['color'])
def rect(tao_object,tdict) :
  for i in range(4):
    tao_object.forward(tdict['dis'])
    tao_object.left(90)

rect(tao,tao1) 

tao2 = turtle.Pen()
tao2dict = {'color' : 'red', 'dis' : 200}
tao2.color(tao2dict['color'])
rect(tao2,tao2dict)

