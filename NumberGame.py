from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import random

#CREATING DATABASE
mydb=mysql.connector.connect(host='localhost',user='root',passwd='root',database='numbergame_database')

mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE game_name (name VARCHAR(255),address VARCHAR(255),email VARCHAR(255),phone INT(10),user_id INT AUTO_INCREMENT PRIMARY KEY)")

root=Tk()
root.resizable(0,0)
root.geometry('400x400')
root.title("Number Guessing Game")
root.config(bg="red")

global score
score=0

icon_img=Image.open("C:\\Users\\faraz\\PycharmProjects\\Tkinter\\Number Guessing\\main.png")
icon_img=icon_img.resize((200,200),Image.ANTIALIAS)
icon_img=ImageTk.PhotoImage(icon_img)

icon_img_label=Label(image=icon_img,borderwidth=0)
icon_img_label.grid(row=0,column=0,pady=20,padx=(100,0))

login_btn_image=Image.open("C:\\Users\\faraz\\PycharmProjects\\Tkinter\\Number Guessing\\button.png")
login_btn_image=login_btn_image.resize((50,50),Image.ANTIALIAS)
login_btn_image=ImageTk.PhotoImage(login_btn_image)

def login_window():
    root.destroy()
    global login
    login=Tk()
    login.resizable(0,0)
    login.title("Login")
    login.geometry('500x300')
    login.config(bg="white")

    frame=LabelFrame(login,pady=5)
    frame.pack()

    name_label=Label(frame,text="Name")
    name_label.grid(row=0,column=0,padx=(50,150))
    phone_label=Label(frame,text="Phone")
    phone_label.grid(row=1,column=0,padx=(50,150))
    email_label=Label(frame,text="Email")
    email_label.grid(row=2,column=0,padx=(50,150))
    address_label=Label(frame,text="Address")
    address_label.grid(row=3,column=0,padx=(50,150))

    entry_name=Entry(frame)
    entry_name.grid(row=0,column=1,padx=(0,50))
    phone_name = Entry(frame)
    phone_name.grid(row=1,column=1,padx=(0,50))
    email_name = Entry(frame)
    email_name.grid(row=2,column=1,padx=(0,50))
    address_name = Entry(frame)
    address_name.grid(row=3,column=1,padx=(0,50))


    def clear_fields():
        entry_name.delete(0,END)
        phone_name.delete(0, END)
        email_name.delete(0, END)
        address_name.delete(0,END)

    def new_game_window():
        global game
        game = Tk()
        game.resizable(0, 0)
        game.geometry("600x200")

        new_game()
        game.mainloop()

    def destroy_button():

        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        new_game()

    def new_game():
        global randomnum_ans,option2,option3
        randomnum_ans=random.randint(1,100)
        global btn1,btn2,btn3
        print(randomnum_ans)
        option2 = random.randint(1, 100)
        option3 = random.randint(1, 100)

        def checkans(answer):

            if(answer== randomnum_ans):
                global score
                score+=1

            btn1.config(bg="green")
            btn2.config(bg="red")
            btn3.config(bg="red")


        btn1=Button(game,text=randomnum_ans,command=lambda: checkans(randomnum_ans),font=("Helvetica",35),bg="white")
        btn2=Button(game,text=option2,command=lambda: checkans(option2),font=("Helvetica",35),bg="white")
        btn3=Button(game,text=option3,command=lambda: checkans(option3),font=("Helvetica",35),bg="white")

        global score
        print(score)

        placement1=random.randint(0,3)
        placement2_column=[i for i in range(0,3) if i not in [placement1]]
        placement2=placement2_column[0]
        placement3_column = [i for i in range(0, 3) if i not in [placement2,placement1]]
        placement3=placement3_column[0]


        print(placement1,placement2,placement3)
        btn1.grid(row=0,column=placement1,padx=10,pady=10)
        btn2.grid(row=0,column=placement2,padx=10,pady=10)
        btn3.grid(row=0,column=placement3,padx=10,pady=10)

        def score_game():
            response=messagebox.showinfo("Score",f"Your Score is {score}")

        btn4=Button(game,text="My Score",bg="red",command=score_game)
        btn4.grid(row=1,column=1)
        btn5=Button(game,text="Next",bg="red",command=destroy_button)
        btn5.grid(row=1,column=0)
        btn6=Button(game,text="Exit",bg="red",command=game.destroy)
        btn6.grid(row=1,column=2)


    def add_user():
        sql_command="INSERT INTO game_name(name,address,email,phone) VALUES (%s,%s,%s,%s)"
        values=(entry_name.get(),address_name.get(),email_name.get(),phone_name.get())
        mycursor.execute(sql_command,values)
        mydb.commit()
        clear_fields()
        login.destroy()
        new_game_window()


    btn_logup=Button(frame,text="Logup",command=add_user)
    btn_logup.grid(row=4,column=0,sticky=E,pady=(20,5))

    login.mainloop()

btn_signin=Button(root,image=login_btn_image,command=login_window,borderwidth=0)
btn_signin.grid(row=1,column=0,sticky=W,padx=(130,0))

exit_btn_image=Image.open("C:\\Users\\faraz\\PycharmProjects\\Tkinter\\Number Guessing\\exit.png")
exit_btn_image=exit_btn_image.resize((50,50),Image.ANTIALIAS)
exit_btn_image=ImageTk.PhotoImage(exit_btn_image)

btn_exit=Button(root,image=exit_btn_image,command=root.quit,borderwidth=0)
btn_exit.grid(row=1,column=0,sticky=E,padx=(0,50))



root.mainloop()