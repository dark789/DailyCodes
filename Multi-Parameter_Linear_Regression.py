def loss(x,y,w):
    nd=len(x)   
    n=len(x[0]) 
    s=0.0
    for i in range(n):  
        s+=dif(x,y,w,i)**2
    s=s/n
    return s
def grad(x,y,w):
    nd=len(x)   
    n=len(x[0]) 
    gradw=[]
    for j in range(nd+1):
        s=0.0
        if j==0:
            for i in range(n):
                s+=dif(x,y,w,i)
            s=2*s/n
            gradw.append(s)
        else:
            for i in range(n):
                s+=dif(x,y,w,i)*x[j-1][i]
            s=2*s/n
            gradw.append(s)
    return gradw
def dif(x,y,w,i):
    A=0.0
    nd=len(x)
    for j in range(nd+1):
        if j==0:
            A+=w[j]
        else:
            A+=w[j]*x[j-1][i]
    A=A-y[i]
    return A
def graddes(x,y,a,w0,loops=100,limit=1e-5,options=1):
    nd=len(x)
    wn=w0
    if options==1:
        for l in range(loops):
            wtem=wn
            for j in range(nd+1):
                wn[j]=wn[j]-a*grad(x,y,wtem)[j]
            print(l+1,chr(9),wn,chr(9),"loss=",loss(x,y,wn))
        print("total:",l+1,"final w:",wn)
    if options==2:
        loopswitch=0
        l=0
        for j in range(nd+1):
            if grad(x,y,wn)[j]>=limit:
                loopswitch=1
                l+=1
                break
        print(loopswitch)
        while loopswitch:
            wtem=wn
            for j in range(nd+1):
                wn[j]=wn[j]-a*grad(x,y,wtem)[j]
            print(l,chr(9),wn,chr(9),"loss=",loss(x,y,wn))
            loopswitch=0
            for j in range(nd+1):
                if grad(x,y,wn)[j]>=limit:
                    loopswitch=1
                    l+=1
                    break
        print("total:",l,"final w:",wn)
    return wn
x=[[1,2,3,4,5]]
y=[2,4,6,8,10]
w0=[0.5,2.5]
graddes(x,y,0.01,w0,options=2)

            
            
        
        
    
    
    

