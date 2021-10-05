# Author      : Charonyx, KMITL @ Thailand

# Title       : YIN YANG PATTERN

if __name__ == '__main__' :
    num = int(input('Enter Input : '))
    k   = num + 2
    if num > 0 :
        for i in range(-k, k + 1) :
            for j in range(-k, k + 1) :
                if not(i == 0 or j == 0) :
                    if abs(i + j) >= k + 2 : print('.', end='')
                    elif j < 0 and ((i < 0 and i + j <= 0) or abs(j) == k or abs(j) == 1 or abs(i) == 1 or abs(i) == 1 or abs(i) == k)  : print('#', end='')
                    elif j > 0 and ((i > 0 and i + j >= 0) or abs(j) == k or abs(j) == 1 or abs(i) == 1 or abs(i) == 1 or abs(i) == k)  : print('+', end='')
                    elif j < 0 : print('+', end='')
                    else : print('#', end='')
            if not(i == 0 or j == 0) : print('')

'''
# ----------------------- EXAMPLE ZONE -----------------------
# EX 1
Enter Input : 1
..#+++
.##+#+
###+++
###+++
#+#++.
###+..

# EX 2
Enter Input : 2
...#++++
..##+##+
.###+##+
####++++
####++++
#++#+++.
#++#++..
####+...

# EX 3
Enter Input : 3
....#+++++
...##+###+
..###+###+
.####+###+
#####+++++
#####+++++
#+++#++++.
#+++#+++..
#+++#++...
#####+....

# EX 4
Enter Input : 4
.....#++++++
....##+####+
...###+####+
..####+####+
.#####+####+
######++++++
######++++++
#++++#+++++.
#++++#++++..
#++++#+++...
#++++#++....
######+.....

'''