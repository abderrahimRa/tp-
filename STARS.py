N=int(input("enter the value please"))
lst=[]
lsst=[]
k=0
o=N
if N%2==0:
          z=int((N)/2)
          for i in range(N):
                  lst.append(" ")
          for i in range(z,N):#this is for adding *in the first part whish is half 
                    lst[i]="*"
                    k=N-i
                    lst[k]="*"
                    print(*lst)
                    
          print(*lst)
          for i in range(1,int(N/2)):#this is for deleting the * that i used in the first part :)
                    lst[i]=" "
                    o=o-1
                    lst[o]=" "                 
                    print(*lst)
          
else:
          
          z=int((N)/2)
          for i in range(N):
                  lst.append(" ")
          lst[z]=("*")
          k=int(((N-1)/2))
          for i in range(z,N):#this is for adding *in the first part  the fist half  
                    lst[i]="*"
                    lst[k]="*"
                    print(*lst)
                    k=k-1
          o=N
          for i in range(0,int(N/2)):#now we gonna delete it with " " using void 
                   lst[i]=" "
                   o=o-1
                   lst[o]=" "  
                   print(*lst)
          #i can tell that the code can be shorter but it so complicated ,i can't simplify it :) 
                  
