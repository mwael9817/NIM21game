x=21
while x!=1:
    y=int(input("Player 1 "))
    if y>3 or y<1 or y>=x:
        print("Illegal move, try again")
    else:
        x=x-y
        print(x)
        if x==1:
            print("Computer loses")
        if y==1:
            z=3
        elif y==2:
            z=2
        elif y==3:
            z=1
        x=x-z
        print(x)
        if x==1:
            print("Computer Won")
            print("Thanks for playing(Losing)")
        
