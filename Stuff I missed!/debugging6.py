MEMBER_STATUS = "GOLD"
passenger_row = int(input("Enter your seat row: ").strip())
has_ticket = input("Do you have a valid ticket? (yes/no): ").strip().lower()
if has_ticket == "no":
    print("Access Denied. Please ensure you have a valid ticket before boarding.")

else:
    if passenger_row <= 8 and MEMBER_STATUS == "GOLD":
        print("Welcome to priority boarding! Please make your way on board now.")
    elif passenger_row <= 8 and MEMBER_STATUS != "GOLD":
        print("Welcome to priority boarding! Please wait for our Gold Business Flyers to finish boarding.")
    else:
        print("Please wait for general boarding.")

    destination = input("Enter your destination code: ").upper().strip()
    if destination in ["AKL", "WLG"]:
        print("Flight is delayed 5 minutes.")
    elif destination != "CHC":
        print("Flight is on time")
    else:
        print("Flight has been cancelled")