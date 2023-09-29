import time

floors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

currentF = floors[0]

while True:
    target = int(input(f"You're currently on Floor {currentF}. Where do you want to go?\n"
                       "[1] [2] [3] [4]\n"
                       "[5] [6] [7] [8]\n"
                       "[9] [10][11][12]\n"
                       "[13][14][15]\n"
                       "--> "))
    if target not in floors:
        print("!!!Invalid!!!\n"
              "Please choose between 1 to 15.")
        continue
    if 1 <= target <= 15:
        print("*ding*")
        time.sleep(1)
        print(f"|{currentF}|")
        time.sleep(1)
        while currentF != target:
            if currentF < target:
                currentF += 1
                print(f"|{currentF}|")
                time.sleep(1)
            elif currentF > target:
                currentF -= 1
                print(f"|{currentF}|")
                time.sleep(1)
        print("*ding*")
        time.sleep(1)
        print(f"You are now on your destination: Floor {currentF}")

    time.sleep(2)
    choice = input("Do you want to go to another floor? ").lower()

    if choice == "no":
        break
