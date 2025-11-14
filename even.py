def check(*a):
    
    result=[]
    for i in a:
        if i%2==0:
            result.append("even")
        else:
            result.append("Odd")
        
    return result
    
    