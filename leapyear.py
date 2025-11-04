# x = input("year")
# if (    (x)%4==0 & int(x)%100!=0) | (int(x)%400==0):
#     print(x,"is leap year")

x = int(input("year: ")); print(x,"is leap year") if (x%4==0 and x%100!=0) or (x%400==0) else print(x,"is not leap year")
