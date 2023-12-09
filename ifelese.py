

def checkstyle(style, money):
    stylecheck = ['japanese', 'thai']
    if money >= 200 and style in stylecheck:
        print('come in')
    elif style not in stylecheck and money >= 300:
        print('buy some clothes')
    else:
        print('make some money')

checkstyle('french', 500)
    