import matplotlib.pyplot as mp
import time as t
t_list=[]
count=0
for i in range(0,3):
    st_t=t.time()
    print("Round",i+1,":")
    in_word=input("Enter Hello:")
    timet=t.time()-st_t
    t_list.append(timet)
    samp="Hello"
    for j in range(len(in_word)):
        if(in_word[j]!=samp[j]):
           count+=1
x=[1,2,3]
mp.plot(x,t_list)
print("No. of mistakes made:",count)
mp.show()