def findDigitsCharsSymbols(inputString):
  charCount = 0
  digitCount = 0
  symbolCount = 0
  for char in inputString:
    if char.islower() or char.isupper():
      charCount+=1
    elif char.isnumeric():
      digitCount+=1
    else:
      symbolCount+=1
      
  print("Chars = ", charCount, "Digits = ", digitCount, "Symbol = ", symbolCount)
      
inputString = input("Enter a string\n")
print("total counts of chars, digits,and symbols \n")

findDigitsCharsSymbols(inputString)
