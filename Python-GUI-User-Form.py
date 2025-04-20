from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title("Practice Project with Webcode")
root.geometry("800x500+250+50")
root.configure(bg="#f0f0f0")

# ======= Title Bar =======
title = Label(root, text="User Entry Form", font=("Impact", 24, "bold"), bg="#212121", fg="white")
title.place(x=0, y=0, relwidth=1)

# ======= Functions =======
def get_data():
    if not var_username.get().strip():
        messagebox.showerror("Input Error", "Please enter your User Name.")
        return
    elif not var_email.get().strip():
        messagebox.showerror("Input Error", "Please enter your Email ID.")
        return
    elif var_age.get() == "Select Age":
        messagebox.showerror("Input Error", "Please select your Age.")
        return
    elif var_check.get() != 1:
        messagebox.showwarning("Terms & Conditions", "Please accept our Terms & Conditions.")
        return
    else:
        result = f"User Name: {var_username.get()}   |   Email ID: {var_email.get()}   |   Gender: {var_gender.get()}   |   Age: {var_age.get()}"
        messagebox.showinfo("Success", "Data collected successfully!")
        lbl_result.config(text=result, fg="green")

def reset_form():
    var_username.set("")
    var_email.set("")
    var_gender.set("Male")
    var_age.set("Select Age")
    var_check.set(0)
    lbl_result.config(text="")

# ======= Variables =======
var_username = StringVar()
var_email = StringVar()
var_gender = StringVar()
var_age = StringVar()
var_check = IntVar()

# ======= Labels & Widgets =======
Label(root, text="User Name:", font=("Calibri", 14), bg="#f0f0f0").place(x=50, y=80)
Entry(root, textvariable=var_username, font=("Calibri", 14)).place(x=200, y=80, height=30, width=500)

Label(root, text="Email ID:", font=("Calibri", 14), bg="#f0f0f0").place(x=50, y=130)
Entry(root, textvariable=var_email, font=("Calibri", 14)).place(x=200, y=130, height=30, width=500)

Label(root, text="Gender:", font=("Calibri", 14), bg="#f0f0f0").place(x=50, y=180)
Radiobutton(root, text="Male", value="Male", variable=var_gender, font=("Calibri", 13), bg="#f0f0f0").place(x=200, y=180)
Radiobutton(root, text="Female", value="Female", variable=var_gender, font=("Calibri", 13), bg="#f0f0f0").place(x=300, y=180)
var_gender.set("Male")

Label(root, text="Age:", font=("Calibri", 14), bg="#f0f0f0").place(x=50, y=230)
age_combo = ttk.Combobox(root, values=[str(i) for i in range(18, 80)], textvariable=var_age, font=("Calibri", 13), state="readonly")
age_combo.place(x=200, y=230, height=30, width=150)
age_combo.set("Select Age")

Checkbutton(root, text="Accept our Terms and Conditions", onvalue=1, offvalue=0, variable=var_check, font=("Calibri", 12), bg="#f0f0f0").place(x=200, y=280)

# ======= Buttons =======
Button(root, text="SHOW DATA", command=get_data, font=("Calibri", 13, "bold"), bg="#333", fg="white", cursor="hand2").place(x=250, y=330, height=35, width=150)
Button(root, text="RESET", command=reset_form, font=("Calibri", 13, "bold"), bg="#666", fg="white", cursor="hand2").place(x=420, y=330, height=35, width=150)

# ======= Result Label =======
lbl_result = Label(root, text="", font=("Calibri", 14), bg="#f0f0f0")
lbl_result.place(x=0, y=400, relwidth=1)

root.mainloop()
