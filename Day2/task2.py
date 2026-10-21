key = input("Enter the key (w/a/s/d/space)")

match key:

    case "w":
        print("Moving Forward")

    case "a":
        print("Moving Backward")

    case "s":
        print("Stepping left")

    case "d":
        print("Stepping Right")

    case "space":
        print("Jumping High")

    case _:
        print("Invalid Key")


    
