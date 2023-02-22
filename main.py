import pandas as pd
import random
import time
import csv

team_in_tournament = ["India", "Sri lanka", "England", "Australia", "West Indies", "South Africa", "Pakistan",
                      "Bangladesh"]
group_A = ["India", "England", "West indies","Bangladesh"]
group_B = ["Pakistan" , "Australia", "South Africa", "Sri Lanka"]

with open("India.csv","w",newline='') as india:   #creating team India's team profile
    indiawriter = csv.writer(india)
    indiawriter.writerow(["Name","Age","Player role"])
    indiawriter.writerow(["Virat Kohli(C)","30","Top order batter"])
    indiawriter.writerow(["Rohit Sharma","31","Open batter"])
    indiawriter.writerow(["KL Rahul","28","Open Batter"])
    indiawriter.writerow(["Hardik Pandya","28","Allrounder"])
    indiawriter.writerow(["Rishabh Pant(WK)","26","Wicketkeeper batter"])
    indiawriter.writerow(["Ravinder Jadeja","29","Allrounder"])
    indiawriter.writerow(["Ishan Kishan","26","Wicketkeeper batter"])
    indiawriter.writerow(["Shradul Thakur","28","Allrounder"])
    indiawriter.writerow(["Jasprit Bumrah","28","Bowler"])
    indiawriter.writerow(["Varun Chakravathy","28","Bowler"])
    indiawriter.writerow(["Mohamed Shami","32","Bowler"])
    india.close()
    reader2 = csv.reader(open("India.csv","r"))

with open("Sri lanka.csv","w",newline='') as sri_lanka:    #creating team sri lanka's team profile
    slwriter = csv.writer(sri_lanka)
    slwriter.writerow(["Name","Age","Player role"])
    slwriter.writerow(["Dasun Shanka(C)","28","Allrounder"])
    slwriter.writerow(["Kusal Perera(WK)","30","Wicketkeeper Batter"])
    slwriter.writerow(["Charith Asalanka","24","Top order batter"])
    slwriter.writerow(["Pathum Nissanka","26","Open batter"])
    slwriter.writerow(["Avishka Fernando","27","Batter"])
    slwriter.writerow(["Bhanuka Rajapaksa","29","Batter"])
    slwriter.writerow(["Wanindu Hasaranga","24","Allrounder"])
    slwriter.writerow(["Chamika Karunarathe","28","Allrounder"])
    slwriter.writerow(["Dushmantha Chameera","29","Bowler"])
    slwriter.writerow(["Lahiru Kumara","25","Bowler"])
    slwriter.writerow(["Maheesh Theekshana","23","Bowler"])
    sri_lanka.close()

    reader3 = csv.reader(open("Sri lanka.csv","r"))

with open("England.csv","w",newline='') as england:   #creating team England's team profile
    englandwriter = csv.writer(england)
    englandwriter.writerow(["Name","Age","Player role"])
    englandwriter.writerow(["Eoin Morgan(C)","29","Batter"])
    englandwriter.writerow(["Jos Buttler(WK)","29","Wicketkeeper Batter"])
    englandwriter.writerow(["Dawid Malan","27","Top order batter"])
    englandwriter.writerow(["Jonny Bairstow","27","Batter"])
    englandwriter.writerow(["Jason Roy","28","Open batter"])
    englandwriter.writerow(["Liam Livingstone","27","Allrounder"])
    englandwriter.writerow(["Moeen Ali","29","Allrounder"])
    englandwriter.writerow(["Adil Rashid","31","Bowler"])
    englandwriter.writerow(["Chris Woakes","28","Allrounder"])
    englandwriter.writerow(["Chris Jordan","28","Bowler"])
    england.close()

    reader4 = csv.reader(open("England.csv","r"))

with open("Australia.csv","w",newline='') as australia:   #cereating team Australia's team profile
    australiawriter = csv.writer(australia)
    australiawriter.writerow(["Name","Age","Player profile"])
    australiawriter.writerow(["Aaron Finch(C)","31","Open Batter"])
    australiawriter.writerow(["David Warner","31","Open Batter"])
    australiawriter.writerow(["Steve Smith","29","Top order batter"])
    australiawriter.writerow(["Glen Maxwell","28","Batter"])
    australiawriter.writerow(["Mathew Wade(WK)","31","Wicketkeeper batter"])
    australiawriter.writerow(["Marcus Stoinus","27","Batter"])
    australiawriter.writerow(["Mitchel Starc","29","Bowler"])
    australiawriter.writerow(["Josh Hazelwood","27","Bowler"])
    australiawriter.writerow(["Pat Cummins","29","Bowler"])
    australiawriter.writerow(["Adam Zampa","27","Bowler"])
    australia.close()

    reader5 = csv.reader(open("Australia.csv","r"))

with open("West indies.csv","w",newline='') as windies:   #creating team West indies team profile
    windieswriter = csv.writer(windies)
    windieswriter.writerow(["Name","Age","Player role"])
    windieswriter.writerow(["Kieron Pollard(C)","34","Allrounder"])
    windieswriter.writerow(["Chris Gayle","36","Open batter"])
    windieswriter.writerow(["Evin Lewis","28","Batter"])
    windieswriter.writerow(["Lendl Simmons","29","Batter"])
    windieswriter.writerow(["Nicholas Pooran(WK)","28","Wicketkeeper batter"])
    windieswriter.writerow(["Shimron Hetmayar","27","Batter"])
    windieswriter.writerow(["Andre Russel","31","Allrounder"])
    windieswriter.writerow(["Dwayne Bravo","32","Allrounder"])
    windieswriter.writerow(["Jason Holder","28","Allrounder"])
    windieswriter.writerow(["Ravi Rampaul","33","Bowler"])
    windieswriter.writerow(["Akeel Hossain","26","Bowler"])
    windies.close()

    reader6 = csv.reader(open("West indies.csv","r"))

with open("South Africa.csv","w",newline='') as safrica:  #creating team South Africa's team profile
    safricawriter = csv.writer(safrica)
    safricawriter.writerow(["Name","Age","Player role"])
    safricawriter.writerow(["Temba Bavuma(C)","29","Top order batter"])
    safricawriter.writerow(["Quinton De Kock(WK)","26","Wicketkeeper Batter"])
    safricawriter.writerow(["Reeza Hendricks","27","Batter"])
    safricawriter.writerow(["David Miller","29","Batter"])
    safricawriter.writerow(["Aiden Markram","28","Batter"])
    safricawriter.writerow(["Kagiso Rabada","27","Bowler"])
    safricawriter.writerow(["Bjorn Fotuin","27","Bowler"])
    safricawriter.writerow(["Anrich Notje","27","Bowler"])
    safricawriter.writerow(["Dwayne Pretorius","26","Bowler"])
    safricawriter.writerow(["Keshav Maharaj","31","Bowler"])
    safricawriter.writerow(["Tabraiz Shamsi","29","Bowler"])
    safrica.close()

    reader7 = csv.reader(open("South Africa.csv","r"))

with open("Pakistan.csv","w",newline='') as pakistan:   #creating team Pakistan's team profile
    pakistanwriter = csv.writer(pakistan)
    pakistanwriter.writerow(["Name","Age","Player role"])
    pakistanwriter.writerow(["Babar Azzam(C)","28","Open Batter"])
    pakistanwriter.writerow(["Mohamed Rizwan(WK)","28","Wicketkeeper Batter"])
    pakistanwriter.writerow(["Shoab Malik","33","Batter"])
    pakistanwriter.writerow(["Mohamed Hafeez","33","Batter"])
    pakistanwriter.writerow(["Fakhar Zaman","29","Batter"])
    pakistanwriter.writerow(["Asif Ali","32","Batter"])
    pakistanwriter.writerow(["Shaheen Shah Afrdi","24","Bowler"])
    pakistanwriter.writerow(["Imaad Wasim","28","Bowler"])
    pakistanwriter.writerow(["Hassan Ali","28","Bowler"])
    pakistanwriter.writerow(["Harris Rauf","28","Bowler"])
    pakistanwriter.writerow(["Shadab Khan","28","Bowler"])
    pakistan.close()

    reader8 = csv.reader(open("Pakistan.csv","r"))

with open("Bangladesh.csv","w",newline='') as bangladesh:    #creating team Bangladesh's team profile
    banglawriter = csv.writer(bangladesh)
    banglawriter.writerow(["Name","Age","Player role"])
    banglawriter.writerow(["Mahmadulla Riyaz(C)","31","Allrounder"])
    banglawriter.writerow(["Mushfiqur Rahim","31","Top order batter"])
    banglawriter.writerow(["Litton Das(WK)","28","Wicketkeeper batter"])
    banglawriter.writerow(["Mohammad Naim","25","Batter"])
    banglawriter.writerow(["Afif Hossain","26","Batter"])
    banglawriter.writerow(["Shakib al Hassan","31","Allrounder"])
    banglawriter.writerow(["Soumya Sarkar","29","Bowler"])
    banglawriter.writerow(["Shoriful Islam","27","Bowler"])
    banglawriter.writerow(["Taskin Ahamed","28","Bowler"])
    banglawriter.writerow(["Mustafizur Rahman","27","Bowler"])
    banglawriter.writerow(["Mehedi Hassan","25","Bowler"])
    bangladesh.close()

    reader9 = csv.reader(open("Bangladesh.csv","r"))

with open("Groups.csv","w",newline='') as groups: #creating a file to store the details of each group
    groupwriter = csv.writer(groups)
    groupwriter.writerow(["GROUP A","GROUP B"])
    groupwriter.writerow(["India","Pakistan"])
    groupwriter.writerow(["England","Australia"])
    groupwriter.writerow(["West Indies","South Africa"])
    groupwriter.writerow(["Bangladesh","Sri Lanka"])
    groups.close()

    reader10 = csv.reader(open("Groups.csv","r"))

with open("Group Fixtures.csv",'w', newline='') as fixtures: #creating a file to store the match fixtures
    fixturewriter = csv.writer(fixtures)
    fixturewriter.writerow(["Group Fixtures"])
    fixturewriter.writerow(["Match 1:","Sri lanka", "VS", "South Africa"])
    fixturewriter.writerow(["Match 2:","India", "VS", "West Indies"])
    fixturewriter.writerow(["Match 3:","Pakistan", "VS", "Australia"])
    fixturewriter.writerow(["Match 4:","England", "VS", "India"])
    fixturewriter.writerow(["Match 5:","Bangladesh", "VS", "West Indies"])
    fixturewriter.writerow(["Match 6:","Sri Lanka", "VS", "Pakistan"])
    fixturewriter.writerow(["Match 7:","England", "VS", "West Indies"])
    fixturewriter.writerow(["Match 8:","Australia", "VS", "Sri Lanka"])
    fixturewriter.writerow(["Match 9:","India", "VS", "Bangladesh"])
    fixturewriter.writerow(["Match 10:","Australia", "VS", "South Africa"])
    fixturewriter.writerow(["Match 11:","England", "VS", "Bangladesh"])
    fixturewriter.writerow(["Match 12:","Pakistan", "VS", "South Africa"])
    fixtures.close()

    reader11 = csv.reader(open("Group Fixtures.csv","r"))
df_india = pd.read_csv("India.csv")
df_sl = pd.read_csv("Sri lanka.csv")
df_pak = pd.read_csv("Pakistan.csv")
df_wi = pd.read_csv("West indies.csv")
df_ban = pd.read_csv("Bangladesh.csv")
df_aus = pd.read_csv("Australia.csv")
df_sa = pd.read_csv("South Africa.csv")
df_eng = pd.read_csv("England.csv")
df_teams = pd.read_csv("Team Details.csv")


print("--------------------------------------------------")
# starting the tournamnet
print("Welcome to the men's ICC T20 World Cup 2021")
print("")
print("You can edit only your team!")
print("If you wish to edit team details, Enter 1")
print("To continue, Enter 2")
print("--------------------------------------------------")
print("")
status = False
while not status:
    try:
        option = int(input("Enter your choice: "))
        if option == 1:                                         #user can edit his team details
            print("__________________________________")
            print("Enter 1 to edit team India")
            print("__________________________________")
            print("Enter 2 to edit team Sri lanka")
            print("__________________________________")
            print("Enter 3 to edit team England")
            print("__________________________________")
            print("Enter 4 to edit team Australia")
            print("__________________________________")
            print("Enter 5 to edit team West indies")
            print("__________________________________")
            print("Enter 6 to edit team South Africa")
            print("__________________________________")
            print("Enter 7 to edit team Pakistan")
            print("__________________________________")
            print("Enter 8 to edit team Bangladesh")
            print("__________________________________")
            detail = int(input("Enter the number the of your team that you wish to edit: ")) #the user can pick his team from the above list
            if detail == 1:     #user has chosen india as his team to edit
                print("")
                print("Team India!!")
                print("A small tip!")
                print("To edit a row completely,enter number of changes as 3")
                print("")
                number = int(input("Enter the number of changes you wish to make: "))
                counter = 1
                while counter <= number:
                    counter = counter + 1
                    df = pd.read_csv("India.csv")
                    print(df)
                    current_index = int(input("Enter index number: "))
                    to_change = input("Enter details you want to change in: ").capitalize()
                    replaced = input("Enter detail you want to replace with it: ").capitalize()
                    df.loc[current_index, to_change] = replaced
                    df.to_csv("India.csv", index=False)
                    print(df)
                    print("")
                status = True
            elif detail == 2: #user has chosen sri lanka as his team to edit
                print("")
                print("Team Sri lanka!!")
                time.sleep(0.2)
                print("A small tip!")
                print("To edit a row completely,enter number of changes as 3")
                print("")
                number = int(input("Enter the number of changes you wish to make: "))
                counter = 1
                while counter <= number:
                    counter = counter + 1
                    df = pd.read_csv("Sri lanka.csv")
                    print(df)
                    current_index = int(input("Enter index number: "))
                    to_change = input("Enter details you want to change in: ").capitalize()
                    replaced = input("Enter detail you want to replace with it: ").capitalize()
                    df.loc[current_index, to_change] = replaced
                    df.to_csv("Sri lanka.csv", index=False)
                    print(df)
                    print("")
                status = True
            elif detail == 3: #user has chosen england as his team to edit
                print("")
                print("Team England!!")
                time.sleep(0.2)
                print("A small tip!")
                print("To edit a row completely,enter number of changes as 3")
                print("")
                number = int(input("Enter the number of changes you wish to make: "))
                counter = 1
                while counter <= number:
                    counter = counter + 1
                    df = pd.read_csv("England.csv")
                    print(df)
                    current_index = int(input("Enter index number: "))
                    to_change = input("Enter details you want to change in: ").capitalize()
                    replaced = input("Enter detail you want to replace with it: ").capitalize()
                    df.loc[current_index, to_change] = replaced
                    df.to_csv("England.csv", index=False)
                    print(df)
                    print("")
                status = True
            elif detail == 4: #user has chosen australia as his team to edit
                print("")
                print("Team Australia!!")
                time.sleep(0.2)
                print("A small tip!")
                print("To edit a row completely,enter number of changes as 3")
                print("")
                number = int(input("Enter the number of changes you wish to make: "))
                counter = 1
                while counter <= number:
                    counter = counter + 1
                    df = pd.read_csv("Australia.csv")
                    print(df)
                    current_index = int(input("Enter index number: "))
                    to_change = input("Enter details you want to change in: ").capitalize()
                    replaced = input("Enter detail you want to replace with it: ").capitalize()
                    df.loc[current_index, to_change] = replaced
                    df.to_csv("Australia.csv", index=False)
                    print(df)
                    print("")
                status = True
            elif detail == 5: #user has chosen west indies as his team to edit
                print("")
                print("Team West indies!!")
                time.sleep(0.2)
                print("A small tip!")
                print("To edit a row completely,enter number of changes as 3")
                print("")
                number = int(input("Enter the number of changes you wish to make: "))
                counter = 1
                while counter <= number:
                    counter = counter + 1
                    df = pd.read_csv("West indies.csv")
                    print(df)
                    current_index = int(input("Enter index number: "))
                    to_change = input("Enter details you want to change in: ").capitalize()
                    replaced = input("Enter detail you want to replace with it: ").capitalize()
                    df.loc[current_index, to_change] = replaced
                    df.to_csv("West indies.csv", index=False)
                    print(df)
                    print("")
                    new_option1 = str(input("Do you wish to edit further? ")).capitalize()
                status = True
            elif detail == 6: #user has chosen south africa as his team to edit
                print("")
                print("Team South Africa!!")
                time.sleep(0.2)
                print("A small tip!")
                print("To edit a row completely,enter number of changes as 3")
                print("")
                number = int(input("Enter the number of changes you wish to make: "))
                counter = 1
                while counter <= number:
                    counter = counter + 1
                    df = pd.read_csv("South Africa.csv")
                    print(df)
                    current_index = int(input("Enter index number: "))
                    to_change = input("Enter details you want to change in: ").capitalize()
                    replaced = input("Enter detail you want to replace with it: ").capitalize()
                    df.loc[current_index, to_change] = replaced
                    df.to_csv("Sri lanka.csv", index=False)
                    print("")
                status = True
            elif detail == 7:   #user has chosen pakistan as his team to edit
                print("")
                print("Team Pakistan!!")
                time.sleep(0.2)
                print("A small tip!")
                print("To edit a row completely,enter number of changes as 3")
                print("")
                number = int(input("Enter the number of changes you wish to make: "))
                counter = 1
                while counter <= number:
                    counter = counter + 1
                    df = pd.read_csv("Pakistan.csv")
                    print(df)
                    current_index = int(input("Enter index number: "))
                    to_change = input("Enter details you want to change in: ").capitalize()
                    replaced = input("Enter detail you want to replace with it: ").capitalize()
                    df.loc[current_index, to_change] = replaced
                    df.to_csv("Pakistan.csv", index=False)
                    print(df)
                    print("")
                status = True
            elif detail == 8: #user has chosen bangladesh as his team to edit
                print("")
                print("Team Bangladesh!!")
                time.sleep(0.2)
                print("A small tip!")
                print("To edit a row completely,enter number of changes as 3")
                print("")
                number = int(input("Enter the number of changes you wish to make: "))
                counter = 1
                while counter <= number:
                    counter = counter + 1
                    df = pd.read_csv("Bangladesh.csv")
                    print(df)
                    current_index = int(input("Enter index number: "))
                    to_change = input("Enter details you want to change in: ").capitalize()
                    replaced = input("Enter detail you want to replace with it: ").capitalize()
                    df.loc[current_index, to_change] = replaced
                    df.to_csv("Bangladesh.csv", index=False)
                    print(df)
                    print("")
                status = True
            else:
                print("")
                print("Invalid entry!")
                print("")
                print("Try again!")
                print("")
                detail = input("Enter the number of the team to edit: ").capitalize()
                status = False
        elif option == 2:
            print("")
            print("This tournament consists of 1 round, with 8 teams battling for glory!")
            print("")
            print("The 8 teams have been seperated into 2 groups, Group A and Group B respectively")
            print("")
            print("--------------------------------------------------")
            status = True
        else:
            print("")
            print("Invalid option")
            print("")
            print("Enter 1 or 2")
            status = False
    except ValueError:
        print("you need to enter an integer!")
        status = False

print("")
print("To view groups, enter Yes")
print("")
status = False
while not status:
    try:
        new_option = str(input("Enter your choice: ")).capitalize()
        if new_option == "Yes":
            time.sleep(0.5)
            df = pd.read_csv("Groups.csv")
            print(df)
            print("")
            status = True
        else:
            print("Invalid option!")
            print("")
            print("Try again!!")
            print("To view groups, enter Yes")
            print("")
            status = False
    except ValueError:
        print("you need to enter a Yes!")
        status = False
print("")
print("To view fixtures, enter yes")
status = False
while not status:
    try:
        view_fixtures = str(input("Enter yes: ")).capitalize()
        if view_fixtures == "Yes":
            print("The following are the match fixtures in the tournament")
            print("")
            time.sleep(0.3)
            print("The Group fixtures are as follows.....")
            print("")
            df_group = pd.read_csv("Group Fixtures.csv")
            print(df_group)
            status = True
        else:
            print("")
            print("Invalid entry!!")
            print("Try again!")
            status = False
    except ValueError:
        print("you need to enter Yes!")
        status = False
print("")
print("---------------------------------------------------------")
print("Round 1 will begin ")
print("---------------------------------------------------------")
print("")
print("Group B matches will be played first")
print("")
status = False
while not status:
    try:
        option2 = str(input("Enter Yes to start group B matches: ")).capitalize()
        if option2 == "Yes":
            with open("Group B Match details.csv","w",newline='') as groupb:
                groupbwriter = csv.writer(groupb)
                groupbwriter.writerow(["Team 1","Team 2", "Winning team","Man of the match"])
                def tournament_game(match_team_1,match_team_2):
                    batting_1 = ""
                    batting_2 = ""
                    list1 = ["heads","tails"]
                    list3 = ["heads","tails"]
                    list2 = ["batting","bowling"]
                    print(match_team_1 + " ,is calling,heads or tails....")
                    head_tail = random.choice(list1)
                    comp_toss = random.choice(list3)
                    print(match_team_1,"has called ",head_tail,"!")
                    if head_tail == "heads" and comp_toss == "heads":
                        print("Heads!")
                        bat_bowl = random.choice(list2)
                        if bat_bowl == "batting" :
                            print(match_team_1 + " ,has chosen to bat first," + match_team_2 + " ,will be bowling")
                            batting_1 = match_team_1
                            batting_2 = match_team_2
                        else:
                            print(match_team_1 + " ,has chosen to bowl first," + match_team_2 + " ,will be batting")
                            batting_1 = match_team_2
                            batting_2 = match_team_1
                    elif head_tail == "tails" and comp_toss == "tails":
                        print("Tails!")
                        bat_bowl = random.choice(list2)
                        if bat_bowl == "batting" :
                            print(match_team_1 + " ,has chose to bat first, " + match_team_2 + " ,will be bowling ")
                            batting_1 = match_team_1
                            batting_2 = match_team_2
                        else:
                            print(match_team_1 + " ,has chose to bowl first, " + match_team_2 + " ,will be batting")
                            batting_1 = match_team_2
                            batting_2 = match_team_1
                    else:
                        print(match_team_2 + " ,have won the toss!")
                        bat_bowl = random.choice(list2)
                        if bat_bowl == "batting" :
                            print(match_team_2 + " ,has chosen to bat first," + match_team_1 + " ,will bowl")
                            batting_1 = match_team_2
                            batting_2 = match_team_1
                        elif bat_bowl == "bowling":
                            print(match_team_2 + ",has chosen to bowl first. " + match_team_1 + " ,will bat")
                            batting_1 = match_team_1
                            batting_2 = match_team_2

                    print("")
                    print("Here we go!")
                    print("")
                    possible_outcome = [0,1,2,3,4,6,-1,-2]  #-1 is to show wicket and -2 is to show wide
                    type_of_wicket = ["BOWLED","CAUGHT","LBW","STUMPED","RUN-OUT"]
                    score = 0
                    team_1_score = 0 #batting first team score
                    team_2_score = 0 #batting second team score
                    team_1_finished = 0 #variable creating to check if a team has already batted
                    next_batting_team = 0
                    batting_team = 1 #team batting first
                    wicket = 0
                    team_1_name = batting_1
                    team_2_name = batting_2
                    team_name = team_1_name
                    ball = ""
                    finalb = ""
                    for m in range(2):  # repeats for both team 1 and team 2
                        for y in range(20): # 20 over game
                            for x in range(6):# 6 balls per over
                                time.sleep(0.2)
                                if x == 0:
                                    ball = "1st ball"
                                elif x == 1:
                                    ball = "2nd ball"
                                elif x == 2:
                                    ball = "3rd ball"
                                elif x == 3:
                                    ball = "4th ball"
                                elif x == 4:
                                    ball = "5th ball"
                                elif x == 5:
                                    ball = "6th ball"
                                outcome = random.choice(possible_outcome)
                                if outcome == -2: #-2 is to indicate a wide ball
                                    while outcome == -2:
                                        print(ball,":","wide")
                                        score = score + 1
                                        if team_1_finished == 1: # to check if team1 has finished batting
                                            if team_1_score < score: # checking if team 2 has won the game by scoring more than team 1
                                                next_batting_team = 2
                                                break  # leaves this while loop
                                        outcome = random.choice(possible_outcome) #reballing
                                        if outcome == -1:
                                            print(ball, ":", "wicket", ":", random.choice(type_of_wicket))
                                            wicket = wicket + 1
                                            if wicket >= 10: # all wickets gone
                                                print("All Out!")
                                                print(y, ".", x, "overs")
                                                next_batting_team = 2
                                                break  # quit balls (exit from this for loop)
                                        elif outcome == -2:
                                            continue  # again enters the current loop
                                        else:
                                            print(ball,":",outcome)
                                            score = score + outcome
                                            break  #leaves the while loop
                                elif outcome == -1: #-1 indicates a wicket

                                    print(ball,":","wicket",":",random.choice(type_of_wicket))
                                    wicket = wicket + 1
                                    if wicket >= 10: # all wickets lost
                                        next_batting_team = 2
                                        print(y,".",x,"overs")
                                        break # leaves the loop for the 6 balls
                                else:
                                    print(ball,":",outcome)
                                    score = int(score) + int(outcome)
                                    if team_1_finished == 1:  # checking if team 1 finished batting
                                        if team_1_score < score:  # # checking if team 2 scored more than team 1 and won the match
                                            next_batting_team = 2 #used to quit from overs
                                            break

                            print("-----------------------------------------------") #a summary of each over
                            print(team_name,"details after",y+1,".",0,"overs")
                            print("score",": ",score,"runs")
                            print("Wickets gone: ",wicket)
                            print("------------------------------------------------")
                            if next_batting_team == 2:
                                wicket = 0
                                next_batting_team = 0
                                break #leaves the overs loop
                            else:
                                continue
                        if batting_team == 1:
                            print("************************************************")
                            print(team_1_name,"score is: ",score)
                            team_1_score = score
                            print("************************************************")
                            print(team_2_name, "target will be", team_1_score + 1)
                            print("************************************************")
                            score = 0
                            wicket = 0
                            batting_team = batting_team + 1
                            team_name = team_2_name
                            team_1_finished = 1
                        else:
                            print(team_2_name,"score is: ",score)
                            team_2_score = score
                            break  #quit from the m loop
                    print("==================================")
                    if team_1_score > team_2_score:
                        print(team_1_name,":",team_1_score)
                        print(team_2_name,":",team_2_score)
                        print(team_1_name, "won the match by",team_1_score-team_2_score,"runs")
                        if team_1_name == group_B[0]:
                            finalb = random.choice(df_pak["Name"])
                            print("Man of the match: ",finalb)
                        elif team_1_name == group_B[1]:
                            finalb = random.choice(df_aus["Name"])
                            print("Man of the match: ",finalb)
                        elif team_1_name == group_B[2]:
                            finalb = random.choice(df_sa["Name"])
                            print("Man of the match: ",finalb)
                        else:
                            finalb = random.choice(df_sl["Name"])
                            print("Man of the match: ",finalb)
                        groupbwriter.writerow([team_1_name,team_2_name,team_1_name,finalb])
                    elif team_1_score == team_2_score:
                        print(team_1_name, ":", team_1_score)
                        print(team_2_name, ":", team_2_score)
                        print("match is a draw")
                    else:
                        print(team_2_name, ":", team_2_score)
                        print(team_1_name, ":", team_1_score)
                        print(team_2_name,"won the match")
                        if team_2_name == group_B[0]:
                            finalb = random.choice(df_pak["Name"])
                            print("Man of the match: ",finalb)
                        elif team_2_name == group_B[1]:
                            finalb = random.choice(df_aus["Name"])
                            print("Man of the match: ",finalb)
                        elif team_2_name == group_B[2]:
                            finalb = random.choice(df_sa["Name"])
                            print("Man of the match: ",finalb)
                        else:
                            finalb = random.choice(df_sl["Name"])
                            print("Man of the match: ",finalb)
                        groupbwriter.writerow([team_1_name, team_2_name, team_2_name, finalb])
                    print("===================================")

                print("Match 1: ",group_B[3],"VS",group_B[2])
                print("")
                match_team_1 = group_B[3]
                match_team_2 = group_B[2]
                tournament_game(match_team_1, match_team_2)
                print("")

                print("Match 2: ",group_B[0],"VS",group_B[1])
                print("")
                match_team_1 = group_B[0]
                match_team_2 = group_B[1]
                tournament_game(match_team_1, match_team_2)
                print("")

                print("Match 3: ",group_B[3],"VS",group_B[0])
                print("")
                match_team_1 = group_B[3]
                match_team_2 = group_B[0]
                tournament_game(match_team_1,match_team_2)
                print("")

                print("Match 4: " , group_B[1] , "VS", group_B[3])
                print("")
                match_team_1 = group_B[1]
                match_team_2 = group_B[3]
                tournament_game(match_team_1,match_team_2)
                print("")

                print("Match 5: " , group_B[1] , "VS" , group_B[2])
                print("")
                match_team_1 = group_B[1]
                match_team_2 = group_B[2]
                tournament_game(match_team_1, match_team_2)
                print("")


                print("Match 6 : " , group_B[0] , "VS" , group_B[2])
                match_team_1 = group_B[0]
                match_team_2 = group_B[2]
                tournament_game(match_team_1, match_team_2)
                print("")
                groupb.close()
                reader13 = csv.reader(open("Group B Match details.csv","r"))
            df_gameB = pd.read_csv("Group B Match details.csv")
            print("////////////////////////////////////////////")
            print("Group B matches are over")
            print("////////////////////////////////////////////")
            print("")
            time.sleep(1)
            print("group B matches are over")
            print("")
            print("Here is group B summary")
            print("")
            print("---------------------------------------------------------------------------------------------------------------")
            print(df_gameB)
            print("---------------------------------------------------------------------------------------------------------------")
            print("")
            status = True
        else:
            print("")
            print("Try again")
            print("you need to enter Yes!")
            print("")
            status = False
    except ValueError:
        print("you need to enter Yes!")
        status = False
print("")
print("Next up are the group A matches")
status = False
while not status:
    try:
        option3 = str(input("Enter yes to start group A matches: ")).capitalize()
        if option3 == "Yes":
            with open("Group A Match details.csv","w",newline='') as groupa:
                groupawriter = csv.writer(groupa)
                groupawriter.writerow(["Team 1","Team 2", "Winning team","Man of the match"])
                def tournament_game(match_team_1,match_team_2):
                    batting_1 = ""
                    batting_2 = ""
                    list1 = ["heads","tails"]
                    list3 = ["heads","tails"]
                    list2 = ["batting","bowling"]
                    print(match_team_1 + " ,is calling,heads or tails....")
                    head_tail = random.choice(list1)
                    comp_toss = random.choice(list3)
                    print(match_team_1,"has called ",head_tail,"!")
                    if head_tail == "heads" and comp_toss == "heads":
                        print("Heads!")
                        bat_bowl = random.choice(list2)
                        if bat_bowl == "batting" :
                            print(match_team_1 + " ,has chosen to bat first," + match_team_2 + " ,will be bowling")
                            batting_1 = match_team_1
                            batting_2 = match_team_2
                        else:
                            print(match_team_1 + " ,has chosen to bowl first," + match_team_2 + " ,will be batting")
                            batting_1 = match_team_2
                            batting_2 = match_team_1
                    elif head_tail == "tails" and comp_toss == "tails":
                        print("Tails!")
                        bat_bowl = random.choice(list2)
                        if bat_bowl == "batting" :
                            print(match_team_1 + " ,has chose to bat first, " + match_team_2 + " ,will be bowling ")
                            batting_1 = match_team_1
                            batting_2 = match_team_2
                        else:
                            print(match_team_1 + " ,has chose to bowl first, " + match_team_2 + " ,will be batting")
                            batting_1 = match_team_2
                            batting_2 = match_team_1
                    else:
                        print(match_team_2 + " ,have won the toss!")
                        bat_bowl = random.choice(list2)
                        if bat_bowl == "batting" :
                            print(match_team_2 + " ,has chosen to bat first," + match_team_1 + " ,will bowl")
                            batting_1 = match_team_2
                            batting_2 = match_team_1
                        elif bat_bowl == "bowling":
                            print(match_team_2 + ",has chosen to bowl first. " + match_team_1 + " ,will bat")
                            batting_1 = match_team_1
                            batting_2 = match_team_2

                    print("")
                    print("Here we go!")
                    print("")
                    possible_outcome = [0,1,2,3,4,6,-1,-2]  #-1 is to show wicket and -2 is to show wide
                    type_of_wicket = ["BOWLED","CAUGHT","LBW","STUMPED","RUN-OUT"]
                    score = 0
                    team_1_score = 0
                    team_2_score = 0
                    team_1_finished = 0
                    next_batting_team = 0
                    batting_team = 1
                    wicket = 0
                    team_1_name = batting_1
                    team_2_name = batting_2
                    team_name = team_1_name
                    ball = ""
                    finala = ""
                    for m in range(2):  # repeats for both team 1 and team 2
                        for y in range(20): # 20 over game
                            for x in range(6):#6balls
                                time.sleep(0.2)
                                if x == 0:
                                    ball = "1st ball"
                                elif x == 1:
                                    ball = "2nd ball"
                                elif x == 2:
                                    ball = "3rd ball"
                                elif x == 3:
                                    ball = "4th ball"
                                elif x == 4:
                                    ball = "5th ball"
                                elif x == 5:
                                    ball = "6th ball"
                                outcome = random.choice(possible_outcome)
                                if outcome == -2: #-2 is to indicate a wide ball
                                    while outcome == -2:
                                        print(ball,":","wide")
                                        score = score + 1
                                        if team_1_finished == 1: # to check if team1 has finished batting
                                            if team_1_score < score: # checking if team 2 has won the game by scoring more than team 1
                                                next_batting_team = 2
                                                break  # leaves this while loop
                                        outcome = random.choice(possible_outcome) #reballing
                                        if outcome == -1:
                                            print(ball, ":", "wicket", ":", random.choice(type_of_wicket))
                                            wicket = wicket + 1
                                            if wicket >= 10: # all wickets gone
                                                print("All Out!")
                                                print(y, ".", x, "overs")
                                                next_batting_team = 2
                                                break  # quit balls (exit from this for loop)
                                        elif outcome == -2:
                                            continue  # again enters the current loop
                                        else:
                                            print(ball,":",outcome)
                                            score = score + outcome
                                            break  #leaves the while loop
                                elif outcome == -1: #-1 indicates a wicket

                                    print(ball,":","wicket",":",random.choice(type_of_wicket))
                                    wicket = wicket + 1
                                    if wicket >= 10: # all wickets lost
                                        next_batting_team = 2
                                        print(y,".",x,"overs")
                                        break # leaves the loop for the 6 balls
                                    elif next_batting_team == 2:
                                        break
                                else:
                                    print(ball,":",outcome)
                                    score = int(score) + int(outcome)
                                    if team_1_finished == 1:  # checking if team 1 finished batting
                                        if team_1_score < score:  # # checking if team 2 scored more than team 1 and won the match
                                            next_batting_team = 2 #used to quit from overs
                                            break

                            print("-----------------------------------------------") #a summary of each over
                            print(team_name,"details after",y+1,".",0,"overs")
                            print("score",": ",score,"runs")
                            print("Wickets gone: ",wicket)
                            print("------------------------------------------------")
                            if next_batting_team == 2:
                                wicket = 0
                                next_batting_team = 0
                                break #quit overs
                            else:
                                continue
                        if batting_team == 1:
                            print("************************************************")
                            print(team_1_name,"score is: ",score)
                            team_1_score = score
                            print("************************************************")
                            print(team_2_name, "target will be", team_1_score + 1)
                            print("************************************************")
                            score = 0
                            wicket = 0
                            batting_team = batting_team + 1
                            team_name = team_2_name
                            team_1_finished = 1
                        else:
                            print(team_2_name,"score is: ",score)
                            team_2_score = score
                            break  #quit from the m loop
                    print("==================================")
                    if team_1_score > team_2_score:
                        print(team_1_name,":",team_1_score)
                        print(team_2_name,":",team_2_score)
                        print(team_1_name, "won the match by",team_1_score-team_2_score,"runs")
                        if team_1_name == group_A[0]:
                            finala = random.choice(df_india["Name"])
                            print("Man of the match: ",finala)
                        elif team_1_name == group_A[1]:
                            finala = random.choice(df_eng["Name"])
                            print("Man of the match: ",finala)
                        elif team_1_name == group_A[2]:
                            finala = random.choice(df_wi["Name"])
                            print("Man of the match: ",finala)
                        elif team_1_name == group_A[3]:
                            finala = random.choice(df_ban["Name"])
                            print("Man of the match: ",finala)
                        groupawriter.writerow([team_1_name,team_2_name,team_1_name, finala])
                    elif team_1_score == team_2_score:
                        print(team_1_name, ":", team_1_score)
                        print(team_2_name, ":", team_2_score)
                        print("match is a draw")
                    else:
                        print(team_2_name, ":", team_2_score)
                        print(team_1_name, ":", team_1_score)
                        print(team_2_name,"won the match")
                        if team_2_name == group_A[0]:
                            finala = random.choice(df_india["Name"])
                            print("Man of the match: ",finala)
                        elif team_2_name == group_A[1]:
                            finala = random.choice(df_eng["Name"])
                            print("Man of the match: ",finala)
                        elif team_2_name == group_A[2]:
                            finala = random.choice(df_wi["Name"])
                            print("Man of the match: ",finala)
                        elif team_2_name == group_A[3]:
                            finala = random.choice(df_ban["Name"])
                            print("Man of the match: ",finala)
                        groupawriter.writerow([team_1_name, team_2_name, team_2_name, finala])
                    print("===================================")

                print("Match 2: ",group_A[0],"VS",group_A[2])
                print("")
                match_team_1 = group_A[0]
                match_team_2 = group_A[2]
                tournament_game(match_team_1, match_team_2)
                print("")

                print("Match 4: ",group_A[0],"VS",group_A[1])
                print("")
                match_team_1 = group_A[0]
                match_team_2 = group_A[1]
                tournament_game(match_team_1,match_team_2)
                print("")

                print("Match 5: ",group_A[3],"VS",group_A[2])
                print("")
                match_team_1 = group_A[3]
                match_team_2 = group_A[2]
                tournament_game(match_team_1,match_team_2)
                print("")

                print("Match 7: ",group_A[1],"VS",group_A[2])
                print("")
                match_team_1 = group_A[1]
                match_team_2 = group_A[2]
                tournament_game(match_team_1,match_team_2)
                print("")

                print("Match 9: ",group_A[0],"VS",group_A[3])
                print("")
                match_team_1 = group_A[0]
                match_team_2 = group_A[3]
                tournament_game(match_team_1,match_team_2)
                print("")

                print("Match 11: " , group_A[1] , "VS" , group_A[3])
                match_team_1 = group_A[1]
                match_team_2 = group_A[3]
                tournament_game(match_team_1, match_team_2)
                print("")
                groupa.close()
                reader19 = csv.reader(open("Group A Match details.csv","r"))
            df_gameA = pd.read_csv("Group A Match details.csv")
            print("////////////////////////////////////////////")
            print("group A matches are over")
            print("////////////////////////////////////////////")
            time.sleep(1)
            print("Here is the summary for group A matches")
            print("")
            print("---------------------------------------------------------------------------------------------------------------")
            print("Here is group A summary")
            print("")
            print(df_gameA)
            print("")
            status = True
        else:
            print("")
            print("you need to enter Yes!")
            status = False
    except ValueError:
        print("you need to enter Yes!")
        status = False

print("---------------------------------------------------------------------------------------------------------------")
print("")
print("---------------------------------------------------------------------------------------------------------------")
print("END OF ROUND 1")
print("All teams in each group have faced each other!")
print("---------------------------------------------------------------------------------------------------------------")
status = False
while not status:
    try:
        option4 = str(input("Enter Yes to view best performers in round 1: ")).capitalize()
        if option4 == "Yes":
            print("")
            print("From round 1 the top 5 wicket-takers are: ")
            print("")
            with open("Best bowlers.csv","w",newline='') as bowlers:
                bowlerwritter = csv.writer(bowlers)
                bowlerwritter.writerow(["Team name",'Player name',"Wickets taken"])
                for a in range(5):
                    bowlers_team = random.choice(team_in_tournament)
                    if bowlers_team == "India":
                        bowler_name = random.choice(df_india["Name"])
                        if bowler_name == "Rishabh Pant(WK)": #wicket keeper can not take wickets
                            while bowler_name == "Rishabh Pant(WK)":
                                bowler_name = random.choice(df_india["Name"])
                                bowlerwritter.writerow([bowlers_team,bowler_name,random.randint(8, 25)])
                                break
                        else:
                            bowlerwritter.writerow([bowlers_team,bowler_name,random.randint(8,25)])
                    elif bowlers_team == "England":
                        bowler_name = random.choice(df_eng["Name"])
                        if bowler_name == "Jos Buttler(WK)": #wicket keeper can not take wickets
                            while bowler_name == "Jos Buttler(WK)":
                                bowler_name = random.choice(df_eng["Name"])
                                bowlerwritter.writerow([bowlers_team,bowlers_team,bowler_name,random.randint(8, 25)])
                                break
                        else:
                            bowlerwritter.writerow([bowlers_team,bowler_name,random.randint(8, 25)])
                    elif bowlers_team == "Sri lanka":
                        bowler_name = random.choice(df_sl["Name"])
                        if bowler_name == "Kusal Perera(WK)": #wicket keeper can not take wickets
                            while bowler_name == "Kusal Perera(WK)":
                                bowler_name = random.choice(df_sl["Name"])
                                bowlerwritter.writerow([bowlers_team,bowler_name,random.randint(8, 25)])
                                break
                        else:
                            bowlerwritter.writerow([bowlers_team,bowler_name,random.randint(8, 25)])
                    elif bowlers_team == "Pakistan":
                        bowler_name = random.choice(df_pak["Name"])
                        if bowler_name == "Mohamed Rizwan(WK)": #wicket keeper can not take wickets
                            while bowler_name == "Mohamed Rizwan(WK)":
                                bowler_name = random.choice(df_pak["Name"])
                                bowlerwritter.writerow([bowlers_team,bowler_name, random.randint(8, 25)])
                                break
                        else:
                            bowlerwritter.writerow([bowlers_team,bowler_name,random.randint(8, 25)])
                    elif bowlers_team == "South Africa":
                        bowler_name = random.choice(df_sa["Name"])
                        if bowler_name == "Quinton De Kock(WK)": #wicket keeper can not take wickets
                            while bowler_name == "Quinton De Kock(WK)":
                                bowler_name = random.choice(df_sa["Name"])
                                bowlerwritter.writerow([bowlers_team,bowler_name,random.randint(8, 25)])
                                break
                        else:
                            bowlerwritter.writerow([bowlers_team,bowler_name,random.randint(8, 25)])
                    elif bowlers_team == "West indies":
                        bowler_name = random.choice(df_wi["Name"])
                        if bowler_name == "Nicholas Pooran(WK)": #wicket keeper can not take wickets
                            while bowler_name == "Nicholas Pooran(WK)":
                                bowler_name = random.choice(df_wi["Name"])
                                bowlerwritter.writerow([bowlers_team,bowler_name,random.randint(8, 25)])
                                break
                        else:
                            bowlerwritter.writerow([bowlers_team,bowler_name,random.randint(8, 25)])
                    elif bowlers_team == "Australia":
                        bowler_name = random.choice(df_aus["Name"])
                        if bowler_name == "Mathew Wade(WK)": #wicket keeper can not take wickets
                            while bowler_name == "Mathew Wade(WK)":
                                bowler_name = random.choice(df_aus["Name"])
                                bowlerwritter.writerow([bowlers_team,bowler_name,random.randint(8, 25)])
                                break
                        else:
                            bowlerwritter.writerow([bowlers_team,bowler_name,random.randint(8, 25)])
                    else:
                        bowler_name = random.choice(df_ban["Name"])
                        if bowler_name == "Litton Das(WK)": #wicket keeper can not take wickets
                            while bowler_name == "Litton Das(WK)":
                                bowler_name = random.choice(df_ban["Name"])
                                bowlerwritter.writerow([bowlers_team,bowler_name,random.randint(8, 25)])
                                break
                        else:
                            bowlerwritter.writerow([bowlers_team,bowler_name,random.randint(8, 25)])
                bowlers.close()

                reader12 = csv.reader(open("Best bowlers.csv","r"))
            df_bowler = pd.read_csv("Best bowlers.csv")
            df_sort_bowler = df_bowler.sort_values(by="Wickets taken", ascending = False) #sorting the wicket takers from highest to lowest
            print(df_sort_bowler)
            print("")
            print("---------------------------------------------------------------------------------------------------------------")
            print("From round 1 the top 5 highest run scorers are: ")
            print("")

            with open("Best batsmen.csv","w",newline='') as batters:
                batterwriter = csv.writer(batters)
                batterwriter.writerow(["Team name", "Player name", "Runs scored"])
                for b in range(5):
                    batters_team = random.choice(team_in_tournament)
                    if batters_team == "India":
                        batters_name = random.choice(df_india["Name"])
                        batterwriter.writerow([batters_team,batters_name,random.randint(120,350)])
                    elif batters_team == "England":
                        batters_name = random.choice(df_eng["Name"])
                        batterwriter.writerow([batters_team,batters_name,random.randint(120, 350)])
                    elif batters_team == "Sri lanka":
                        batters_name = random.choice(df_sl["Name"])
                        batterwriter.writerow([batters_team,batters_name,random.randint(120, 350)])
                    elif batters_team == "Pakistan":
                        batters_name = random.choice(df_pak["Name"])
                        batterwriter.writerow([batters_team,batters_name,random.randint(120, 350)])
                    elif batters_team == "South Africa":
                        batters_name = random.choice(df_sa["Name"])
                        batterwriter.writerow([batters_team,batters_name,random.randint(120, 350)])
                    elif batters_team == "West indies":
                        batters_name = random.choice(df_wi["Name"])
                        batterwriter.writerow([batters_team,batters_name,random.randint(120, 350)])
                    elif batters_team == "Australia":
                        batters_name = random.choice(df_aus["Name"])
                        batterwriter.writerow([batters_team,batters_name,random.randint(120, 350)])
                    elif batters_team == "Bangladesh":
                        batters_name = random.choice(df_ban["Name"])
                        batterwriter.writerow([batters_team,batters_name,random.randint(120, 350)])
                batters.close()

                reader13 = csv.reader(open("Best batsmen.csv","r"))
            df_batter = pd.read_csv("Best batsmen.csv")
            df_sort_batter = df_batter.sort_values(by="Runs scored", ascending=False) #sorting the top run scorers from most runs to least runs
            print(df_sort_batter)
            status = True
        else:
            print("")
            print("Invalid Entry!")
            print("Try again")
            print("")
            status = False
    except ValueError:
        print("you need to enter Yes!")
        status = False
print("")
print("**********************")
print("END OF ROUND 1!")
print("**********************")
