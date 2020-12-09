import sys
import threading
import time
from threading import*
datastore={} 
def C(k,v,timestamp=0):
    if k in datastore:
        print("this key already exists")
    else:
        if(k.isalpha()):#checking dtype
            if sys.getsizeof(datastore)<(1000000000) and sys.getsizeof(v)<=(16000):
                if timestamp==0:
                    l=[v,timestamp]
                else:
                    l=[v,time.time()+timestamp]
                if len(k)<=32: 
                    datastore[k]=l
            else:
                raise Exception(" Memory limit exceeded!! ")
        else:
            raise Exception(" Invalid key name!! ")

            
def R(k):
    if k not in datastore:
        raise Exception("given key does not exist in datastore.  enter a valid key") 
    else:
        temp=datastore[k]
        if temp[1]!=0:
            if time.time()<temp[1]:
                concat=str(k)+":"+str(temp[0]) 
                return concat
            else:
                print("error: time-to-live of",k,"has expired") 
        else:
            concat=str(k)+":"+str(temp[0])
            return concat

def  D(k):
    if k not in datastore:
        raise Exception(" given key does not exist in database.enter a valid key") 
    else:
        temp=datastore[k]
        if temp[1]!=0:
            if time.time()<temp[1]: 
                del datastore[k]
                print("k is successfully deleted")
            else:
                print("error: time-to-live of",k,"has expired") 
        else:
            del datastore[k]
            print("k is successfully deleted")




