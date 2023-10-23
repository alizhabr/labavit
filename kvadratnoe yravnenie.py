a=int(input())
b=int(input())
c=int(input())
d=b**2-4*a*c
if d<0:
    print("нет решения")
if d==0:
    print("корень: ", -b/(2*a))
else:
    print("1 корень: ", (-b+d**.5)/(2*a))
    print("2 корень: ",(-b-d**.5)/(2*a))
