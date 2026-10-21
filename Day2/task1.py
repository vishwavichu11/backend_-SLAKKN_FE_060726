extentions=input("Enter file extention (1.html/2.css/3.js/4.py):")

match extentions:
    case "html":
        print("webpage structure file")

    case "css":
        print("Styling & Designing")

    case "js":
        print("Frontend logic")

    case "py":
        print("python backend Script")

    case _:
        print("Unknown File Type!")
