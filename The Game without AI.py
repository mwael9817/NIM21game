x=21
while x!=1:
    y=int(input("Player 1 "))
    if y>3 or y<1 or y>=x:
        print("Illegal move, Please try again")
    else:
        x=x-y
        print(x)
        if x==1:
            print("Player 2 loses")
        else:
            z=int(input("Player 2 "))
            if z>3 or z<1 or z>=x:
                  print("Illegal move, please try again")
            else:
                  x=x-z
                  print(x)
                  if x==1:
                      print("Player 1 loses")
                  
              
