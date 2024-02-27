# Import all the required libraries
import tkinter as tk

from tkcalendar import Calendar


# Create the Tkinter winder and insert the root file and create function
# for current date information
# add color in background and title box


def get_date():
    selected_date = cal.get_date()
    date_label.config(text="Selected Date: " + selected_date)


root = tk.Tk()
root.title("First GUI Calendar")
root.geometry("400x400")
root.configure(background="green")
sid = tk.Label(text="This is My first GUI Calendar", bg="dark gray", relief="sunken")
sid.place(relx=0.5, rely=0, anchor="n")

# Set the window size and create Calendar desk or menu.

root.wm_minsize(280, 280)
cal = Calendar(root, selectmode="day", date_pattern="dd-mm-yyyy")
cal.place(x=100,y=0)
# Adjust the Calendar window with fill pack function
cal.pack(pady=20,fill="both", expand=True)

#  Create a button to trigger date selection and link it to the get_date() function
select_button = tk.Button(root, text="Select Date", command=get_date,bg="red", relief="groove")
select_button.place(relx=0.5, rely=0.9, anchor="s")

# Create a label to display the selected date

date_label = tk.Label(root, text="")
date_label.pack(pady=20)

# Run the Tkinter and Calendar loop

root.mainloop()
