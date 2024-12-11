# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:38:19 2024

"""
import numpy as np
import matplotlib.pyplot as plt


# This function will receive an array ('image') with values between 0 and 255, rescale eache element
# to the range [0,1] and then apply the formula R=kL+b to convert Radiance to Refractance
# the return will be an array with decimal in range [0,1]
  
def rad_to_ref(image: np.ndarray,k,b):
    image=image.__truediv__(255)
    image=image.__mul__(k)
    image=image.__add__(b)
    return image   #multiply every element by k and add b (k*L+b)


# This function will receive and array with decimal values and convert each value to an integer in the range [0,255]
def rescale(image):
    image=image.__mul__(255)
    image= image.round().astype('uint8')
    return image

# save array as an image with the provided filename and path. 
# If path is omitted, it will save on the current working directory. 
# path must be provided without the end backslash
def savefile(array,filename,path=''):
    if path != '':
        path += "\\"
    plt.imsave(path + filename +'.png',array)




# import each CSV file to an array. 
# files must be on the working directory or the path must be provided with the file name.
# It will gnore the first row which have a header
# the data type will be unsigned integer 8-bytes
r = np.loadtxt('red.csv',dtype='uint8',delimiter=',',skiprows=1,)
g = np.loadtxt('green.csv',dtype='uint8',delimiter=',',skiprows=1)
b = np.loadtxt('blue.csv',dtype='uint8',delimiter=',',skiprows=1)


# Try to stack all three bands in a rgb array and remove the first colum wich has a label
# if any of them have a diferent size it will raise an error and stop execution
try:
    rgb = np.stack((r,g,b),axis=2)
    rgb = np.delete(rgb,[0],axis=1)

except:
    print("Input arrays are not the same size.")
    print(f"r={r.shape}")
    print(f"g={g.shape}")
    print(f"b={b.shape}")
else: 
    plt.imshow(rgb)
    plt.axis('off')
    plt.show()
    new_image=rad_to_ref(rgb, 0.8, 0.1)
    plt.imshow(new_image)
    plt.axis('off')
    plt.show()
    rescaled_image = rescale(new_image)
    plt.imshow(rescaled_image)
    plt.axis('off')
    plt.show()
    savefile(rescaled_image,'check_plus.png')

