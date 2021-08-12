'''
Created on Mar 6, 2016

@author: Bill Begueradj
'''

import tkinter

class Begueradj(tkinter.Frame):
    '''Define a GUI for membership subscription.    
    '''
    def __init__(self, parent):
        '''Set the constructor.
        Set the parent Frame widget.
        Call initialize_membership_interface() to draw the GUI
        '''
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_membership_interface()

    def initialize_membership_interface(self):
        ''' Draw a simplistic GUI consisting of 2 buttons.
        The user clicks on the sign up button to land on the second
        window dedicated for the subscription process.
        The user may click on the cancel button to leave 
        the application.
        '''
        self.parent.title('Membership Area')
        self.parent.grid_rowconfigure(0, weight = 1)
        self.parent.grid_columnconfigure(0, weight = 1)
        self.parent.config(background = "lavender")    

        self.label_welcome = tkinter.Label(self.parent,text="Not a member? Please sign up: ",anchor=tkinter.W,background="dark slate gray",foreground="white", font="Helvetica 8  bold")
        self.label_welcome.grid(row = 0, columnspan = 2, stick = tkinter.E + tkinter.W)

        self.button_signup = tkinter.Button(self.parent,font="Helvetica 10 bold", text = "Sign up", command = self.signup)
        self.button_signup.grid(row = 1, column = 0, sticky = tkinter.E + tkinter.W)
        self.button_cancel_signup = tkinter.Button(self.parent,text = "Cancel",font="Helvetica 10 bold", command = self.parent.quit)
        self.button_cancel_signup.grid(row = 1, column = 1, sticky = tkinter.E + tkinter.W)

    def signup(self):
        '''Design the subscription window.
        Bind this child window to the main one using tkinter.Toplevel()
        '''
        self.signup_window = tkinter.Toplevel(self)
        self.signup_window.wm_title("Sign up Area")
        self.signup_window.grid_rowconfigure(0, weight = 1)
        self.signup_window.grid_columnconfigure(0, weight = 1)
        # Member's first name
        self.label_firstname = tkinter.Label(self.signup_window,text="First name: ",anchor=tkinter.W,background="dark slate gray",foreground="white", font="Helvetica 8  bold")
        self.label_firstname.grid(row = 0, column = 0, stick = tkinter.E + tkinter.W)
        self.entry_firstname = tkinter.Entry(self.signup_window)
        self.entry_firstname.grid(row = 0, column = 1)
        # Member's last name
        self.label_lastname = tkinter.Label(self.signup_window,text="Last name: ", anchor=tkinter.W,background="dark slate gray",foreground="white", font="Helvetica 8  bold")
        self.label_lastname.grid(row = 1, column = 0, stick = tkinter.E + tkinter.W)
        self.entry_lastname = tkinter.Entry(self.signup_window)
        self.entry_lastname.grid(row = 1, column = 1)
        # Member's email
        self.label_email = tkinter.Label(self.signup_window,text="Email: ", anchor=tkinter.W,background="dark slate gray",foreground="white", font="Helvetica 8  bold")
        self.label_email.grid(row = 2, column = 0, stick = tkinter.E + tkinter.W)
        self.entry_email = tkinter.Entry(self.signup_window)
        self.entry_email.grid(row = 2, column = 1)
        # Member's password
        self.label_password = tkinter.Label(self.signup_window,text="Password: ",anchor=tkinter.W,background="dark slate gray",foreground="white", font="Helvetica 8  bold")
        self.label_password.grid(row = 3, column = 0, stick = tkinter.E + tkinter.W)
        self.entry_password = tkinter.Entry(self.signup_window, show = "*")
        self.entry_password.grid(row = 3, column = 1)        
        # Member's repeat password
        self.label_repeat_password = tkinter.Label(self.signup_window,text="Repeat password: ",anchor=tkinter.W,background="dark slate gray",foreground="white", font="Helvetica 8  bold")
        self.label_repeat_password.grid(row = 4, column = 0, stick = tkinter.E + tkinter.W)
        self.entry_repeat_password = tkinter.Entry(self.signup_window, show = "*")
        self.entry_repeat_password.grid(row = 4, column = 1)

        self.button_submit = tkinter.Button(self.signup_window,text="Submit",font="Helvetica 10 bold")
        self.button_submit.grid(row = 5, column = 0, sticky = tkinter.E + tkinter.W)
        self.button_cancel_submit = tkinter.Button(self.signup_window,text = "Cancel",font="Helvetica 10 bold", command = self.parent.quit)
        self.button_cancel_submit.grid(row = 5, column = 2, sticky = tkinter.E + tkinter.W)

def main():
    root = tkinter.Tk()
    b = Begueradj(root)
    b.mainloop()
# Start of the main program
if __name__ == "__main__":
    main()