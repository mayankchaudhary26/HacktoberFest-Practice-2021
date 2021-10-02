# Find if strings 'X' and 'Y' are Isomorphic or not
def isIsomorphic(X, Y):
 
    # if 'X' and 'Y' have different lengths, they cannot be isomorphic
    if len(X) != len(Y):
        return False
 
    # use a dictionary to store a mapping from characters of string 'X' to string 'Y'
    dict = {}
 
    # use set to store a pool of already mapped characters
    s = set()
 
    for i in range(len(X)):
        x = X[i]
        y = Y[i]
 
        # if `x` is seen before
        if x in dict:
            # return false if the first occurrence of `x` is mapped to a
            # different character
            if dict[x] != y:
                return False
 
        # if `x` is seen for the first time (i.e., it isn't mapped yet)
        else:
            # return false if `y` is already mapped to some other char in 'X'
            if y in s:
                return False
 
            # map `y` to `x` and mark it as mapped
            dict[x] = y
            s.add(y)
 
    return True
 
 
if __name__ == '__main__':
 
    X = "ACAB"
    Y = "XCXY"
 
    if isIsomorphic(X, Y):
        print(f"{X} and {Y} are Isomorphic")
    else:
        print(f"{X} and {Y} are not Isomorphic")
