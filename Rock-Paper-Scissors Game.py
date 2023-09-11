import random
l=["rock", "paper","scissor"]
userName=str(input("please tell your name  "))
while True:
    UC=str(input('''
     GAME START..................................
    YES y
    NO|EXIT n
    
         '''))
    ccount=0
    ucount=0
    if UC=="y":
        print('''
              1 :rock
              2:scissor
              3: paper
              ''')
        for a in range (1,6):
            userinput=int(input())
            if userinput==1:
                uchoice="rock"
            elif userinput==2:
                uchoice="scissor"
            elif uchoice==3:
                uchoice=="paper"
            else:
                print("wrong choice")
                break
                
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer value",Cchoice)
                print("user Choice",uchoice)
                print("game Draw")
            elif (uchoice=="rock"and Cchoice=="scissor") or(uchoice=="paper"and Cchoice=="rock") or(uchoice=="scissor" and Cchoice=="paper") :
                print("Computer value",Cchoice)
                print("user Choice",uchoice)               
                print(userName,"wins")
                ucount=ucount+1
            elif(Cchoice=="rock"and uchoice=="scissor") or(Cchoice=="paper"and uchoice=="rock") or(Cchoice=="scissor" and uchoice=="paper") :
                print("Computer value",Cchoice)
                print("user Choice",uchoice)
                print("Compputer WINS")
                ccount=ccount+1   
        if ucount==ccount:
             print("game draw") 
             print(userName,ucount)
             print("computer",ccount) 
        elif ucount>ccount:
             print("finally:  ",userName,"wins") 
             print(userName,ucount)
             print("computer",ccount) 
        else:
            print("finallly computer wins") 
            print(userName,ucount)
            print("computer",ccount) 
            
    else:
        break
    
    
        
    
    
        




