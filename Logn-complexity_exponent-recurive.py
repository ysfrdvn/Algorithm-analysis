def power_recursive(x,y):
    if(y==0):
        return 1
    if(y==1):
        return x
    if(y%2==0):
        return power_recursive(x*x,int(y/2))
    if(y%2==1):
        return power_recursive(x*x,int(y/2)) * x  #logn karmaşıklık

power_recursive(2,999)        