from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pyautogui
import time

groups = ['603444704719112']

def start():
    time.sleep(5)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('t')
    pyautogui.keyUp('t')
    pyautogui.keyUp('ctrl')


    for i in range(len(groups)):
        link = 'https://facebook.com/groups/'+groups[i]
        pyautogui.typewrite(link)
        pyautogui.typewrite('\n')
        time.sleep(7)
        for i in range (0,27):
            pyautogui.keyDown('tab')
            pyautogui.keyUp('tab')
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')
        
        print("Waiting for 5 seconds\n")
        time.sleep(5)
        print("Writing post\n")
        pyautogui.typewrite("Hello there")

        for i in range (0,3):
            pyautogui.keyDown('tab')
            pyautogui.keyUp('tab')
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.keyDown('tab')
        pyautogui.keyUp('tab')
        

        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        
        time.sleep(4)
        pyautogui.typewrite("F:\ECODIBBA\Face Book Auotamation Task 1\photo.jpg")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        for i in range (0,6):
            pyautogui.keyDown('tab')
            pyautogui.keyUp('tab')
        
        # pyautogui.keyDown('ctrl')
        # pyautogui.keyDown('enter')
        # pyautogui.keyUp('enter')
        # pyautogui.keyUp('ctrl')

        # time.sleep(3)

        # pyautogui.write(['f6'])
        # time.sleep(1)


root = Tk()

root.title('Login Form')
# root.iconbitmap('favicon.ico')

root.geometry('700x500')

root.configure(background='#171717')


text_label = Label(root,text='Facebook Automatate',fg='white',bg='#7E7C73')
text_label.pack()
text_label.config(font=('verdana',24))

# email_label = Label(root,text='Enter Email',fg='white',bg='#0096DC')
# email_label.pack(pady=(20,5))
# email_label.config(font=('verdana',12))

# email_input = Entry(root,width=50)
# email_input.pack(ipady=6,pady=(1,15))

# password_label = Label(root,text='Enter Password',fg='white',bg='#0096DC')
# password_label.pack(pady=(20,5))
# password_label.config(font=('verdana',12))

# password_input = Entry(root,width=50)
# password_input.pack(ipady=6,pady=(1,15))

login_btn = Button(root,text='Start',bg='white',fg='black',width=20,height=2,command=start)
login_btn.pack(pady=(20,20))
login_btn.config(font=('verdana',10))



root.mainloop()