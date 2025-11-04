details ={
    "name": [],
    "age": []
}
x  = input("enter th no of entries")
for i in range(int(x)):

    details["name"].append(input("Enter name: "))
    details["age"].append(int(input("Enter age: ")))
for i in range(int(x)):

    # print([int(x)])
    print("Name is",details["name"][i])
    print("Age is",details["age"][i])