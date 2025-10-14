write=str(input())
started = False
while True:
 write=input(">").lower()
 if write== str("start"):
    if started:
       print("car is alrady started")
    else  :
       started= True
    print("start the car")
 elif write==str("stop") :
    if not started:
       print("car is alrady stoped")
    else :
       started=False  
    print("stop the car") 
 elif write==str("quit") :
    print("exit the car")   
 else :
    print("i dont understand that...")    