import time

print("Teminal $>")
while True:
    user=input("&> ")
    if user == "init install package":
        cancel=False
        n=0
        percent="[__________]"
        while n <= 100:
            print(f"\r{n}% installing {percent}\033[K", end="", flush=True)
            if n <= 10:
                percent="[#_________]"
            elif n <= 20:
                percent="[##________]"
            elif n <= 30:
                percent="[###_______]"
            elif n <= 40:
                percent="[####______]"
            elif n <= 50:
                percent="[#####_____]"
            elif n <= 60:
                percent="[######____]"
            elif n <= 70:
                percent="[#######___]"
            elif n <= 80:
                percent="[########__]"
            elif n <= 90:
                percent="[#########_]"
            else:
                percent="[##########]"
            n += 1
            time.sleep(0.5)
            if n == 30:
                time.sleep(1)
            elif n == 70:
                time.sleep(0.8)
            elif n == 85:
                print(f"{n}% installing {percent}")
                while True:
                    user=input("do you want to continue?[y/n]: ")
                    if user == "y":
                        time.sleep(0.5)
                        break
                    elif user == "n":
                        print("installation cancelled")
                        cancel=True
                        break
                    else:
                        print("No command detected")
                if cancel:
                    break
            elif n == 100:
                if not cancel:
                    print(f"{n}% installing {percent}")
                    print("Installation Complete")
                