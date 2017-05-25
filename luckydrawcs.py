import csv, random, time, datetime

with open('BuildingBloCS.csv',newline="") as csvfile:
    file = csv.reader(csvfile,delimiter = ',')
    occupation = []
    name = []
    school = []
    signupdate = []#because of the first row
    chance = []
    realdate = []

    for row in file:
        occupation.append(row[5])
        name.append(row[2])
        school.append(row[3])
        date = row[0].split()[0]
        signupdate.append(date)
        
    chances = 1
    for i in range(1,len(signupdate)):
        month = int(signupdate[i].split("/")[0])
        day = int(signupdate[i].split("/")[1])
        year = int(signupdate[i].split("/")[2])
        curr = datetime.date(year,month,day)
        realdate.append(curr)
        print(realdate)
    for i in range (len(realdate)-1),1:
        if realdate[i+1]
        
    def luckydraw():
        winner = random.randint(1,len(name)-1)
        return name[winner], school[winner]

    def kindlewinner():#signups on pi day
        winner = random.randint(1,13)
        return name[winner], school[winner]
    
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
