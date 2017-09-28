import os
import face_recognition
import sys
import pickle
import numpy
from collections import Counter
known_encoding=[]
directory=input("Enter directory:")
if(len(directory)<=1):
    print('Enter a valid path for KABOOM!!!!')
    exit(1)
else:
    image=face_recognition.load_image_file(directory)
    encoding=face_recognition.face_encodings(image)
    print('Original encoding:')
    print(encoding)
    print('********************************************************************************')
    res=pickle.load(open("encoding_info.pkl","rb"))
    for i in res:
       a,b=i
       known_encoding.append(b)



