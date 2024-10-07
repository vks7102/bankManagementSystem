import tkinter as tk

class bank():
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Login")
        scr_width =self.root.winfo_screenwidth()
        scr_height =self.root.winfo_screenheight()
        self.root.geometry(f"{scr_width}x{scr_height}+0+0")

        mainlable = tk.Label(self.root, text="Welcome to ABC Bank", font=("Arial", 40, "bold"), bg="light green", bd=5, relief="groove")
        mainlable.pack(side="top", fill="x")

        adminFrame = tk.Frame(self.root, bg="light grey", bd = 5, relief="ridge")
        adminFrame.place(x=400,y=90,width=450, height=550)

        mainlable = tk.Label(adminFrame, text="Login as", font=("Arial", 40, "bold"), bg="light green", bd=5, relief="groove")
        mainlable.grid(row=0,column=0,padx=40,pady=50)

        adminBtn = tk.Button(adminFrame, text="Admin Login",width=20,bg="light blue", bd=3, relief="raised", font=("Arial", 20, "bold"))
        adminBtn.grid(row=1,column=0,padx=40,pady=50)

        branchBtn = tk.Button(adminFrame, text="Branch Login",width=20,bg="light blue", bd=3, relief="raised", font=("Arial", 20, "bold"))
        branchBtn.grid(row=2,column=0,padx=40,pady=50)

        accBtn = tk.Button(adminFrame, text="Account Login",width=20,bg="light blue", bd=3, relief="raised", font=("Arial", 20, "bold"))
        accBtn.grid(row=3,column=0,padx=40,pady=50)

        accopnBtn = tk.Button(adminFrame, text="Account Login",width=20,bg="light blue", bd=3, relief="raised", font=("Arial", 20, "bold"))
        accopnBtn.grid(row=4,column=0,padx=40,pady=50)

root = tk.Tk()
obj = bank(root)
root.mainloop()