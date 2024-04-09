database=["Croaks","Eat Flies","Shrimps","Sings"]
knowbase=["Frog","Canary","Green","Yellow"]
def display():
    print("\n X is \nl..Croaks \n2.Eat Flies \n3.shrimps \n4.Sings",end=")
    print("\n Select One",end=")
def main():
          print("----Forward--Chaining----.",end=")
          display()
          x=int(input())
          print(" \n",end=")
          if x==1 or x== 2:
                print(" Chance Of Frog",end=")
          elif x==3 or x==4:
                      print(" Chance of Canary ",end=")
          else:
                            print("\n----n Valid Option Select---",end=")

          if x>=l and x<=4:
                                  
                                  print("\n X is ",end=")
                                  print(database[x-1],end=")
                                  print("\n Color Is 1.Green 2.Yellow",end=")
                                  print("\n Select Option ",end=")
                                  k= int(input())  
          if k==l and(x==l or x==2):      
                                        print(" yes it is ",end=")
                                        print(knowbase[0],end=")
                                        print(" And Color Is ", end=")
                                        print(knowbase[2], end=")
          elif k==2 and(x ==3 or x==4):
                                              print(" yes it is ", end=")
                                              print(knowbase[ l ], end=")
                                              print(" And Color Is ", end=")
                                              print(knowbase[3], end=")
          else:                                                   
                                                    print("\n---InValid Knowledge Database", end=")
if __name__=="__main__":                                                       
main()
