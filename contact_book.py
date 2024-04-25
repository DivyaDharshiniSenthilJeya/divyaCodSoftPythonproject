import sqlite3
import tkinter as tk
from tkinter import messagebox

# Connect to the database
conn = sqlite3.connect('contact.db')
c = conn.cursor()

# Create the contact table
c.execute('''CREATE TABLE IF NOT EXISTS contacts
             (NAME TEXT,
              PHONE TEXT,
              EMAIL TEXT,
              ADDRESS TEXT)''')
conn.commit()

# Define the function for adding contact information to the database
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    c.execute("INSERT INTO contacts (NAME, PHONE, EMAIL, ADDRESS) VALUES (?, ?, ?, ?)", (name, phone, email, address))
    conn.commit()
    messagebox.showinfo("Success", "Contact added successfully!")

def view_contacts():
    cursor = conn.execute("SELECT * FROM contacts")
    for row in cursor:
        print(f"Name: {row[0]}\nPhone: {row[1]}\nEmail: {row[2]}\nAddress: {row[3]}\n")

def delete_contact():
    name = name_entry.get()
    c.execute("DELETE FROM contacts WHERE NAME=?", (name,))
    conn.commit()
    messagebox.showinfo("Success", "Contact deleted successfully!")

# Create the GUI
root = tk.Tk()
root.title("Contact Book")

# Create the labels
name_label = tk.Label(root, text="Name:")
phone_label = tk.Label(root, text="Phone:")
email_label = tk.Label(root, text="Email:")
address_label = tk.Label(root, text="Address:")


# Create the entry widgets
name_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
email_entry = tk.Entry(root)
address_entry = tk.Entry(root)

# Create the buttons
add_button = tk.Button(root, text="Add contact", command=add_contact)
view_button = tk.Button(root, text="View contacts", command=view_contacts)
delete_button = tk.Button(root, text="Delete contact", command=delete_contact)

# Grid the labels, entry widgets, and buttons
name_label.grid(row=0, column=0)
phone_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
address_label.grid(row=3, column=0)

name_entry.grid(row=0, column=1)
phone_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
address_entry.grid(row=3, column=1)


add_button.grid(row=4, column=0)
view_button.grid(row=4, column=1)
delete_button.grid(row=4, column=2)

# Start the main loop
root.mainloop()

# Close the database connection
conn.close()
