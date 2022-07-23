def expo_calc(time=0):
    if time == 0:
        return "The time was taken as 0.\nYou are dead, congrats."
    elif time > 0:
        return (f"The distance is between a {time*343} meter radius.")
    else:
        return "You are dead."


def lit_calc(diff=0):
    if diff == 0:
        return "Youre in it, either watch or seek shelter"
    if diff > 0:
        return (f"You are {diff*343} meters from the storm. Good luck")
    else:
        return "Wut"


def main():
    print("Hi! Count the seconds btwn when you saw the light and the sound first. Or guess, no ones judging\n")
    print("What do you want to calculate?\n1. Explosion\n2. Lightning\n3. Quit")
    
    chois = int(input("\nPick the num: "))
    
    if chois == 1:
        explo_tim = float(input(
            "What was the time diffrence between the cloud and the kaboom? "))
        print(expo_calc(time=explo_tim))
    elif chois == 2:
        flash_thun_tim = float(
            input("What was the time btwn flash and thunder? "))
        print(lit_calc(diff=flash_thun_tim))
    elif chois == 3:
        print("Bye have a great time")
    else:
        print("Had to pick one of the options...")


if __name__ == "__main__":
    main()
