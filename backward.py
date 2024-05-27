database=["craoks","eat flies","shrimps","sings"]
knowbase=["frog","canary"]
color=["green","yellow"]
def display():
    print("x is\n1.frog\n2.canary",end='')
    print("select one",end='')
def main():
    print("backward chaining",end='')
    display()
x=int(input())
print("\n",end='')
if x==1:
    print("chnace of eating flies",end='')
elif x==2:
    print("chance of shrimping",end='')
else:
    print("invalid option select",end='')
    if x>=1 and x<=2:
        print("x is",end='')
        print(knowbase[x-1],end='')
        print("\n1.green\n2.yellow")
        k=int(input())
    if k==1 and x==1:
        print("yes it is in",end='')
        print(color[0],end='')
        print("color and will",end='')
        print(database[0])
    elif k==2 and x==2:
        print("yes it is in",end='')
        print(color[1],end='')
        print("color and will",end='')
        print(database[1])
    else:
        print("invalid knowledge databsee",end='')
if __name__=="__main__":
    main()

