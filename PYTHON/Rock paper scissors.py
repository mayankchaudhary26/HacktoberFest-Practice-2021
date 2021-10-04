# Importing the necessary modules
import random 

#Declaring a pre-defined set of outcomes
outputs = ['rock','paper','scissor']

# Initialising scores of computer and user 
user = 0
computer = 0
name = input("Enter your name: ")

while True:
    try:
        n = int(input("Enter the number of rounds: "))
    except:
        print("\nInvalid input. Please input a number.")

# Playing for n rounds 
for i in range(1,n+1):
    temp1 = input("Enter rock, paper or scissor: ").strip().lower()
    while temp1 not in outputs:
        print("\nInvalid input. Please select from the options.")
        temp1 = input("Enter rock, paper or scissor: ").strip().lower()

    # Generating a choice for the computer using random library
    temp2 = random.choice(outputs)

    # If user choice and computer's choice is same, it's a tie
    if (temp1==temp2):
        print("Round "+str(i)+" is tied")
    
    # If user beats computer, increment user's score by 1
    elif ((temp1=='rock')and(temp2=='scissor'))or((temp1=='paper') and (temp2=='rock')) or ((temp1=='scissor')and(temp2=='paper')):
        user +=1
        print("Round "+str(i)+" is won by user")
    
    # If computer beats user, increment computer's score by 1
    elif ((temp2=='rock')and(temp1=='scissor'))or((temp2=='paper') and (temp1=='rock')) or ((temp2=='scissor')and(temp1=='paper')):
        computer += 1
        print("Round "+str(i)+" is won by computer")

# Display the results 
if user>computer:
    print("\n #### After "+str(n)+" rounds of play, "+name+" wins! #### \n")
elif computer>user:
    print("\n #### After "+str(n)+" rounds of play, Computer wins! #### \n")
else:
    print("\n #### After "+str(n)+" rounds of play, It's a tie! #### \n")


