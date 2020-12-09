
from threading import Thread, Lock
_db_lock = Lock()



import proj2 as p 
p.C("HELLOWORLD",25)
p.C("object_VAR",70,3600) 
p.R("HELLOWORLD")
p.R("object_VAR")
p.C("HELLOWORLD",50)
p.D("HELLOWORLD")
k1=input()
v1=input()
timestamp1=int(input())
k2=input()
v2=input()
timestamp2=int(input())
t1=Thread(target=(p.C or p.R or p.D),args=(k1,v1,timestamp1))
t2=Thread(target=(p.C or p.R or p.D),args=(k2,v2,timestamp2))
t1.start()
t2.start()
t1.join()
t2.join()
print("DONE")

