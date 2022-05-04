import random
#create if statements to identify what should be the outcome for the specific speed.
speed_limit = random.randint(0,100)
police = f"I pull you over because you were on {speed_limit} miles per hour."
if speed_limit >= 70:
    print(f"{police}")
elif speed_limit >= 50:
    print(f"{police} ")
elif input("Anything you might want to tell me?"):
        input("What it is?")
        input("Okay you have a good day")
