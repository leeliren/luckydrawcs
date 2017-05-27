import csv, random, time, datetime

with open('BuildingBloCS.csv',newline="") as csvfile:
    file = csv.reader(csvfile,delimiter = ',')
    occupation = []
    name = []
    school = []
    signupdate = []#because of the first row
    realdate = []

    for row in file:
        occupation.append(row[5])
        name.append(row[2])
        school.append(row[3])
        date = row[0].split()[0]
        signupdate.append(date)
        
    for i in range(1,len(signupdate)):
        month = int(signupdate[i].split("/")[0])
        day = int(signupdate[i].split("/")[1])
        year = int(signupdate[i].split("/")[2])
        curr = datetime.date(year,month,day)
        realdate.append(curr)

    dictionary = dict(zip(name, school))
    realdate.reverse()
    name.reverse()
    namewchance = []
    curr = None
    count = 0

    for i in range(len(school)-1):
        if realdate[i] != curr:
            curr = realdate[i]
            count+=1
            for j in range (count):
                namewchance.append(name[i])
        else:
            for k in range(count):
                namewchance.append(name[i])

    def luckydraw():
        winner = random.randint(1,len(namewchance)-1)
        person = namewchance[winner]
        return person, dictionary[person]

    def kindlewinner():#signups on pi day
        winner = random.randint(-13,-1)
        return name[winner], dictionary[name[winner]]
    
    def display(prize):
        if prize == "luckydraw":
            print("Winner is ",end = "")
            a = luckydraw()
            winner = a[0]
            school = a[1]
        elif prize == "kindle":
            print("Kindle winner is ",end = "")
            b = kindlewinner()
            winner = b[0]
            school = b[1]
        for i in range (4): #for the suspense :)
            time.sleep(.5)
            print(".",end = "")
        print(winner,"from", school, "!!")

    display("luckydraw")

