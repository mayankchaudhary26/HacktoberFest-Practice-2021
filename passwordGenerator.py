import random
from string import digits, punctuation, ascii_letters

symbols = digits + punctuation + ascii_letters

print ("="*20+"Strong Password Generator"+"="*20)

length = int(input('Password Length (Recommend : min 8) : '))

password = ''.join(random.sample(symbols, length))

print (password)