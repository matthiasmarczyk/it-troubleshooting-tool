print("IT Troubleshooting Tool")

while True:
    print("\nChoose a problem:")
    print("1 - Internet is not working")
    print("2 - Printer is not working")
    print("3 - PC does not start")
    print("4 - Exit")

    choice = input("Enter a number: ")

    if choice == "1":
        print("\nSuggested steps:")
        print("- Check if LAN or Wi-Fi is connected.")
        print("- Restart the router.")
        print("- Test the connection on another device.")

    elif choice == "2":
        print("\nSuggested steps:")
        print("- Check if the printer is turned on.")
        print("- Check the cable or Wi-Fi connection.")
        print("- Restart the printer.")

    elif choice == "3":
        print("\nSuggested steps:")
        print("- Check the power cable.")
        print("- Check if the monitor is turned on.")
        print("- Hold the power button for 10 seconds and try again.")

    elif choice == "4":
        print("\nExiting the program.")
        break

    else:
        print("\nInvalid input. Please choose a number from the menu.")