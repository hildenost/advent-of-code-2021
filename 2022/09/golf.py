for k in 2,10:
 h=set() 
 r=[(0,0)]*k
 for m in open("a"):
  for _ in range(int(m[2:])):
   d,x,y=m[0],*r[0]
   r[0]=(x+(d=="R")-(d=="L"),y+(d=="U")-(d=="D"))
   for i in range(1,k):
    x,y,v,w=*r[i],*r[i-1]
    if not(-2<v-x<2 and-2<w-y<2):r[i]=(x+(v>x)-(v<x),y+(w>y)-(w<y))
   h|={r[-1]}
 print(len(h))
