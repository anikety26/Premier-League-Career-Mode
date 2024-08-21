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
loan=0
prev_team='b'
ucl=["Real Madrid", "Barcelona", "Bayern Munich","Real Madrid", "Barcelona", "Bayern Munich", "Paris St. Germain", "Inter Milan", "Juventus", "Borrusia Dortmund", "Atletico Madrid", "AC Milan"]
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
        trophies.append(f"{year} Euros")
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
    clubteams=["Al Ahly","Waydad Casablanca","Monterrey","Leon","Pachuca","Seattle Sounders","Al-Hilal","Al Ain","Urawa Red Diamonds","Ulsan HD","Flamengo","Palmeiras","Fluminense","River Plate","Flamengo","Palmeiras","Fluminense","River Plate","Borussia Dortmund","Bayern Munich","Inter Milan","Juventus","Atletico Madrid","Real Madrid","Paris St. Germain","Borussia Dortmund","Bayern Munich","Inter Milan","Juventus","Atletico Madrid","Real Madrid","Paris St. Germain"]
    
    year=2023+season
    if year==2025:
        clubteams.append('Manchester City')
        clubteams.append('Chelsea')
        clubteams.append('Manchester City')
        clubteams.append('Chelsea')
        clubteams.append('Manchester City')
        clubteams.append('Chelsea')
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
teams = ['Arsenal', 'Aston Villa','Bournemouth', 'Brentford', 'Brighton & Hove Albion','Chelsea',
             'Crystal Palace', 'Everton','Fulham','Ipswich Town' ,'Leicester City','Liverpool', 'Manchester City', 'Manchester United',
             'Newcastle United','Nottingham Forest', 'Southampton', 'Tottenham Hotspur', 'West Ham United', 'Wolverhampton Wanderers']
startteams = ['Bournemouth', 'Brentford', 
             'Crystal Palace', 'Everton','Fulham','Ipswich Town', 'Leicester City', 'Nottingham Forest','Southampton',  'Wolverhampton Wanderers']
hometeam.extend(teams)
awayteam.extend(teams)
gameteam.extend(teams)
gameteam.extend(teams)
    
your=[]
stadiums = [  'Emirates Stadium',  'Villa Park','Vitality Stadium',  'Gtech Community Stadium','American Express Stadium', 'Stamford Bridge',  'Selhurst Park',
                  'Goodison Park','Craven Cottage','Portman Road Stadium','King Power Stadium', 'Anfield',  'Etihad Stadium',  'Old Trafford',
                  "St. James' Park",'City Ground',"St. Mary's Stadium",  'Tottenham Hotspur Stadium', 'London Stadium',  'Molineux Stadium']

relteams =['Luton Town', 'Burnley', 'Sheffield United', 'Leeds United','Watford']
relstartteams =['Luton Town', 'Burnley', 'Sheffield United', 'Leeds United','Watford']
relstadiums=['Kenilworth Road','Turf Moor','Bramall Lane','Elland Road','Vicarage Road']
fateams=[]
carabaoteams=[]
bigsix=["Chelsea","Liverpool","Manchester United","Manchester City","Arsenal","Tottenham Hotspur"]
good=["Chelsea","Liverpool","Manchester United","Manchester City","Arsenal","Tottenham Hotspur","Aston Villa","Newcastle United","Brighton & Hove Albion"]
print("Welcome to the Premier League Football Game!")
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

    computer_team_index=0
    options=[]
    options.extend(teams)
    if your_team in options:
        options.remove(your_team)
    if season>1:
        year=2023+season
        print(f"Date: June 1st, {year}")
        print("It is the summer transfer window")
        prev_team=your_team
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
        if your_team.title() in good:
            good.remove(your_team)
        if old in good:
            good.remove(old)
        if goals>=20:
            options=good
        if season>1 and goals>=15:
            while count<=tot:
                da=19-count
                opt=random.choice(good)
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
                print(f"{o}. Retire")
                offers.append(old)
                offers.append(your_team)
            elif a>=8 and b>=8 or goals<12:
                print(f"{m}. Go back to {old}")
                print(f"{n}. Retire")
                offers.append(old)
  
            elif 12<goals<18 or a>=7:
                print(f"{m}. Sign with {your_team}")
                print(f"{n}. Retire")
                offers.append(your_team)


               
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
                    print(" ")
                    print(f"You are now back at {your_team}")
                    print(" ")
                    break
                elif your_team.lower()=="sign" and loan==1:
                    your_team=dfd
                    print(" ")
                    print(f"You are signing with {your_team}")
                    print(" ")
                    break
                elif your_team.title() in offers:
                    your_team=your_team.title()
     
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
             a=random.randrange(1,10)
             if your_team in relteams or (a<=5 and goals<9 and points<42):
                if your_team in relteams:
                    print(f"{your_team} got relegated so you need to transfer")
                else:
                    print(f"{your_team} are forcing you out of the club so you need to transfer")
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
             elif loan==1 and your_team==dfd:
                print("")
                print(f"You are signing with {your_team}")
                print(" ")
           
             elif loan==1:
                print(" ")
                print(f"You now play for {your_team}")
                print(" ")
            
             print(" ")
    elif season>1:
            if 'Retire' in offers:
                offers.remove('Retire')
            if your_team in offers:
                your_team=your_team

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
                        
                        break
                    else:
                        print(" ")
                        print("Please choose one of the options")
                        print(" ")
                        continue
    count=0
    past=0
    numwin=0
    numloss=0
    numtie=0
    points=0
    goals=0
    assists=0
        
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
    if your_team==old or your_team==prev_team:
        a=2
    else: 
        career.append(your_team)
    if loan==1 and your_team==prev_team:
        career.append(your_team)
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
            if your_team=="Arsenal" or your_team=="Manchester City" or your_team=="Manchester United" or your_team=="Chelsea" or your_team=="Liverpool" or your_team=="Tottenham Hotspur":
                your_team_score=random.randint(0,7)
            if computer_team=="Arsenal" or computer_team=="Manchester City" or computer_team=="Manchester United" or computer_team=="Chelsea" or computer_team=="Liverpool" or computer_team=="Tottenham Hotspur":
                computer_team_score=random.randint(0,5)
            if your_team=="Brighton & Hove Albion" or your_team=="West Ham United" or your_team=="Aston Villa":
                your_team_socre=random.randint(0,5)
            if computer_team=="Brighton & Hove Albion" or computer_team=="West Ham United" or computer_team=="Aston Villa":
                computer_team_score=random.randint(0,4)
            if your_team=="Sheffield United" or your_team=="Leeds United" or your_team=="Southampton" or your_team=="Luton Town" or your_team=="Watford":
                your_team_socre=random.randint(0,3)
            if computer_team=="Sheffield United" or computer_team=="Leeds United" or computer_team=="Southampton" or computer_team=="Luton Town" or computer_team=="Watford":
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
                good=["Chelsea","Liverpool","Manchester United","Manchester City","Arsenal","Tottenham Hotspur","Aston Villa","Newcastle United","Brighton & Hove Albion"]
                if your_team.title() in good:
                    good.remove(your_team)
                if old in good:
                    good.remove(old)
                if goals>=20:
                    options=good
                
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
                    best=['Arsenal','Chelsea','Liverpool','Manchester United','Manchester City','Tottenham Hotspur']
                    worst=["Sheffield United","Leeds United","Southampton","Luton Town","Watford","Ipswich Town"]
                    rest= [ 'Aston Villa','Bournemouth', 'Brentford', 'Brighton & Hove Albion',
             'Crystal Palace', 'Everton','Fulham','Leicester City',
             'Newcastle United','Nottingham Forest', 'West Ham United', 'Wolverhampton Wanderers']
                    if your_team in best or your_team=="Arsenal" or your_team=="Manchester City" or your_team=="Manchester United" or your_team=="Chelsea" or your_team=="Liverpool" or your_team=="Tottenham Hotspur":
                         wins = random.randrange(9, 13)
                         x=15-wins
                         losses = random.randrange(1,  x)
                         draws = 19- wins - losses
                    
                    elif your_team in worst or your_team=="Sheffield United" or your_team=="Leeds United" or your_team=="Southampton" or your_team=="Luton Town" or your_team=="Watford":
                         wins = random.randrange(3, 5)
                         x=20-wins
                         losses = random.randrange(14, x)
                         draws = 19- wins - losses
                    elif your_team in rest:
                        wins = random.randrange(5, 10)
                        x=17-wins
                        losses = random.randrange(6,  x)
                        draws = 19- wins - losses
                    numwin=wins
                    numloss=losses
                    numtie=draws
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
                    uel=["Rangers","Celtic","Atalanta","Roma","Ajax","Bayer Leverkusen","Villarreal","Sporting CP","Olympiacos ","AEK Athens","Slavia Prague","Real Betis","Marseille","Rangers","Celtic","Atalanta","Roma","Ajax","Bayer Leverkusen","Villarreal","Marseille"]
                    uecl=["Lille","Club Brugge","Fenerbache","Genk","Fiorentina","Eintracht Frankfurt","Lille","Club Brugge","Fenerbache","Genk","Fiorentina","Eintracht Frankfurt","Dinamo Zagreb","Besiktas","Viktoria Plzen"]
                    


                    ucl=["Real Madrid", "Barcelona", "Bayern Munich","Real Madrid", "Barcelona", "Bayern Munich", "Paris St. Germain", "Inter Milan", "Juventus", "Borrusia Dortmund", "Atletico Madrid", "AC Milan"]
              fa=['Ipswich Town', 'Leicester City', 'Southampton', 'Leeds United','Watford','Arsenal', 'Aston Villa','Bournemouth', 'Brentford', 'Brighton & Hove Albion','Burnley','Chelsea',
             'Crystal Palace', 'Everton','Fulham', 'Liverpool','Luton Town', 'Manchester City', 'Manchester United',
             'Newcastle United','Nottingham Forest','Sheffield United', 'Tottenham Hotspur', 'West Ham United', 'Wolverhampton Wanderers','Arsenal', 'Aston Villa','Bournemouth', 'Brentford', 'Brighton & Hove Albion','Burnley','Chelsea',
             'Crystal Palace', 'Everton','Fulham', 'Liverpool','Luton Town', 'Manchester City', 'Manchester United',
             'Newcastle United','Nottingham Forest','Sheffield United', 'Tottenham Hotspur', 'West Ham United', 'Wolverhampton Wanderers',"Blackburn Rovers","Coventry City","Plymouth Argyle","Chelsea","Liverpool","Manchester United","Manchester City","Arsenal","Tottenham Hotspur",]
              carabao=["Blackburn Rovers","Coventry City","Middlesborough",'Ipswich Town', 'Leicester City', 'Southampton', 'Leeds United','Watford','Arsenal', 'Aston Villa','Bournemouth', 'Brentford', 'Brighton & Hove Albion','Burnley','Chelsea',
             'Crystal Palace', 'Everton','Fulham', 'Liverpool','Luton Town', 'Manchester City', 'Manchester United',
             'Newcastle United','Nottingham Forest','Sheffield United', 'Tottenham Hotspur', 'West Ham United', 'Wolverhampton Wanderers','Arsenal', 'Aston Villa','Bournemouth', 'Brentford', 'Brighton & Hove Albion','Burnley','Chelsea',
             'Crystal Palace', 'Everton','Fulham', 'Liverpool','Luton Town', 'Manchester City', 'Manchester United',
             'Newcastle United','Nottingham Forest','Sheffield United', 'Tottenham Hotspur', 'West Ham United', 'Wolverhampton Wanderers']
              fa.append(your_team)
              fa.append(your_team)
              carabao.append(your_team)
              carabao.append(your_team)
                
              

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
              carabao_winner=random.choice(carabao)
              print(" ")
              print("Final Standings:")
              print("-----------------")

              records = {}

              for team in teams:
                    best=['Arsenal','Chelsea','Liverpool','Manchester United','Manchester City','Tottenham Hotspur']
                    worst=["Sheffield United","Leeds United","Southampton","Luton Town","Watford","Ipswich Town"]
                    rest= [ 'Aston Villa','Bournemouth', 'Brentford', 'Brighton & Hove Albion',
             'Crystal Palace', 'Everton','Fulham','Leicester City',
             'Newcastle United','Nottingham Forest', 'West Ham United', 'Wolverhampton Wanderers']

                    c=count-1
                    if team in best or team=="Arsenal" or team=="Manchester City" or team=="Manchester United" or team=="Chelsea" or team=="Liverpool" or team=="Tottenham Hotspur":
                         wins = random.randrange(22, 28)
                         x=37-wins
                         losses = random.randrange(2,  x)
                         draws = 38- wins - losses
                         if old==team:
                             wins = random.randrange(9, 13)
                             x=15-wins
                             losses = random.randrange(1,  x)
                             draws = 19- wins - losses
                             wins=wins+oldwin
                             losses=losses+oldloss
                             draws=draws+oldtie
                             

                    
                    elif team in worst or team=="Sheffield United" or team=="Leeds United" or team=="Southampton" or team=="Luton Town" or team=="Watford":
                         wins = random.randrange(3, 6)
                         x=37-wins
                         losses = random.randrange(28,  x)
                         draws = 38- wins - losses
                         if old==team:
                             wins = random.randrange(1, 5)
                             x=20-wins
                             losses = random.randrange(14, x)
                             draws = 19- wins - losses
                             wins=wins+oldwin
                             losses=losses+oldloss
                             draws=draws+oldtie
                    elif team in rest:
                        wins = random.randrange(8, 19)
                        x=31-wins
                        losses = random.randrange(8,  x)
                        draws = 38- wins - losses
                        if old==team:
                             wins = random.randrange(3, 9)
                             x=17-wins
                             losses = random.randrange(7,  x)
                             draws = 19- wins - losses
                             wins=wins+oldwin
                             losses=losses+oldloss
                             draws=draws+oldtie
                    

                    
                        
                    point=3*wins+draws
                    r=random.randrange(1,30)


                    records[team] = (wins, draws, losses, point,r)
            
              ypoints=numwin*3+numtie
              r=random.randrange(1,30)
             

              records[your_team]=(numwin,numtie,numloss, ypoints,r)
             

              sorted_teams = sorted(records, key=lambda x: (records[x][3],records[x][4]), reverse=True)
              
              t=0
              ucl=["Real Madrid", "Barcelona", "Bayern Munich","Real Madrid", "Barcelona", "Bayern Munich", "Paris St. Germain", "Inter Milan", "Juventus", "Borrusia Dortmund", "Atletico Madrid", "AC Milan"]
              uel=["Rangers","Celtic","Atalanta","Roma","Ajax","Bayer Leverkusen","Villarreal","Sporting CP","Olympiacos ","AEK Athens","Slavia Prague","Real Betis","Marseille","Rangers","Celtic","Atalanta","Roma","Ajax","Bayer Leverkusen","Villarreal","Marseille"]
              uecl=["Lille","Club Brugge","Fenerbache","Genk","Fiorentina","Eintracht Frankfurt","Lille","Club Brugge","Fenerbache","Genk","Fiorentina","Eintracht Frankfurt","Dinamo Zagreb","Besiktas","Viktoria Plzen"]
              good=[]
              for team in sorted_teams:
                    t=t+1
                    print(f"{team}: {records[team][3]} points")
                    if t==5 or t==10 or t==15:
                        print(" ")
                    if t==1:
                        epl_winner=team
                        if season>1:
                            winners.append(team)
                    if t<=4:
                        ucl.append(team)
                        ucl.append(team)
                        good.append(team)
                    if t==5 or t==6:
                        uel.append(team)
                        uel.append(team)
                        uel.append(team)
                        good.append(team)
                    if t==7:
                        uecl.append(team)
                        uecl.append(team)
                        uecl.append(team)
                        good.append(team)
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
              print(" ")
              time.sleep(2)
              year=2023+season
              if your_team==epl_winner:
                  trophies.append(f"{year} Premier League")
                  print("Congratulations, you have won the Premier League!")             
              if your_team==fa_winner:
                  trophies.append(f"{year} FA Cup")
                  print("Congratulations, you have won the FA Cup!")
              if your_team==carabao_winner:
                  trophies.append(f"{year} Carabao Cup")
                  print("Congratulations, you have won the Carabao Cup!")
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
              print(f"Premier League Winner: {epl_winner}")
              print(f"FA Cup Winner: {fa_winner}")
              print(f"Carabao Cup Winner: {carabao_winner}")
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
                  goals=random.randint(16,30)
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
   
             
              
              
        
