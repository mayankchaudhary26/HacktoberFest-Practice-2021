def main():
    #getting input
    text=input('Enter the text string\n').upper()
    pattern=input('Enter the pattern to search\n').upper()
    shift_table = shiftTableConstruction(pattern)
    m=len(pattern)
    i=m-1
    n=len(text)
    while(i<=n-1):
        k=0
        while(k<=m-1 and pattern[m-1-k]==text[i-k]):
            k=k+1
        if(k==m):
            return i-m+1
        else:
            if (text[i] in shift_table.keys()):
                i=i+shift_table[text[i]]
            else:
                i=i+m
    return -1

def shiftTableConstruction(pattern):
    m=len(pattern)
    table={}
    for i in range(m-2,-1,-1):
        if(pattern[i] not in table):
            table[pattern[i]] = m-1-i
    return table            

main()
