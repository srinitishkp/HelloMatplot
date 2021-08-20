import matplotlib.pyplot as mp
import time as t
t_list=[]
count=0
print("Program to record typing times and produce a chart")
for i in range(0,3):
    print("Round",i+1,":")
    input("Press enter to start round")
    st_t=t.time()
    in_word=input("Enter Hello:")
    timet=t.time()-st_t
    t_list.append(timet)
    samp="Hello"
    try:
        for j in range(len(in_word)):
            if(in_word[j]!=samp[j]):
                  count+=1
    except IndexError:
        count+=1
x=[1,2,3]

legend=["1","2","3"]
print("No. of mistakes made:",count)
while(True):
    ch=input("1.Linear graph \n2.Bar graph \n3.Exit\n Enter your choice") 
    print(ch)
    if ch== "1":
        mp.xticks(x,legend)
        mp.plot(x,t_list)
        mp.xlabel("Attempt")
        mp.ylabel("Time taken")
        mp.title("Typing time evolution")
        mp.show()   
    elif ch=="2":
        mp.xlabel("Attempt")
        mp.ylabel("Time taken")
        mp.title("Typing time evolution")
        mp.bar(x,t_list)
        mp.xticks(x,legend)
        mp.show()
    else:
        exit()
    