import pickle
import os
import face_recognition
directory=os.getcwd()
encoding_info=[]
i=0
for file in os.listdir(directory):
    filename=os.fsdecode(file)
    if(filename.startswith("Image")):
         image=face_recognition.load_image_file(filename)
         encoding=face_recognition.face_encodings(image)
         encoding_info.append((filename,encoding))
pickle.dump(encoding_info,open("encoding_info.pkl","wb"))
# res=pickle.load(open("encoding_info.pkl","rb"))
# for i in res:
#     a,b=i
#     print(a)