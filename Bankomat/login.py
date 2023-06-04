import tkinter as tk
from tkinter import messagebox


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

      
        self.configure(background="#66CD00")
        title_font = ("Arial", 36, "bold")
        label_font = ("Arial", 24)
        entry_font = ("Arial", 24)

       
        self.heading_label = tk.Label(self, text="PRIJAVA", font=title_font, background="#66CD00", fg="white")
        self.heading_label.pack(pady=40)

       
        self.username_label = tk.Label(self, text="Korisnicko ime:", font=label_font, background="#66CD00", fg="white")
        self.username_label.pack()
        self.username_entry = tk.Entry(self, font=entry_font)
        self.username_entry.pack()

        
        self.password_label = tk.Label(self, text="Lozinka:", font=label_font, background="#66CD00", fg="white")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*", font=entry_font)
        self.password_entry.pack()

        
        self.login_button = tk.Button(self, text="Prijava", font=label_font, command=self.login, bg="#008000", fg="black")
        self.login_button.pack(pady=20)

       
        self.signup_button = tk.Button(self, text="Registracija", font=label_font, command=self.signup, bg="#32CD32", fg="black")
        self.signup_button.pack()

        self.pack(fill="both", expand=True)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        login(username, password)

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        sign_up(username, password)


def read_credentials():
    credentials = {}
    try:
        with open('nalozi.txt', 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                credentials[username] = password
    except FileNotFoundError:
        return {}
    return credentials


def write_credentials(credentials):
    with open('nalozi.txt', 'w') as file:
        for username, password in credentials.items():
            file.write(f'{username},{password}\n')


def sign_up(username, password):
    credentials = read_credentials()
    if username in credentials:
        messagebox.showerror("Registracija greska", "Korisnicko ime vec postoji.")
    else:
        credentials[username] = password
        write_credentials(credentials)
        messagebox.showinfo("Registracija uspesna", "Registracija uspesna. Molim ulogujte se.")


def login(username, password):
    credentials = read_credentials()
    if username not in credentials or credentials[username] != password:
        messagebox.showerror("Prijava greska", "Netacno korisnicko ime ili lozinka.")
    else:
        messagebox.showinfo("Uspesna prijava", "Prijava uspesna.")
        app.destroy()


if __name__ == "__main__":
    app = tk.Tk()
    app.title("Prijava")
    app.geometry("1100x700")
    app.resizable(False, False)
    app.configure(background="#66CD00")

    login_page = LoginPage(app, None)

    app.mainloop()
