t=1
games={}
hometeam=[]
awayteam=[]
gameteam=[]
options=[]
import time
import random
import math

your_team='s'
past_team=0
home=0
away=0
t=0
career=[]
totgoal=[]
totassist=[]
trophies=[]
winners=[]
ucl=["Manchester City","Chelsea","Liverpool","Manchester City","Chelsea","Liverpool", "Bayern Munich","Arsenal","Manchester United","Tottenham Hotspur", "Bayern Munich", "Paris St. Germain", "Inter Milan", "Juventus", "Borrusia Dortmund", "AC Milan"]

def worldcup():
    worldcupteams=['Argentina','France','Spain','Brazil','Argentina','France','Spain','Brazil','England','Portugal','Uruguay','Germany','Germany','Netherlands','Belgium','Italy']
    
    worldcup_winner=random.choice(worldcupteams)
    if worldcup_winner==your_national:
        year=2023+season
        print(" ")
        trophies.append(f"{year} World Cup")
        print("Congratulations, you have won the World Cup!")
        print(" ")
    return worldcup_winner
def euro():
    euroteams=['England','Spain','France','Netherlands','Germany','Belgium','England','Spain','France','Netherlands','Germany','Belgium','Italy','Croatia','Denmark']
    euro_winner=random.choice(euroteams)
    if euro_winner==your_national:
        year=2023+season
        print(" ")
        trophies.append(f"{year} Premier League")
        print("Congratulations, you have won the Euros!")
        print(" ")
        
    return euro_winner
def copa():
    copateams=['Argentina','Brazil','Uruguay','Colombia','Argentina','Brazil','Uruguay','Colombia','Chile','Venezuela','Canada','Mexico','USA']
    copa_winner=random.choice(copateams)
    if copa_winner==your_national:
        year=2023+season
        print(" ")
        trophies.append(f"{year} Copa America")
        print("Congratulations, you have won the Copa America!")
        print(" ")
    return copa_winner

def clubworld(winners):
    clubteams=["Manchester City","Chelsea","Manchester City","Chelsea","Manchester City","Chelsea","Al Ahly","Waydad Casablanca","Monterrey","Leon","Pachuca","Seattle Sounders","Al-Hilal","Al Ain","Urawa Red Diamonds","Ulsan HD","Flamengo","Palmeiras","Fluminense","River Plate","Flamengo","Palmeiras","Fluminense","River Plate","Borussia Dortmund","Bayern Munich","Inter Milan","Juventus","Paris St. Germain","Borussia Dortmund","Bayern Munich","Inter Milan","Juventus","Paris St. Germain"]
    
    year=2023+season
    if year==2025:
        clubteams.append('Atletico Madrid')
        clubteams.append('Real Madrid')
        clubteams.append('Atletico Madrid')
        clubteams.append('Real Madrid')
        clubteams.append('Atletico Madrid')
        clubteams.append('Real Madrid')
    else:
        clubteams.append(winners)
        clubteams.append(winners)
        clubteams.append(winners)
    club_winner=random.choice(clubteams)
    winners=[]
    if club_winner==your_team:
        year=2023+season
        print(" ")
        trophies.append(f"{year} Club World Cup")
        print("Congratulations, you have won the Club World Cup!")
        print(" ")
    return club_winner
        

import math
num=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
teams = ["Alaves","Athletic Bilbao","Atletico Madrid","Barcelona","Celta Vigo","Espanyol","Getafe","Girona","Las Palmas",
         "Leganes","Mallorca","Osasuna","Rayo Vallecano","Real Betis","Real Madrid","Real Sociedad","Sevilla","Valencia","Valladolid","Villarreal"]
startteams = ["Alaves","Celta Vigo","Espanyol","Getafe","Las Palmas",
         "Leganes","Mallorca","Osasuna","Rayo Vallecano","Valladolid"]
hometeam.extend(teams)
awayteam.extend(teams)
gameteam.extend(teams)
gameteam.extend(teams)
    
your=[]
stadiums =["Mendizorrotza","San Mamés","Metropolitano","Camp Nou","Balaídos","Stage Front Stadium","Coliseum",
           "Montilivi","Gran Canaria","Butarque","Son Moix","El Sadar","Vallecas","Benito Villamarín","Santiago Bernabéu",
           "Anoeta","Ramón Sánchez-Pizjuán","Mestalla","José Zorrilla","La Cerámica"]

relteams =['Cadiz','Almeria','Granada','Elche','Levante']
relteamsorg =['Cadiz','Almeria','Granada','Elche','Levante']
relstadiums=['Nuevo Mirandilla','Power Horse Stadium','Nuevo Los Cármenes','Manuel Martínez Valero','Ciutat de València']
fateams=[]
carabao=[]
bigsix=["Athletic Bilbao","Atlético Madrid","Barcelona","Real Madrid","Real Sociedad","Sevilla"]
good=["Atletico Madrid","Barcelona","Real Madrid","Real Sociedad","Sevilla","Real Betis","Valencia"]
print("Welcome to the La Liga Football Game!")
old=0

                        


def chooseteam():
     numwin=0
     numloss=0
     numtie=0
     print("Choose a club to start with:")
     i=0
     for team in startteams:
            print(f"{i+1}. {team}")
            i=i+1
     while True:
         your_team = input()
         your_team=your_team.title()
         print(" ")
        
         if your_team in startteams:
            career.append(your_team)
            selected_team_index=teams.index(your_team)
            print(f"You have chosen {your_team}.")
            print(" ")
            break
         else:
            print("Please choose one of the options")
            continue
         
     
     return your_team
nationalstart=['Argentina','Brazil','France','Germany','Spain','Portugal']
def nationalchoose():
     print("Choose a national team:")
     national=['Argentina','USA','Germany','France','Spain','Urugauy','France','Netherlands','Belgium','Italy','Portugal','Denmark','Brazil','Colombia']
     can=1
     nationalstart=['Argentina','Brazil','England','France','Germany','Portugal']
     for a in nationalstart:
         print(f"{can}. {a}")
         can=can+1
     while True:
        your_national=input()
        your_national=your_national.title()

        if your_national in nationalstart:
            print(" ")
            print(f"You have chosen {your_national}")
            print(" ")
            break
        else:
            print(" ")
            print("Please choose one of the options")
            continue
     return your_national


        

your_team=chooseteam()
your_national=nationalchoose()


season=0
        
while True:
    season=season+1
    count=0
    past=0
    numwin=0
    numloss=0
    numtie=0
    points=0
    goals=0
    assists=0
    computer_team_index=0
    options=[]
    options.extend(teams)
    options.remove("Athletic Bilbao")
    if your_team in options:
        options.remove(your_team)
    if season>1:
        year=2023+season
        print(f"Date: June 1st, {year}")
        print("It is the summer transfer window")
        print(" ")
        if age>=35:
            print("You have retired.")
            print(" ")
            print("Career Overview:")
            print("\n".join(career))
            print(" ")
            print("Career Trophies:")
            print("\n".join(trophies))
            print(" ")
            print("Career Stats:")
            print(f"{sum(totgoal)} Goals")
            print(f"{sum(totassists)} Assists")
            time.sleep(1000)
            break
            
            
        print("You have offers from:")
        if loan==1:
            tot=random.randint(1,3)
        else:
            tot=random.randint(1,4)
        tot=tot+1
        count=1
        big=0
        offers=[]
        good=["Atlético Madrid","Barcelona","Real Madrid","Real Sociedad","Sevilla","Real Betis","Valencia"]
        if your_team.title() in good:
            good.remove(your_team)
        if old in good:
            good.remove(old)
        if season>1 and goals>=15:
            while count<=tot:
                da=19-count
                opn=random.randint(0,da)
                opt= good[opn]
                good.remove(opt)
                print(f"{count}. {opt}")
                offers.append(opt)
                count=count+1
        else:
            if old in options:
                options.remove(old)
            while count<=tot:
                da=19-count-5
                if da<=len(options):
                    opn=random.randint(0,da)
                else:
                    opn=random.randint(0,len(options)-1)
                opt= options[opn]
                options.remove(opt)
                print(f"{count}. {opt}")
                offers.append(opt)
                count=count+1
        if loan==1 and age<=31:
            m=tot+1
            n=tot+2
            a=random.randint(1,10)
            b=random.randint(1,10)
            if goals>18:
                print(f"{m}. Sign with {your_team}")
                print(f"{n}. Go back to {old}")
                offers.append(old)
                offers.append(your_team)
            elif a>=8 and b>=8 or goals<12:
                print(f"{m}. Go back to {old}")
                offers.append(old)
  
            elif 12<goals<18 or a>=7:
                print(f"{m}. Sign with {your_team}")
                offers.append(your_team)

            else:
                a=1
            
            dfd=your_team
        if age>31 and loan==0:
            n=tot+1
            print(f"{n}. Retire")
           
        if age>31 and loan==1:
            m=tot+1
            n=tot+2
            o=tot+3
            a=random.randint(1,10)
            b=random.randint(1,10)
            if goals>18:
                print(f"{m}. Sign with {your_team}")
                print(f"{n}. Go back to {old}")
                offers.append(old)
                offers.append(your_team)
            elif a>=8 and b>=8 or goals<12:
                print(f"{m}. Go back to {old}")
                offers.append(old)
  
            elif 12<goals<18 or a>=7:
                print(f"{m}. Sign with {your_team}")
                offers.append(your_team)
            else:
                a=1
                print(f"{m}. Retire")
            dfd=your_team
        if age>31:
            print("Do you want to move to any of these teams or retire? (Y/N)")
            y=input()
        elif loan==1:
            print(" ")
        else:
            print("Do you want to move to any of these teams? (Y/N)")
            y=input()
        if y.upper()=='Y' or y.upper()=='YES':
            while True:
                print("Which team do you want to go to?")
                your_team=input()
                your_team=your_team.title()
                if your_team.lower()=="go back" and loan==1:
                    your_team=old
                    career.append(your_team)
                    print(" ")
                    print(f"You are now back at {your_team}")
                    print(" ")
                    break
                elif your_team.lower()=="sign" and loan==1:
                    your_team=dfd
                    career.append(your_team)
                    print(" ")
                    print(f"You are signing with {your_team}")
                    print(" ")
                    break
                elif your_team.title() in offers:
                    your_team=your_team.title()
                    career.append(your_team)
                    print(" ")
                    print(f"You now play for {your_team}")
                    print(" ")
                    break
                elif your_team.lower()=="retire":
                    print("You have retired.")
                    print(" ")
                    print("Career Overview:")
                    print("\n".join(career))
                    print(" ")
                    print("Career Trophies:")
                    print("\n".join(trophies))
                    print(" ")
                    print("Career Stats:")
                    print(f"{sum(totgoal)} Goals")
                    print(f"{sum(totassists)} Assists")
                    time.sleep(1000)
                    break
                else:
                    print(" ")
                    print("Please choose one of the options")
                    print(" ")
                    continue
            
        
        else:
             print(" ")
             if your_team in relteams:
                print(f"{your_team} got relegated so you need to transfer")
                print(" ")
                while True:
                    print("Which team do you want to move to?")
                    your_team=input()
                    your_team=your_team.title()
                    if your_team.lower()=="retire":
                        print("You have retired.")
                        print(" ")
                        print("Career Overview:")
                        print("\n".join(career))
                        print(" ")
                        print("Career Trophies:")
                        print("\n".join(trophies))
                        print(" ")
                        goals=0
                        assists=0
                        for goal in totgoal:
                            goals=goals+goal
                        for assist in totassists:
                            assists=assists+assist
                        print("Career Stats:")
                        print(f"{goals} Goals")
                        print(f"{assists} Assists")
                        time.sleep(1000)
                        break
                    if your_team in offers:
                        
                        print(" ")
                        print(f"You now play for {your_team}")
                        print(" ")
                        career.append(your_team)
                        break
                    else:
                        print(" ")
                        print("Please choose one of the options")
                        print(" ")
                        continue
        
             if your_team.lower()=="retire":
                    print("You have retired.")
                    print(" ")
                    print("Career Overview:")
                    print("\n".join(career))
                    print(" ")
                    print("Career Trophies:")
                    print("\n".join(trophies))
                    print(" ")
                    print("Career Stats:")
                    print(f"{sum(totgoal)} Goals")
                    print(f"{sum(totassists)} Assists")
                    time.sleep(1000)
                    break
             if loan==1 and your_team==old:
                print(" ")
                print(f"You are now back at {your_team}")
                print(" ")
                career.append(your_team)
             elif loan==1 and your_team==dfd:
                print("")
                print(f"You are signing with {your_team}")
                print(" ")
                career.append(your_team)
             elif loan==1:
                print(" ")
                print(f"You now play for {your_team}")
                print(" ")
                career.append(your_team)
             print(" ")
    elif season>1:
            if 'Retire' in offers:
                offers.remove('Retire')
            if your_team in offers:
                your_team=your_team
                career.append(your_team)

            elif your_team in relteams:
                print(f"{your_team} got relegated so you need to transfer")
                while True:
                    print("Which team do you want to move to?")
                    your_team=input()
                    your_team=your_team.title()
                    if your_team.lower()=="retire":
                        print("You have retired.")
                        print(" ")
                        print("Career Overview:")
                        print("\n".join(career))
                        print(" ")
                        print("Career Trophies:")
                        print("\n".join(trophies))
                        print(" ")
                        goals=0
                        assists=0
                        for goal in totgoal:
                            goals=goals+goal
                        for assist in totassists:
                            assists=assists+assist
                        print("Career Stats:")
                        print(f"{goals} Goals")
                        print(f"{assists} Assists")
                        time.sleep(1000)
                        break
                    if your_team in offers:
                        
                        print(" ")
                        print(f"You now play for {your_team}")
                        print(" ")
                        career.append(your_team)
                        break
                    else:
                        print(" ")
                        print("Please choose one of the options")
                        print(" ")
                        continue
        
    hometeam=[]
    awayteam=[]
    gameteam=[]
    options=[]
    hometeam.extend(teams)
    awayteam.extend(teams)
    gameteam.extend(teams)
    gameteam.extend(teams)
    if your_team.title()=='Retire':
        print("You have retired.")
        print(" ")
        print("Career Overview:")
        print("\n".join(career))
        print(" ")
        print("Career Trophies:")
        print("\n".join(trophies))
        print(" ")
        print("Career Stats:")
        print(f"{sum(totgoal)} Goals")
        print(f"{sum(totassists)} Assists")
        time.sleep(1000)
        break
    

    selected_team_index=teams.index(your_team)
    count=0
    year=2023+season
    if year==2026 or year==2030 or year==2034 or year==2038 or year==2042 or year==2046 or year==2050:
        print(f"{year} World Cup Winner: {worldcup()}")
        time.sleep(1)
    if year==2028 or year==2032 or year==2036 or year==2040 or year==2044 or year==2048 or year==2052:
        print(f"{year} Euro Winner: {euro()}")
        print(f"{year} Copa America Winner: {copa()}")
        time.sleep(1)
    if year==2025 or year==2033 or year==2037 or year==2041 or year==2045 or year==2049 or year==2054:
        print(f"{year} Club World Cup Winner: {clubworld(winners)}")
        time.sleep(1)
    
    
    print(" ")
    print(f"Season {season}")
    age=20+season
    print(f"Age: {age}")
    print(f"Club: {your_team}")
    print(" ")
    loan=0
    print("Type 'Y' to begin season:")
    d=input()
    away=0
    home=0
    hometeam=[]
    awayteam=[]
    gameteam=[]
    hometeam.extend(teams)
    awayteam.extend(teams)
    gameteam.extend(teams)
    gameteam.extend(teams)
    
    gameteam.remove(your_team)
    gameteam.remove(your_team)
    hometeam.remove(your_team)
    awayteam.remove(your_team)
    half=[]

    while count<39:
            selcted_team_index=teams.index(your_team)
            your_stadium=stadiums[teams.index(your_team)]

           
            count=count+1
            while True:
                computer_team = random.choice(gameteam)
                if computer_team==your_team or computer_team in half:
                    continue
                else:
                    half.append(computer_team)
                    break
            computer_team_index=teams.index(computer_team)
            
            
          
 
            print(" ")
            val=random.randint(1,10)
            print("Week %s" % count)
            
            if val<6:
              if computer_team in awayteam:
                  print(f"{your_team} at {computer_team}")
                  stadium=stadiums[computer_team_index]
                  print("Venue: %s"%stadium)
                  awayteam.remove(computer_team)

              else:
                  print(f"{computer_team} at {your_team}")
                  print("Venue: %s"%your_stadium)
                  hometeam.remove(computer_team)
                 
                  
    
        
             
                  
            elif val>=6:
                if computer_team in hometeam:
                  print(f"{computer_team} at {your_team}")
                  print("Venue: %s"%your_stadium)

                  hometeam.remove(computer_team)

                else:
                  print(f"{your_team} at {computer_team}")
                  stadium=stadiums[computer_team_index]
                  print("Venue: %s"%stadium)
        
                  awayteam.remove(computer_team)
                 
                  
        
              
             
            print(" ")
            

            wh='sim'
            your_team_score=0
            gameteam.remove(computer_team)
            if your_team=="Athletic Bilbao" or your_team=="Atletico Madrid" or your_team=="Real Madrid" or your_team=="Sevilla" or your_team=="Girona" or your_team=="Real Sociedad":
                your_team_score=random.randint(0,7)
            if your_team=="Athletic Bilbao" or your_team=="Atletico Madrid" or your_team=="Real Madrid" or your_team=="Sevilla" or your_team=="Girona" or your_team=="Real Sociedad":
                your_team_score=random.randint(0,5)
            if your_team=="Real Betis" or your_team=="Valencia" or your_team=="Villarreal":
                your_team_socre=random.randint(0,5)
            if computer_team=="Real Betis" or computer_team=="Valencia" or computer_team=="Villarreal":
                computer_team_score=random.randint(0,4)
            if your_team=="Espanyol" or your_team=="Valladolid" or your_team=="Rayo Vallecano" or your_team in relteamsorg:
                your_team_socre=random.randint(0,3)
            if computer_team=="Espanyol" or computer_team=="Valladolid" or computer_team=="Rayo Vallecano" or computer_team in relteamsorg:
                computer_team_score=random.randint(0,3)
            else:
                your_team_score=random.randint(0,5)
                computer_team_score=random.randint(0,3)
              
            if your_team_score > computer_team_score:
                print(f"Congratulations! Your team won the game {your_team_score}-{computer_team_score}.")
                numwin=numwin+1
                points=points+3
            elif your_team_score < computer_team_score:
                print(f"Sorry, you lost the game {computer_team_score}-{your_team_score}.")
                numloss=numloss+1
                points=points+0
            else:
                print(f"The game ended in a draw {your_team_score}-{computer_team_score}.")
                numtie=numtie+1
                points=points+1
              
                

          
            
            print(" ")
            numwin=str(numwin)
            numloss=str(numloss)
            numtie=str(numtie)
            record=numwin+'-'+numtie+'-'+numloss
            print(f"Your record is %s and you have {points} points" % record)
            y='y'
            if y=='Y' or y=='y' or y=='yes':
              time.sleep(1)
            numwin=int(numwin)
            numloss=int(numloss)
            numtie=int(numtie)

            if count==19:
                options=[]
                options.extend(teams)
                options.remove("Athletic Bilbao")
                if your_team in options:
                    options.remove(your_team)
                print(" ")
                year=2024+season
                print(f"Date: January 1st, {year}")
                print("It is the january transfer window")    
                print(" ")
                print("You have offers from:")
                tot=random.randint(1,2)
                tot=tot+1
                count2=1
                offers=[]
                while count2<=tot:
                    da=19-count2-5
                    if da<=len(options):
                        opn=random.randint(0,da)
                    else:
                        opn=random.randint(0,len(options)-2)
                    opt= options[opn]
                    options.remove(opt)
                    loanteam='dnfnfnfnfnfskegjv'
                    a=random.randint(1,10)
                    if count2==tot and a>2:
                    
                        print(f"{count2}. {opt} (Loan)")
                        loanteam=opt
                    else:

                        print(f"{count2}. {opt}")
                        offers.append(opt)
                        
                    count2=count2+1
                    continue
                print("Do you want to move to any of these teams? (Y/N)")
                y=input()
        
                if y=='Y' or y=='y' or y=='yes' or y=='Yes':
                    old=your_team
                    oldwin=numwin
                    oldloss=numloss
                    oldtie=numtie
                    while True:
                        print("Which team do you want to move to?")
                        your_team=input()
                        your_team=your_team.title()
                        if your_team==loanteam:
                            loan=1
                            career.append(f"> {your_team}")
                            print(" ")
                            print(f"You are on loan at {your_team}")
                            break
                        elif your_team.title() in offers:
                            your_team=your_team.title()
                            career.append(your_team)
                            print(" ")
                            print(f"You now play for {your_team}")
                            break
        
                        elif your_team=="loan" or your_team=="Loan":
                            loan=1
                            career.append(f"> {your_team}")
                            print(" ")
                            print(f"You are on loan at {your_team}")
                            break
                        else:
                            loan=0
                            print(" ")
                            print("Please choose one of the options")
                            print(" ")
                            continue
                    selcted_team_index=teams.index(your_team)
                    if your_team=="Real Madrid" or your_team=="Barcelona":
                         wins = random.randrange(10, 14)
                         x=15-wins
                         losses = random.randrange(1,  x)
                         draws = 38- wins - losses
                    elif your_team=="Sevilla" or your_team=="Atletico Madrid" or your_team=="Athletic Bilbao" or your_team=="Girona":
                         wins = random.randrange(8, 12)
                         x=15-wins
                         losses = random.randrange(2,  x)
                         draws = 38- wins - losses
                    
                    elif your_team=="Espanyol" or your_team=="Valladolid" or your_team=="Rayo Vallecano" or your_team in relteamsorg:
                         wins = random.randrange(1, 5)
                         x=20-wins
                         losses = random.randrange(14,  x)
                         draws = 38- wins - losses
                    else:
                        wins = random.randrange(3, 9)
                        x=17-wins
                        losses = random.randrange(7,  x)
                        draws = 38- wins - losses
                    points=numwin*3+numtie
                    hometeam=[]
                    awayteam=[]
                    gameteam=[]
                    hometeam.extend(teams)
                    awayteam.extend(teams)
                    gameteam.extend(teams)
                    gameteam.extend(teams)
    
                    gameteam.remove(your_team)
                    gameteam.remove(your_team)
                    hometeam.remove(your_team)
                    awayteam.remove(your_team)
                
                time.sleep(1)
                half=[]
                

                    



                
            
              
            if count==38:
              if season==1:
                    totgoal=[]
                    totassists=[]
                    uel=["Rangers","Celtic","Atalanta","Roma","Ajax","Bayer Leverkusen","Aston Villa","Sporting CP","Olympiacos ","AEK Athens","Slavia Prague",
                   "Brighton & Hove Albion","Marseille","Rangers","Celtic","Atalanta","Roma","Ajax","Bayer Leverkusen","Aston Villa","Brighton & Hove Albion","Marseille"]
                    uecl=["Lille","Club Brugge","Fenerbache","Genk","Fiorentina","Eintracht Frankfurt","Lille","Club Brugge","Fenerbache","Genk","Fiorentina","Eintracht Frankfurt","Dinamo Zagreb","Besiktas","Viktoria Plzen"]
                    


                    
                    ucl=["Manchester City","Chelsea","Liverpool","Manchester City","Chelsea","Liverpool", "Bayern Munich","Arsenal","Manchester United","Tottenham Hotspur", "Bayern Munich", "Paris St. Germain", "Inter Milan", "Juventus", "Borrusia Dortmund", "AC Milan"]

              fa=["Alaves","Athletic Bilbao","Atletico Madrid","Barcelona","Celta Vigo","Espanyol","Getafe","Girona","Las Palmas",
         "Leganes","Mallorca","Osasuna","Rayo Vallecano","Real Betis","Real Madrid","Real Sociedad","Sevilla","Valencia","Valladolid","Villarreal","Alaves","Athletic Bilbao","Atletico Madrid","Barcelona","Celta Vigo","Espanyol","Getafe","Girona","Las Palmas",
         "Leganes","Mallorca","Osasuna","Rayo Vallecano","Real Betis","Real Madrid","Real Sociedad","Sevilla","Valencia","Valladolid","Villarreal",'Cadiz','Almeria','Granada','Elche','Levante']
              
              
              
              fa.append(your_team)
              fa.append(your_team)
              
                
              

              ucl_winner=random.choice(ucl)
              ucl.remove(ucl_winner)
              a=random.choice(ucl)
              ucl.remove(a)
              b=random.choice(ucl)
              ucl.remove(b)
              c=random.choice(ucl)
              uel.append(a)
              uel.append(b)
              uel.append(c)
              uel_winner=random.choice(uel)
              uecl_winner=random.choice(uecl)
              fa_winner=random.choice(fa)
              fa.remove(fa_winner)
              two=random.choice(fa)
              carabao.append(fa_winner)
              carabao.append(two)
              print(" ")
              print("Final Standings:")
              print("-----------------")

              records = {}

              for team in teams:
                    c=count-1
                    if team=="Real Madrid" or team=="Barcelona":
                         wins = random.randrange(22, 28)
                         x=37-wins
                         losses = random.randrange(2,  x)
                         draws = 38- wins - losses
                    elif team=="Sevilla" or team=="Atletico Madrid" or team=="Athletic Bilbao" or team=="Girona":
                         wins = random.randrange(16, 24)
                         x=37-wins
                         losses = random.randrange(6,  x)
                         draws = 38- wins - losses
                    
                    elif team=="Espanyol" or team=="Valladolid" or team=="Rayo Vallecano" or team in relteamsorg:
                         wins = random.randrange(3, 6)
                         x=37-wins
                         losses = random.randrange(28,  x)
                         draws = 38- wins - losses
                    else:
                        wins = random.randrange(4, 15)
                        x=31-wins
                        losses = random.randrange(13,  x)
                        draws = 38- wins - losses
                    

                    if old in teams and old==team:
                        wins = oldwin + random.randrange(3, 13)
                        x=20-numwin
                        losses = oldloss+random.randrange(3,  6)
                        draws = oldtie+19- numwin - numloss

                    point=3*wins+draws


                    records[team] = (wins, draws, losses, point)
            
              ypoints=numwin*3+numtie
             

              records[your_team]=(numwin,numtie,numloss, ypoints)
             

              sorted_teams = sorted(records, key=lambda x: records[x][3], reverse=True)
              t=0
              
              ucl=["Manchester City","Chelsea","Liverpool","Manchester City","Chelsea","Liverpool", "Bayern Munich","Arsenal","Manchester United","Tottenham Hotspur", "Bayern Munich", "Paris St. Germain", "Inter Milan", "Juventus", "Borrusia Dortmund", "AC Milan"]

              uel=["Rangers","Celtic","Atalanta","Roma","Ajax","Bayer Leverkusen","Aston Villa","Sporting CP","Olympiacos ","AEK Athens","Slavia Prague",
                   "Brighton & Hove Albion","Marseille","Rangers","Celtic","Atalanta","Roma","Ajax","Bayer Leverkusen","Aston Villa","Brighton & Hove Albion","Marseille"]
              uecl=["Lille","Club Brugge","Fenerbache","Genk","Fiorentina","Eintracht Frankfurt","Lille","Club Brugge","Fenerbache","Genk","Fiorentina",
                    "Eintracht Frankfurt","Dinamo Zagreb","Besiktas","Viktoria Plzen"]
                    
              for team in sorted_teams:
                    t=t+1
                    print(f"{team}: {records[team][3]} points")
                    if t==5 or t==10 or t==15:
                        print(" ")
                    if t==1:
                        epl_winner=team
                        if season>1:
                            winners.append(team)
                        carabao.append(team)
                    if t==2:
                        carabao.append(team)
                    if t<=4:
                        ucl.append(team)
                        ucl.append(team)
                    if t==5 or t==6:
                        uel.append(team)
                        uel.append(team)
                        uel.append(team)
                    if t==7:
                        uecl.append(team)
                        uecl.append(team)
                        uecl.append(team)
                    if t>=18:
                        f=teams.index(team)
                        relteams.append(team)
                        relstadiums.append(stadiums[f])
                        teams.remove(team)
                        stadiums.remove(stadiums[f])
                        teams.append(relteams[0])
                        stadiums.append(relstadiums[0])
                        relteams.remove(relteams[0])
                        relstadiums.remove(relstadiums[0])
              carabao_winner=random.choice(carabao)
              print(" ")
              time.sleep(2)
              year=2023+season
              if your_team==epl_winner:
                  trophies.append(f"{year} La Liga")
                  print("Congratulations, you have won the La Liga!")             
              if your_team==fa_winner:
                  trophies.append(f"{year} Copa del Rey")
                  print("Congratulations, you have won the Copa del Rey!")
              if your_team==carabao_winner:
                  trophies.append(f"{year} Supercopa de España")
                  print("Congratulations, you have won the Supercopa de España!")
              if your_team==ucl_winner:
                  trophies.append(f"{year} Champions League")
                  print("Congratulations, you have won the Champions League!")
                  
              if your_team==uel_winner:
                  trophies.append(f"{year} Europa League")
                  print("Congratulations, you have won the Europa League!")

              if your_team==uecl_winner:
                  trophies.append(f"{year} Conference League")
                  print("Congratulations, you have won the Conference League!")
              
              time.sleep(2)
              print(" ")
              print(f"La Liga Winner: {epl_winner}")
              print(f"Copa del Rey Winner: {fa_winner}")
              print(f"Supercopa de España Winner: {carabao_winner}")
              print(" ")
              print(f"UCL Winner: {ucl_winner}")
              print(f"Europa League Winner: {uel_winner}")
              print(f"Conference League Winner: {uecl_winner}")
              print(" ")
              
              

              time.sleep(2)
              print("Season Stats:")
              goals=0
              assist=0
              if numwin>=16:
                  goals=random.randint(16,31)
                  assist=random.randint(9,18)
                  totgoal.append(goals)
                  totassists.append(assist)
              elif 7<numwin<16:
                  goals=random.randint(8,15)
                  assist=random.randint(4,9)
                  totgoal.append(goals)
                  totassists.append(assist)
              else:
                  goals=random.randint(3,8)
                  assist=random.randint(2,6)
                  totgoal.append(goals)
                  totassists.append(assist)
              print(f"{goals} Goals")
              print(f"{assist} Assists")
              time.sleep(2)

              break
            
              
            else:
                print(" ")
                continue
   
             
     
            break
          
            

       
            
        
    print(" ")
   
             
              
              
        
