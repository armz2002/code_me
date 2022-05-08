import os
from cryptography.fernet import Fernet

with open ("main_key.txt",'rb') as keyy:
    key=keyy.read()
f=Fernet(key)
with open ('Hydrangeas.jpg','rb') as enkpic:
    enkpicture=enkpic.read()
dek=f.decrypt(enkpicture)
with open ('Hydrangeas.jpg','wb') as main_pic :
    main_pic.write(dek)