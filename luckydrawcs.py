import csv
import random
import time
with open('BuildingBloCS.csv',newline="") as csvfile:
    file = csv.reader(csvfile,delimiter = ',')
    occupation = []
    name = []
    school = []

    for row in file:
        occupation.append(row[5])
        name.append(row[2])
        school.append(row[3])

    def luckydraw():
        winner = random.randint(1,len(name)-1)
        if occupation[winner] == "Student":
            return name[winner], school[winner]
        elif occupation[winner] == "Teacher": #teachers cant win
            return luckydraw()

    def kindlewinner():#signups on pi day
        winner = random.randint(1,13)
        if occupation[winner] == "Student":
            return name[winner], school[winner]
        elif occupation[winner] == "Teacher": #teachers cant win
            return kindlewinner()
        
    def display(prize):
        if prize == "luckydraw":
            print("Winner is ",end = "")
            winner = luckydraw()[0]
            school = luckydraw()[1]
        elif prize == "kindle":
            print("Kindle winner is ",end = "")
            winner = kindlewinner()[0]
            school = kindlewinner()[1]
        for i in range (4): #for the suspense :)
            time.sleep(.5)
            print(".",end = "")
        print(winner,"from", school, "!!")

    display("kindle")
