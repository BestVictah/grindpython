product = {'pencil':{'price':50,'colour': 'red' },
          'eraser':{'price':10,'colour': 'green'},
          'ruler':{'price':100,'colour': 'pink' }}

while True:
    print('---please select---')
    p = input('name: ')
    q = int(input('quanti: '))
    print('----')
    if p in product:
      print (f'item: {p} \nprice: {product[p]["price"]} \ncolour: {product[p]["colour"]}')
      print(f'quanti: {q}  \ntotal: {product[p]['price'] * q}')
    else: 
       print('item not found')
