from cryptography.fernet import Fernet
import os

os.system('cls')
main_key=Fernet.generate_key()
with open('main_key.txt','wb') as KEY :
    KEY.write(main_key)
f=Fernet(main_key)
with open('Hydrangeas.jpg','rb') as orgpic:
    main_pic=orgpic.read()
enk=f.encrypt(main_pic)
with open("Hydrangeas.jpg",'wb') as changpic :
    changpic.write(enk)