import time
import webbrowser

print("Terminal $>")

while True:
    user = input("&> ")

    if user == "init install package":
        cancel = False
        n = 0
        percent = "[__________]"
        print("Checking package")
        time.sleep(3)
        print("Initiating install package")
        time.sleep(3)
        print("Checking package installed")
        time.sleep(3)

        while n <= 100:
            # Update the progress bar first
            if n == 0:
                percent = "[__________]"
            elif n <= 10:
                percent = "[#_________]"
            elif n <= 20:
                percent = "[##________]"
            elif n <= 30:
                percent = "[###_______]"
            elif n <= 40:
                percent = "[####______]"
            elif n <= 50:
                percent = "[#####_____]"
            elif n <= 60:
                percent = "[######____]"
            elif n <= 70:
                percent = "[#######___]"
            elif n <= 80:
                percent = "[########__]"
            elif n <= 90:
                percent = "[#########_]"
            else:
                percent = "[##########]"

            # Display percentage and bar together
            print(
                f"\r{n}% installing {percent}\033[K",
                end="",
                flush=True
            )

            time.sleep(0.05)

            if n == 30:
                time.sleep(1)
            elif n == 70:
                time.sleep(0.8)

            # Ask for confirmation at 85%
            if n == 85:
                print()
                while True:
                    user = input(
                        "Do you want to continue? [y/n]: "
                    ).strip().lower()

                    if user == "y":
                        break
                    elif user == "n":
                        print("Installation cancelled.")
                        cancel = True
                        break
                    else:
                        print("No command detected.")

                if cancel:
                    break

            n += 1

        # Finish the progress line cleanly
        print()

        if not cancel:
            print("Installation Complete!\n")

    elif user == "about":
        print("This program is created because of curiosness and fun, there is no installation process here, it's all just a simulation:).\n")
    elif user == "commands":
        print("init install package ~ initiating an installing simulation event in a terminal\nhelp ~ providing details where to find help to this program\n")
    elif user == "help":
        print("go to this website:https://github.com/j34rom/Terminal-simulation-game/blob/main/terminal%20version%201.py\n")
    elif user == "opn prn":
        print("seach it for your self jerk")
        time.sleep(1)
        print("do yourself a favor")
        time.sleep(1)
        print("wait a moment")
        time.sleep(1)
        print("just wait a moment ok?")
        time.sleep(1)
        print("wait a moment we are figuring something")
        time.sleep(3)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print(1)
        time.sleep(1)
        print("voilaaaaaaaaaa!!!!!!!!!!!!!!!")
        time.sleep(0.5)
        webbrowser.open("https://www.google.com")
        print()
    elif user == "spec p":
        choice1 = input("do you want to continue?[y/n]: ")
        if choice1 == "y":
            print("You perverted jerk")
            time.sleep(5)
            webbrowser.open("https://www.google.com")
            print()
        else:
            print("Good decision\n")
