import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

def Convolution(img,kernal):
    
    #This convolution will decrease the size of the img
    
    ix,iy=img.shape
    kx,ky=kernal.shape
    dsize=int(kx/2)
    outimg=np.zeros((ix-2*dsize,iy-2*dsize))
    for i in range(dsize,(ix-dsize)):
        for j in range(dsize,(iy-dsize)):
            temkx=0
            temky=0
            s=0
            for m in range(i-int(kx/2),i+int(kx/2)+1):
                temky=0
                for n in range(j-int(ky/2),j+int(ky/2)+1):
                    s+=img[m,n]*kernal[temkx,temky]
                    temky+=1
                temkx+=1
            outimg[i-dsize,j-dsize]=s
    return outimg



#Some special convolutions are followed

#Sobel Kernals:
img=cv.imread(r"G:\python\ModualPrictice\opencv\TestPics\Test1.jpg")
img=img[:,:,1]
ver1=np.array([[1,0,-1],
              [2,0,-2],
              [1,0,-1]])
ver2=np.array([[-1,0,1],
               [-2,0,2],
               [-1,0,1]])
hor1=np.array([[1,2,1],
              [0,0,0],
              [-1,-2,-1]])
hor2=np.array([[-1,-2,-1],
              [0,0,0],
              [1,2,1]])
con1=Convolution(img,ver1)
con2=Convolution(img,ver2)
con3=Convolution(img,hor1)
con4=Convolution(img,hor2)
allcon=(con1**2+con2**2+con3**2+con4**2)**0.5
allcon[allcon>255]=255
allcon[allcon<0]=0
allcon=allcon.reshape(allcon.shape[0],allcon.shape[1],1)
zeros=np.zeros((allcon.shape[0],allcon.shape[1],1))
allcon=np.concatenate((zeros,allcon,zeros),axis=2)

cv.imwrite(r"G:\python\ModualPrictice\opencv\TestPics\Test3.jpg",allcon)
plt.subplot(321)
plt.imshow(img)
plt.subplot(322)
plt.imshow(allcon)
plt.subplot(323)
plt.imshow(con1)
plt.subplot(324)
plt.imshow(con2)
plt.subplot(325)
plt.imshow(con3)
plt.subplot(326)
plt.imshow(con4)
plt.show()



