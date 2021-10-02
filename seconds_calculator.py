import datetime



name = input('Enter name: ')
dayOfBirth = int(input('Enter day of birth: '))
monthOfBirth = int(input('Enter month of birth: '))
yearOfBirth = int(input('Enter year of birth: '))

todayDate = datetime.date.today()
dayOfBirth = datetime.date(yearOfBirth, monthOfBirth, dayOfBirth)

secondsLived = todayDate - dayOfBirth

print(name + ' you have lived for ' + str(secondsLived.total_seconds()) + ' seconds')