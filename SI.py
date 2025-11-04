p = float(input("Enter principal amount: " ))
r = float(input("Enter rate : " ))
t = float(input("Enter time(years): " ))


def copoundIntrest(p,r,t, tcompute):
    if tcompute==t:
        print(p ," " , t)
        return p
    SI  = (p * r * t)/100+p
    return copoundIntrest(SI,r,t,tcompute+1)
x = copoundIntrest(p,r,t,0)
print("Simple Interest is: ",x )