uniqueNumbersInWord = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fivteen',
    16:'sixteen',
    17:'seventeen',
    18:'eightteen',
    19:'ninteen',
    20:'twenty',
    30:'thrity',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninty',
    }

nword = uniqueNumbersInWord

def ntw(number):
    n = None
    if number in nword.keys():
        n= (nword[number])
        
    elif number < 99 and number % 10 == 0:
        n = (nword[number])
    elif number < 100 and number % 10 != 0:
        n = ' '.join([nword[(number//10)*10],nword[(number%10)],])
    elif 100 < number < 121:
        n = ' '.join([nword[number//100], 'hundred and', nword[number%100]])
    elif 120 < number < 1000:
        n = ' '.join([nword[number//100], 'hundred and ', ])
        n += ntw(number %100)
    elif 1000 < number < 1000000:
        n = ntw(number //1000) + " thousand"
        try:
            n+= ', '+ntw(number%1000)
        except:
            pass
    elif  1000000 < number < 1000000000:
        n = ntw(number //1000000) + " Million"
        try:
            n+= ', '+ntw(number%1000000)
        except:
            pass
    elif 1000000000 < number < 1000000000000:
        n = ntw(number //1000000000) + " Billion"
        try:
            n+= ', '+ntw(number%1000000000)
        except:
            pass
    return(n.strip())
