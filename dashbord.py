from tkinter import*
from PIL import Image,ImageTk
class mutual:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Fund Survey System")
        
        self.icon_title=PhotoImage(file="image/share logo.png")
        
        title=Label(self.root,text="Fund Survey System",image=self.icon_title ,compound=LEFT,font=("times new nroman",30,"bold"),bg="#010c48",fg="white",anchor="w",padx=15).place(x=0,y=0,relwidth=1,height=120)
        btn_logout=Button(self.root,text="Logout",font=("times new roman",13,"bold"),bg="orange",cursor="hand2").place(x=1150,y=10,height=30,width=175)
        
        self.lbi_clock=Label(self.root,text="Welcome to fund survey app\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new nroman",20),bg="#4d636d",fg="white")
        self.lbi_clock.place(x=0,y=130,relwidth=1,height=20)
        #==left Menu==
        self.menulogo=Image.open("image/menu logo.png")

        self.menulogo=self.menulogo.resize((40,40))
        self.menulogo=ImageTk.PhotoImage(self.menulogo)

        leftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        leftMenu.place(x=0,y=150,width=310,height=650)
        lbl_menulogo=Label(leftMenu,image=self.menulogo)
        lbl_menulogo.pack(side=TOP,fill=X)
        self.icon_side=PhotoImage(file="image/acc.png")
        
        lbl_menu=Label(leftMenu,text="Menu",font=("times new roman",12,),bg="grey").pack(side=TOP,fill=X)
        btn_Account_Det=Button(leftMenu,text="Account Details",image=self.icon_side,compound=LEFT,font=("times new roman",12,"bold"),bg="white").pack(side=TOP, fill=X)
        self.icon_side1=PhotoImage(file="image/wallet.png")
        btn_wallet_Det=Button(leftMenu,text="  $0.00 Stock  ",image=self.icon_side1,compound=LEFT,font=("times new roman",12,"bold"),bg="white").pack(side=TOP, fill=X)
        self.icon_side2=PhotoImage(file="image/All order.png")
        btn_Allorder_Det=Button(leftMenu,text="    All Orders   ",image=self.icon_side2,compound=LEFT,font=("times new roman",12,"bold"),bg="white").pack(side=TOP, fill=X)
        self.icon_side3=PhotoImage(file="image/bankdetails.png")
        btn_Bankdetails_Det=Button(leftMenu,text="  Bank Details ",image=self.icon_side3,compound=LEFT,font=("times new roman",12,"bold"),bg="white").pack(side=TOP, fill=X)
        self.icon_side4=PhotoImage(file="image/report.png")
        btn_report_Det=Button(leftMenu,text="     Report  ",image=self.icon_side4,compound=LEFT,font=("times new roman",12,"bold"),bg="white").pack(side=TOP, fill=X)

root=Tk()
obj=mutual(root)
root.mainloop()