switch_on=input("Is the charger switch is ON? (Yes?No)")

if switch_on =="Yes":
    cable_connected = input("Is cable plugged into the phone? (Yes/No):")

    if cable_connected == "Yes":
        print("phone is charging...")

    else:
        print("Switch is on, but cable is not pugged in")

else:
    print("Switch is Off, Turn on the switch first")
