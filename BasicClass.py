class Theater:
  # Attribute
  theaterName = 'Victah Theater'


# constructor (__init__) เป็น 1 ใน Method ของ class
# Self keyword ที่แยกขอบเขต ระหว่าง class และ ค่า ของมัน

  def __init__(self, movieTiltle, ticketPrice):
    self.movieTiltle = movieTiltle
    self.ticketPrice = ticketPrice

  # Method
  def hello(self):
    print('welcome to the Theater')

#instance
#movie01 = Theater('DarkAvenger', 150)
#print(movie01.theaterName)
#print(movie01.movieTiltle)
#print(movie01.ticketPrice)
#movie01.hello()

#print('-------------------------------------')  #comment ทั้งหมด ctrl + ฝ
# movie02 = Theater('lightAvnger',500)
# print(movie02.movieTiltle)
# print(movie02.ticketPrice)
# print(movie02.theaterName)
# movie02.hello()

# การสือบทอด Class
class Customer(Theater) :
  def __init__(self, fullname, age ,movieTiltle, ticketPrice, seats):
    super().__init__(movieTiltle, ticketPrice)      #super คือ keywordสำหรับการสือบือด class จากTheater (Superclass)
    self.fullname = fullname
    self.age = age
    self.seats = seats
    self.money = 10000

  def buyTicket(self):
    # การคำนวนตั๋วหนัง
    self.total = self.ticketPrice * self.seats
    
    # หักเงินจากลูกค้า
    self.money -= self.total

    print(f'ชื่อลูกค้า : {self.fullname}')  # f = format string
    print(f'อายุ : {self.age}')
    print(f'เรื่อง : {self.movieTiltle}')
    print(f'ซื้อ : {self.seats} ที่นั่ง รวมเงิน {self.total}')
    print(f'เหลือเงิน : {self.money} บาท')

customer01 = Customer('Victah',20,'hungergame',250,2)
print(customer01.theaterName) #เพราะเป็นคลาสลูกที่สืบทอดมาเลยเรียก คลาส TheaterName
customer01.hello()
customer01.buyTicket()


customer02 = Customer('BEST',22,'hungergame2',500,12)
print(customer02.theaterName) #เพราะเป็นคลาสลูกที่สืบทอดมาเลยเรียก คลาส TheaterName
customer02.hello()
customer02.buyTicket()
