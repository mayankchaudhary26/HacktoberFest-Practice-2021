pattern = "asbcklfdmegnot"
strg =  "eksge"
priority = list(pattern)
                
# Create a dictionary to store priority of each character
myDict = { priority[i] : i for i in range(len(priority))}
strg = list(strg)

# Pass lambda function as key in sort function
strg.sort( key = lambda ele : myDict[ele])
                
# Reverse the string using reverse()
strg.reverse()
                
new_str = ''.join(strg)
print(new_str)