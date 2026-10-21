workout_day = input("Enter workout day (chest / back / shoulder / legs): ")
match workout_day:
    case "chest":
        print("Workout: Flat Bench Press, Incline Dumbbell Press & Push-ups.")

    case "back":
        print("Workout: Lat Pulldown, Seated Cable Row & Deadlift.")

    case "shoulder":
        print("Workout: Overhead Barbell Press, Lateral Raises & Face Pulls.")

    case "legs":
        print("Workout: Barbell Squats, Leg Press & Calf Raises.")

    case _:
        
        print("Rest Day")
