# Num guessing Game

#start
#user choose the lvl ->easy=6,inter=6 ==>1-15,1-50,diff=4==>1-100


import random


easy=random.randint(1,10)  
inter=random.randint(1,25)
diff=random.randint(1,100)

n=5

chances={
    "easy":{
	    "chance":n,
		"randomise":easy,
        "range":10
		},
	"inter":{
	    "chance":n,
		"randomise":inter,
        "range":25
		},
	"diff":{
	    "chance":n,
		"randomise":diff,
        "range":100
	     },
	}

result={
    "user":0,
}


user_choice = input("Choose difficulty level (easy/inter/diff): ").lower()



if user_choice not in chances:
    print("Invalid choice. Please choose 'easy', 'inter', or 'diff'.")
    exit()
else:
    option=chances[user_choice]
    target=option["randomise"]
    attempts=option["chance"]
    range=option["range"]

while attempts>0:
   try:
       guess=int(input("Enter a number between 1 and {}: ".format(range)))
       
    
   except ValueError:
         print("Invalid input! Please enter a number.")
         continue
   if guess==target:
           result["user"]+=1
           print("Congratulations! You guessed the number.")
           break
   elif guess<target:
           print("Too low. Try again.")
   else:
           print("Too high. Try again.")
   attempts-=1
   print(f"Attempts left: {attempts}")

if attempts == 0:
    print(f"Game over! The correct number was {target}.")

print(f"Your wins: {result['user']}")