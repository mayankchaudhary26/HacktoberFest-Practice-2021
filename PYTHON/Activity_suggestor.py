import requests
import sys
from time import sleep

def getActivity(activityType):
    recieve  = requests.get(url='http://www.boredapi.com/api/activity?type='+activityType)
    # calling an api to get some acitvity
    data = recieve.json() #parsing the json file
    activity = data['activity'] #getting the activity name
    return activity

if __name__=="__main__":
    choices = ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]
    wmessage = "Getting bored?\nWan't some suggestions about something interesting?"
    for c in wmessage:
        sleep(0.1)
        sys.stdout.write(c)
        sys.stdout.flush()
    # used the above loop to get a typing effect
    sleep(0.5)
    print("\n\nChose a type of activity that might excite you:")
    i=1
    for choice in choices:
        print("\nEnter "+str(i)+" for "+choice)
        i+=1
        sleep(0.5)
    choiceNumber  = int(input("\nEnter your choice number: "))
    sleep(0.5)
    print("\nMay be you can try something like: \n")
    print(getActivity(choices[choiceNumber-1]))
