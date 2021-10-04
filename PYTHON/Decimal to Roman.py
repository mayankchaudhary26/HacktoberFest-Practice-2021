def roman_iterative(num) :
    sr = ''
    while num > 0 :
        if num >= 1000 :
            sr += 'M'
            num -= 1000
        elif num >= 900 :
            sr += 'CM'
            num -= 900
        elif num >= 500 :
            sr += 'D'
            num -= 500
        elif num >= 400 :
            sr += 'CD'
            num -= 400
        elif num >= 100 :
            sr += 'C'
            num -= 100
        elif num >= 90 :
            sr += 'XC'
            num -= 90
        elif num >= 50 :
            sr += 'L'
            num -= 50
        elif num >= 40 :
            sr += 'XL'
            num -= 40
        elif num >= 10 :
            sr += 'X'
            num -= 10
        elif num >= 9 :
            sr += 'IX'
            num -= 9
        elif num >= 5 :
            sr += 'V'
            num -= 5
        elif num >= 4 :
            sr += 'IV'
            num -= 4
        elif num >= 1 :
            sr += 'I'
            num -= 1
    return sr

def roman_recursive(num,sr='') :
    if num == 0:
        return ''
    else:
        if num >= 1000 :
            sr = 'M'
            num -= 1000
        elif num >= 900 :
            sr = 'CM'
            num -= 900
        elif num >= 500 :
            sr = 'D'
            num -= 500
        elif num >= 400 :
            sr = 'CD'
            num -= 400
        elif num >= 100 :
            sr = 'C'
            num -= 100
        elif num >= 90 :
            sr = 'XC'
            num -= 90
        elif num >= 50 :
            sr = 'L'
            num -= 50
        elif num >= 40 :
            sr = 'XL'
            num -= 40
        elif num >= 10 :
            sr = 'X'
            num -= 10
        elif num >= 9 :
            sr = 'IX'
            num -= 9
        elif num >= 5 :
            sr = 'V'
            num -= 5
        elif num >= 4 :
            sr = 'IV'
            num -= 4
        elif num >= 1 :
            sr = 'I'
            num -= 1
    return sr + roman_recursive(num,sr)
if __name__ == '__main__':
	print(' *** Convert Decimal to Roman number ***')
	num = int(input('Enter Decimal number : '))
	#print("Roman number Iterative : ",roman_iterative(num),sep = '')
	print("Roman number Recursive : ",roman_recursive(num),sep = '')
	input('Press Enter to exit...')