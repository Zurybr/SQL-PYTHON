from tkinter import *
from tkinter import messagebox
import pymysql
class InferfasGraficaRegistro:
    def __init__(self):
        self.root=Tk()
        self.root.title('Base de Datos de Zurybr')
        self.root.resizable(width=False, height=False)
        self.frame=Frame(self.root)
        self.frame.pack()
        id=IntVar()
        username=StringVar()
        password=StringVar()
        email=StringVar()
        firstname=StringVar()
        lastname=StringVar()

        self.label1=Label(self.frame, text="ID:",justify='right')
        self.label1.grid(row=1,column=1,padx=10,pady=10)
        self.entry1=Entry(self.frame,justify='right',textvariable=id)
        self.entry1.grid(row=1,column=2,padx=10,pady=10)

        self.label2=Label(self.frame, text="Username:")
        self.label2.grid(row=2,column=1,padx=10,pady=10)
        self.entry2=Entry(self.frame,justify='right',textvariable=username)
        self.entry2.grid(row=2,column=2,padx=10,pady=10)

        self.label3=Label(self.frame, text="password:")
        self.label3.grid(row=3,column=1,padx=10,pady=10)
        self.entry3=Entry(self.frame,justify='right',textvariable=password,show="*")
        self.entry3.grid(row=3,column=2,padx=10,pady=10)

        self.label4=Label(self.frame, text="email:")
        self.label4.grid(row=4,column=1,padx=10,pady=10)
        self.entry4=Entry(self.frame,justify='right',textvariable=email)
        self.entry4.grid(row=4,column=2,padx=10,pady=10)

        self.label5=Label(self.frame, text="First Name:")
        self.label5.grid(row=5,column=1,padx=10,pady=10)
        self.entry5=Entry(self.frame,justify='right',textvariable=firstname)
        self.entry5.grid(row=5,column=2,padx=10,pady=10)

        self.label6=Label(self.frame, text="Last Name:")
        self.label6.grid(row=6,column=1,padx=10,pady=10)
        self.entry6=Entry(self.frame,justify='right',textvariable=lastname)
        self.entry6.grid(row=6,column=2,padx=10,pady=10)
        self.root.mainloop()

class InterfasGraficaLog:

    def __init__(self):
        self.root=Tk()
        self.root.title('Login')
        self.root.resizable(width=False, height=False)
        self.frame=Frame(self.root)
        self.frame.pack()
        host=StringVar()
        users=StringVar()
        passw=StringVar()
        db=StringVar()

        self.label1=Label(self.frame, text="Host:",justify='right')
        self.label1.grid(row=1,column=1,padx=10,pady=10)
        self.entry1=Entry(self.frame,justify='right',textvariable=host)
        self.entry1.grid(row=1,column=2,padx=10,pady=10)

        self.label2=Label(self.frame, text="User:")
        self.label2.grid(row=2,column=1,padx=10,pady=10)
        self.entry2=Entry(self.frame,justify='right',textvariable=users)
        self.entry2.grid(row=2,column=2,padx=10,pady=10)

        self.label3=Label(self.frame, text="password:")
        self.label3.grid(row=3,column=1,padx=10,pady=10)
        self.entry3=Entry(self.frame,justify='right',textvariable=passw,show="*")
        self.entry3.grid(row=3,column=2,padx=10,pady=10)

        self.label4=Label(self.frame, text="Bas de Datos:")
        self.label4.grid(row=4,column=1,padx=10,pady=10)
        self.entry4=Entry(self.frame,justify='right',textvariable=db)
        self.entry4.grid(row=4,column=2,padx=10,pady=10)
        button1=Button(self.frame, text='Enviar', width=3,command=lambda:self.guardarDatos(host.get(),
        users.get(),
        passw.get(),
        db.get()))
        button1.grid(row=5,column=0,columnspan=2)
        self.root.mainloop()


    def guardarDatos(self,host,users,passw,db):

        self.host=host
        self.users=users
        self.passw=passw
        self.db=db
        DataBase(self.host,self.users,self.passw,self.db)

class DataBase(InterfasGraficaLog):
    def __init__(self,host,users,passw,db):
        print('establecioendo coneccion...')
        try:
            self.connection=pymysql.connect(
            host='{}'.format(host),
            user='{}'.format(users),
            password='{}'.format(passw),
            db='{}'.format(db)
            )
            self.cursor=self.connection.cursor()
            self.connection.autocommit(True)
            messagebox.showinfo(message="conexion establecida", title="Ya lo tienes")
            InferfasGraficaRegistro()
        except Exception as e:
            messagebox.showinfo(message="algo salio mal, comprueba los datos", title="Ups!")
            raise

DB=InterfasGraficaLog()


'''
sql3.freemysqlhosting.net
sql3419553
kvYRt9fxg6
sql3419553
'''
