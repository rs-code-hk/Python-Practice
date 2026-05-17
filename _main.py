age = 11
temp = "Hello"

match age:
    case _ if temp == "Hello":
        print("This happened")
    case _ if age < 10:
        print("You are younger than ten")
    case 10:
        print("You are ten")
    case _ if age > 10:
        print("You are older than 10")