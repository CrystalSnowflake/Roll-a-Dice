import random

response = 'y'
response = input("Do you want to roll the dice? [y/n]")

while(response == 'y'):
    dice = random.randint(1,6)

    if(dice == 1):
        print("[-------]")
        print("[          ]")
        print("[    0    ]")
        print("[          ]")
        print("[-------]")
    if(dice == 2):
        print("[-------]")
        print("[        0]")
        print("[          ]")
        print("[0        ]")
        print("[-------]")
    if(dice == 3):
        print("[-------]")
        print("[        0]")
        print("[    0    ]")
        print("[0        ]")
        print("[-------]")
    if(dice == 4):
        print("[-------]")
        print("[0      0]")
        print("[          ]")
        print("[0      0]")
        print("[-------]")
    if(dice == 5):
        print("[-------]")
        print("[0      0]")
        print("[    0    ]")
        print("[0      0]")
        print("[-------]")
    if(dice == 6):
        print("[-------]")
        print("[0      0]")
        print("[0      0]")
        print("[0      0]")
        print("[-------]")
    
    response = input("Do you want to roll the dice? [y/n]")