from threading import Thread
import random
import tkinter as tk
from tkinter import X, StringVar, filedialog,Radiobutton
import webbrowser
import pyautogui
import time
import keyboard 
from tkinter import messagebox as tmsg

global flow 
flow = True
groups = []
extime=3
group_file_path=""

def data():
    file3=open('groups.txt','r')
    Lines=file3.readlines()
    groups.clear()
    for line in  Lines:
        line.strip()
        groups.append(line)
    print(groups)
    file3.close()



def start( Content,img1,img2):
    if (flow==True):
        time.sleep(5)
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('t')
        pyautogui.keyUp('t')
        pyautogui.keyUp('ctrl')

        if (flow==True):
            for i in range(len(groups)):
                link = 'https://facebook.com/groups/'+groups[i]
                pyautogui.typewrite(link)
                pyautogui.typewrite('\n')
                y = random.randint(1,5)
                time.sleep(5+y)
                if (flow==True):
                    pyautogui.keyDown('p')
                    pyautogui.keyUp('p')


                    
                    print("Waiting for  seconds\n")
                    y = random.randint(0,2)
                    time.sleep(1+y)
                    if (flow==True):
                        print("Writing post\n")
                        pyautogui.typewrite(Content)
                        if (flow==True):
                            for i in range (0,3):
                                pyautogui.keyDown('tab')
                                pyautogui.keyUp('tab')
                                time.sleep(0.5)
                            pyautogui.keyDown('enter')
                            pyautogui.keyUp('enter')

                            if (flow==True):
                                pyautogui.keyDown('tab')
                                pyautogui.keyUp('tab')
                            
                                time.sleep(1)
                                if (flow==True):
                                    pyautogui.keyDown('enter')
                                    pyautogui.keyUp('enter')

                                    y = random.randint(1,4)

                                    time.sleep(1+y)
                                    if (flow==True):
                                        img=random.choice([img1,img2])
                                        print("Uploading image\n")
                                        pyautogui.typewrite(img)
                                        time.sleep(1)
                                        pyautogui.keyDown('enter')
                                        pyautogui.keyUp('enter')
                                        time.sleep(1)
                                        if (flow==True):
                                            for i in range (0,6):
                                                pyautogui.keyDown('tab')
                                                pyautogui.keyUp('tab') 
                                                time.sleep(0.5) 

                                            if (flow==True):
                                                pyautogui.keyDown('enter')
                                                pyautogui.keyUp('enter') 
                                                y = random.randint(0,5)
                                                time.sleep(8+y+extime)
                                                
                                                if (flow==True):
                                                    pyautogui.write(['f6'])
                                                    y = random.randint(1,3)
                                                    time.sleep(y)
                                                else:
                                                    print(" terminated")
                                            else:
                                                print("Stop msg")
                                        else:
                                            print("stop execut")
                                    else:
                                        print("exe spt")
                                else:
                                    print("stp")
                            else:
                                print("execution stop")
                        else:
                            print("No match found")
                    else:
                        print ("Stopped")
                else:
                    print("Stop")
            else:
                print("Stopped Execution")




       



class FacebookPostUI:
    
    def __init__(self, master):
        self.master = master
        self.master.title("Facebook Page Post")
        self.master.configure(bg="#f7f7f7")
        
        
        # Title
        self.title_label = tk.Label(master, text="Facebook Bulk advertiser", bg="#3b5998", fg="white", font=("Roboto", 15, "bold"))
        self.title_label.pack(fill=tk.X, pady=1)
        
        # URL Entry
        self.url_label = tk.Label(master, text="ADD URL", bg="#f2f3f4", font=("Roboto", 9))
        self.url_label.pack()
        self.url_text = tk.Text(master, height=3, width=50, bg="white", fg="#333333", font=("Roboto", 10))
        self.url_text.pack(pady=10, padx=10, ipady=5, ipadx=5, fill=tk.BOTH)
        
        # Button to add groups
        self.post_button = tk.Button(master, text="Add Facebook Groups", bg="#3b5998", fg="white", font=("Roboto",5, "bold"), command=self.add_IDs)
        self.post_button.pack(pady=10, padx=40, ipady=5, ipadx=1, fill=tk.X)
        
        # URL Entry
        self.ids_label = tk.Label(master, text="Manage IDs", bg="#f2f3f4", font=("Roboto", 9))
        self.ids_label.pack()
        self.ids_text = tk.Text(master, height=4, width=50, bg="white", fg="#333333", font=("Roboto", 10))
        self.ids_text.pack(pady=10, padx=10, ipady=5, ipadx=5, fill=tk.BOTH)
    
        # ids count
        # self.image_display = tk.Label(master, textvariable=, bg="#f2f3f4", fg="#333333", font=("Roboto", 10))
        # self.image_display.pack(pady=5)
        
        
        # Button to add groups
        self.post_button = tk.Button(master, text="Update Facebook Group IDs", bg="#3b5998", fg="white", font=("Roboto", 5, "bold"), command=self.update_IDs)
        self.post_button.pack(pady=8, padx=10, ipady=5, ipadx=1, fill=tk.BOTH)
        
       
        
        # Content Entry
        self.content_label = tk.Label(master, text="Post Content", bg="#f2f3f4", font=("Roboto", 7))
        self.content_label.pack()
        self.content_text = tk.Text(master, height=7, width=50, bg="white", fg="#333333", font=("Roboto", 7))
        self.content_text.pack(pady=5, padx=5, ipady=5, ipadx=5, fill=tk.BOTH)

        
        # Image Selection
        self.image_label = tk.Label(master, text="Select Media 1", bg="#f2f3f4", font=("Roboto", 7))
        self.image_label.pack(side="left",pady=5)
        self.image_path = tk.StringVar()
        self.image_path.set("No Media selected")
        self.image_button = tk.Button(master, text="Browse", bg="#3b5998", fg="white", font=("Roboto", 7), command=self.browse_image)
        self.image_button.pack(side="left",pady=5)
        self.image_display = tk.Label(master, textvariable=self.image_path, bg="#f2f3f4", fg="#333333", font=("Roboto", 7))
        self.image_display.pack(side="left",pady=5)  
         
        # Image Selection
        self.image_label = tk.Label(master, text="Select Media 2", bg="#f2f3f4", font=("Roboto",7))
        self.image_label.pack(side="left",pady=5)
        self.image_path2 = tk.StringVar()
        self.image_path2.set("No Media selected")
        self.image_button2 = tk.Button(master, text="Browse", bg="#3b5998", fg="white", font=("Roboto",7), command=self.browse_image2)
        self.image_button2.pack(side="left",pady=5)
        self.image_display = tk.Label(master, textvariable=self.image_path2, bg="#f2f3f4", fg="#333333", font=("Roboto", 7))
        self.image_display.pack(side="left",pady=5)  
         
        
        
         # Note for users
        self.image_display = tk.Label(master, text="Press Activate button to enable posting", bg="#f2f3f4", fg="#333333", font=("Roboto", 10))
        self.image_display.pack(side="left" ,pady=5)



        #Activation Button
        self.active_button = tk.Button(master, text="Activate", bg="#3b5998", fg="white", font=("Roboto", 8), command=self.activate)
        self.active_button.pack(side='left',pady=5)     
           # Post Button
        self.post_button = tk.Button(master, text="    Post to Facebook     ", bg="#3b5998", fg="white", font=("Roboto",7, "bold"), command=self.post_to_facebook)
        self.post_button.pack(side="left",pady=10, padx=40, ipady=5, ipadx=1 )

         # Schedule Button
        self.post_button = tk.Button(master, text="Schedule for Everyday", bg="#3b5998", fg="white", font=("Roboto", 7, "bold"), command=self.schedule)
        self.post_button.pack(side="left",pady=10, padx=40, ipady=5, ipadx=1)   

        # # add radio buttons
        
        # v = StringVar(master, "1")
 
        # # Dictionary to create multiple buttons
        # values = {"Video" : "1",
        #         "Photo" : "2"}
 
        # # Loop is used to create multiple Radiobuttons
        # # rather than creating each button separately
        # for (text, value) in values.items():
        #     Radiobutton(master, text = text, variable = v, 
        #                 value = value, indicator = 0,
        #                  bg="#3b5998", fg="white", font=("Roboto", 10, "bold")).pack(fill = X, pady = 5)
        
    
        self.change_value()
    def fetch_file(self):
        ftyp=1
        if ftyp==1:
            ans=tmsg.askquestion("Assure your file type.","Your media is an image?")
            if ans=='yes':
                ftyp=1
                extime=0
            else:
                ftyp=2
                extime=3

        print(extime)
        print (ftyp)
    
    

    def browse_image(self):
        
        filename1 = filedialog.askopenfilename(initialdir="/", title="Select Media",
                                              filetypes=(("Image files", "*.jpg *.jpeg *.png *.gif *.3g2 *.3gp *.3gpp *.m4v *.mp4 *.mepg4 *.mov *.mkv *.qt *.vob"), ("All files", "*.*")))
        if filename1:
            self.image_path.set(filename1)
            
    def browse_image2(self):
        
        filename2 = filedialog.askopenfilename(initialdir="/", title="Select Media",
                                              filetypes=(("Image files", "*.jpg *.jpeg *.png *.gif *.3g2 *.3gp *.3gpp *.m4v *.mp4 *.mepg4 *.mov *.mkv *.qt *.vob"), ("All files", "*.*")))
        if filename2:
            self.image_path2.set(filename2)
    def browse_groups(self):
        groupname = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("Group files", "*.txt *doc"), ("All files", "*.*")))
        self.groups_path.set(groupname)
        group_file_path=str((groupname))
        print(group_file_path)
        


    def post_to_facebook(self):
        self.fetch_file()
        permission=tmsg.askquestion("User Confirmation","Are you sure you want to continue?")
        if (permission=='yes'):
            flow=True
            print(flow)
            content = self.content_text.get("1.0", tk.END)
            image_path1 = self.image_path.get()
            print(image_path1+"\n")
            Img1=image_path1.replace("/","\\")
            print(Img1)
            image_path2 = self.image_path2.get()
            print(image_path2+"\n")
            Img2=image_path2.replace("/","\\")
            print(Img2)
            print( content)
            webbrowser.open("https://www.facebook.com/", new = 0, autoraise = "true")
            start(content,Img1,Img2)
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('w')
            pyautogui.keyUp('w')
            pyautogui.keyUp('ctrl')
        
            
   
    def change_value(self):
        new_value = groups
        self.ids_text.delete(1.0, tk.END)  # Clear the current content
        for i in range (0,len(new_value)):
            if (i!=len(new_value)-1):
                x=new_value[i].strip()+","
            else:
                x=new_value[i].strip()
            self.ids_text.insert(tk.END, x)  # Insert the new value

    
    
    def add_IDs(self):
        
        content = self.url_text.get("1.0", tk.END)
        print( content)
        content=content.strip()
        temp=content.split(',')
        print(temp)
        file2 =open('groups.txt','w')
        for i in temp:
            x=i.split('/')
            p=len(x)-1
            if x[p] not in groups and x[p]!="" and x[p]!="\n":
                groups.append(x[p])
                file2.writelines(x[p]+'\n')
        file2.close()
        self.change_value()
        data()
        msg=str(len(groups))+" Groups were added for posting?"
        tmsg.showinfo("Groups Info",msg)
        
    def update_IDs(self):
        
        update_ids = self.ids_text.get("1.0", tk.END)
        print (update_ids)
        update_ids=update_ids.strip() 
        temp=update_ids.split(',')
        open('groups.txt', 'w').close()
        file3=open('groups.txt','w')
        print(temp)
        groups.clear()
        for i in temp:
            i=i.strip()
            i=i+"\n"
            if (i != '\n' and i!=""):
                groups.append(i)
                file3.writelines(i)
            
        print(groups)
        file3.close()
            

        self.change_value()
        data()
        msg=str(len(groups))+" Groups were updated for posting?"
        tmsg.showinfo("Groups Update",msg)
            

    def activate(self):
        webbrowser.open("https://www.facebook.com/", new = 0, autoraise = "true")
        time.sleep(3)
        pyautogui.keyDown('shift')
        pyautogui.keyDown('?')
        pyautogui.keyUp('?') 
        pyautogui.keyUp('shift') 
        time.sleep(3)
        for i in range (0,2):
            pyautogui.keyDown('tab')
            pyautogui.keyUp('tab')
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
        pyautogui.keyDown('escape')
        pyautogui.keyUp('escape')
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('w')
        pyautogui.keyUp('w')
        pyautogui.keyUp('ctrl')
    
    
    
    def schedule(self):
        time.sleep(1)
        while(True):
            self.post_to_facebook()           
            print("schedule\n")
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('w')
            pyautogui.keyUp('w')
            pyautogui.keyUp('ctrl')
            time.sleep(86400)
            

def main():
    data()
    root = tk.Tk()
    root.geometry('1300x650')    
    app = FacebookPostUI(root)    
    root.mainloop()   
     
    
    

if __name__ == "__main__":
    main()