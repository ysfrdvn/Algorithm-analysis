def power_recursive(x,y):
    global sayac
    sayac = sayac + 1
    if(y==0):
        return 1
    if(y==1):
        return x
    if(y%2==0):
        return power_recursive(x*x,int(y/2))
    if(y%2==1):
        return power_recursive(x*x,int(y/2)) * x  #logn karmaşıklık

power_recursive(2,999)        

def call_report_rec(x,y):
    global sayac
    sayac = 0
    r = power_recursive(x,y)
    print(x, " üzeri ",y, " değeri : ",r, " çağrım sayisi : ", sayac)

call_report_rec(2,999)    #999 u 10 çağırımda buluyo
