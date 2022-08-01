
def real_chk(diff):
    if (diff == 0):
        return "You got pranked"
    elif (diff > 0):
            return (f"Reality check, its not {diff} \nIts {diff*0.9313226} GB!")
    else:
        return "Wut"


def main():
    storag = int(input("How much storage do you have? "))
    print(real_chk(storag))

if __name__ == "__main__":
    main()