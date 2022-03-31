N = int(input())
list=[]
for _ in  range (N):
 x=input().split(" ")
 command =x[0]
 if command=="insert":
  list.insert(int(x[1]),int(x[2]))
 if command=="print":
  print(list)
 if command=='remove':
    list.remove(int(x[1]))
 if command=='append':
    list.append(int(x[1]))
 if command=='sort':
    list.sort()
 if command=='pop':
    if(len(list)!=0):
     list.pop()
 if command=='reverse':
    list.reverse()




