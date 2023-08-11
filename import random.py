import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose = input('choose 0 for rock , 1 for paper and 2 for scissors'+' ')
computer_choice = random.randint(0,2)
if not choose.isdigit():
    print("You've entered an invalid value, try again and choose a number between 0-2.")
else :
  choose = int(choose)
  if choose >2 or choose <0:
    print ("You've entered an invalid value, try again and choose a number between 0-2.")
  elif choose ==0 or choose==1 or choose ==2:
    if choose ==0:
      print(f'you chose :rock{rock} ')
    if choose ==1:
      print(f'you chose: paper {paper}')
    if choose ==2:
      print (f'you chose :scissors {scissors}')  
    if computer_choice==0:
      print ('the computer chose rock') 
      if choose == 0:
       print ("its a draw")
      if choose == 1 :
       print ('you win')
      if choose == 2 :
       print ('hard luck!, try again.')
    elif computer_choice==1:
      print ('the computer chose paper') 
      if choose == 1:
       print ("its a draw")
      if choose == 2:
       print ('you win')
      if choose == 0:
       print ('hard luck!, try again.')  
    elif computer_choice==1:
      print ('the computer chose scissors') 
      if choose == 2:
       print ("its a draw")
      if choose == 0:
       print ('you win')
      if choose == 1:
       print ('hard luck!, try again.')  
    