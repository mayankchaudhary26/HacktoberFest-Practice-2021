def countBits(n):
    return len("".join( b for b in bin(n)[2::] if b == '1'))

print(countBits(int(input())))
