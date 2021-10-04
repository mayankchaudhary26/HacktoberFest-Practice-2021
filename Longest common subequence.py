def lcs(a, b):
    ''' Finds longest common subsequence of arrays a, b. '''
    lengths = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    result = []
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            result.append(a[x-1])
            x, y = x - 1, y - 1
    return result[::-1]


#########################################################################








'''    Verification test    '''
if __name__ == "__main__":
    for a in [[-1,2,-3,4,-5,5], [-1,-2,-3], [], [0], [2, -2, 1, 2, -1, 3, -1, -1, -1]]:
        for b in [[-1,2,-3,4,-5,5], [-1,-2,-3], [], [0], [2, -2, 1, 2, -1, 3, -1, -1, -1]]:
            if a<=b:
                print('Longest common subsequence of:\n    {:s}\n    {:s}'.format(str(a), str(b)))
                print('is: {:s}\n'.format(str(lcs(a,b))))
