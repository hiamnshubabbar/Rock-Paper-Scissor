import random
print(""" "Welcome to the Rock , Paper and Scissors game"
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

   _______
---'   ____)____
           ______)
       __________)
      (____)
---.__(___)
""")

rock = """ 
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""
scissor = """
   _______
---'   ____)____
           ______)
       __________)
      (____)
---.__(___)
"""

rps = [rock,paper,scissor]






your_choie = int(input("Please enter your choice: 1 for rock , 2 for paper and 3 for scissor: "))
computer_choice = random.randint(1,3)

if your_choie == 0 :
    print("enter a valid number")
elif your_choie >3:
    print("enter a valid number")
elif rps[your_choie-1] == rps[0] and rps[computer_choice-1] == rps[2]:
    print(f"you chose :\n{rps[your_choie-1]} \n computer chose :\n {rps[computer_choice-1]} ")
    print("you won")
elif rps[your_choie-1] == rps[1] and rps[computer_choice-1] == rps[0]:
    print(f"you chose :\n{rps[your_choie - 1]} \n computer chose :\n {rps[computer_choice - 1]} ")
    print("you won")
elif rps[your_choie-1] == rps[2] and rps[computer_choice-1] == rps[1]:
    print(f"you chose :\n{rps[your_choie - 1]} \n computer chose :\n {rps[computer_choice - 1]} ")
    print("you won")
elif rps[your_choie-1] == rps[computer_choice-1]:
    print(f"you chose :\n{rps[your_choie - 1]} \n computer chose :\n {rps[computer_choice - 1]} ")
    print("It's a tie.")
else:
    print(f"you chose :\n{rps[your_choie - 1]} \n computer chose :\n {rps[computer_choice - 1]} ")
    print("you loose")
