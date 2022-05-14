from tkinter import *
from simplecrypt import encrypt, decrypt
from tkinter import filedialog
import os
from tkinter import messagebox as mbox 

root = Tk()
root.title('Decrypting Data')
root.geometry("400x250")
root.configure(bg="#90EE90")

file_name_entry=''
encryption_text_data=''

def saveData():
    global file_name_entry
    global encryption_text_data
    file_name=file_name_entry.get()
    file=open(file_name+'.txt','w')
    data=encryption_text_data.get("1.0",END)
    ciphercode=encrypt("KEY",data)
    print(ciphercode)
    hexdata=ciphercode.hex()
    print(hexdata)
    file.write(hexdata)
    file_name_entry.delete(0,END)
    encryption_text_data.delete(1.0,END)
    mbox.showinfo("Update","Data has succesfuly been updated")

def viewData():
    global decryption_text_data
    text_file=filedialog.askopenfilename(title="Open Text File",filetype=(("Text Files","*.txt"),))
    name=os.path.basename(text_file)
    print(name)
    read_file=open(name,"r")
    paragraph=read_file.read()
    bytes_string=bytes.fromhex(paragraph)
    decrypted_value=decrypt("KEY",bytes_string)
    final_output=decrypted_value.decode("utf-8")
    print(final_output)
    decryption_text_data.insert(END,final_output)

def startDecryption():
    global file_name_entry
    global decryption_text_data
    root.destroy()
 
    decryption_window = Tk()
    decryption_window.geometry("600x500")
    
    decryption_text_data = Text(decryption_window, height=20, width=72)
    decryption_text_data.place(relx=0.5,rely=0.35, anchor=CENTER)
    
    btn_open_file = Button(decryption_window, text="Choose File..", font = 'arial 13',relief=FLAT,bg="orange",command=viewData)
    btn_open_file.place(relx=0.5,rely=0.8, anchor=CENTER)
    
    decryption_window.mainloop()
    
    
def startEncryption():
    global file_name_entry
    global encryption_text_data
    root.destroy()
 
    encryption_window = Tk()
    encryption_window.geometry("600x500")
    
    file_name_label = Label(encryption_window, text="File Name: " , font = 'arial 13',bg="#90EE90")
    file_name_label.place(relx=0.1,rely=0.15, anchor=CENTER)
    
    file_name_entry = Entry(encryption_window, font = 'arial 15',bg="#90EE90")
    file_name_entry.place(relx=0.38,rely=0.15, anchor=CENTER)
    
    btn_create = Button(encryption_window, text="Create", font = 'arial 13',command=saveData,relief=FLAT,bg="orange")
    btn_create.place(relx=0.75,rely=0.15, anchor=CENTER)
    
    encryption_text_data = Text(encryption_window, height=20, width=72)
    encryption_text_data.place(relx=0.5,rely=0.55, anchor=CENTER)
    
    encryption_window.mainloop()
    
    
heading_label = Label(root, text="Encryption & Decryption" , font = 'arial 18 italic')
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)

btn_start_encryption = Button(root, text="Start Encryption" , font = 'arial 13' , command=startEncryption)
btn_start_encryption.place(relx=0.3,rely=0.6, anchor=CENTER)

btn_start_decryption = Button(root, text="Start Decryption" , font = 'arial 13' ,  command=startDecryption)
btn_start_decryption.place(relx=0.7,rely=0.6, anchor=CENTER)

root.mainloop()

