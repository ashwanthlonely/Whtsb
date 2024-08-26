import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import pywhatkit as kit
import time
import pyautogui as pag
import os

# Function to close the current WhatsApp Web tab
def close_whatsapp_tab():
    time.sleep(5)  # Give it some time to send the message
    pag.hotkey('ctrl', 'w')  # This closes the current tab

# Function to send WhatsApp messages
def send_whatsapp(file_path, message):
    df = pd.read_excel(file_path)

    if 'Mobile Number' not in df.columns:
        messagebox.showerror("Error", "Excel file must contain 'Mobile Number' column.")
        return

    total_numbers = len(df)
    for index, row in df.iterrows():
        mobile_number = row['Mobile Number']
        
        try:
            kit.sendwhatmsg_instantly(f"+{mobile_number}", message, wait_time=20)
            close_whatsapp_tab()  # Close the WhatsApp tab after sending the message
            df.at[index, 'Feedback'] = "Sent"
        except Exception as e:
            df.at[index, 'Feedback'] = f"Failed: {str(e)}"
        
        time.sleep(5)  # Delay of 5 seconds between each message
        
        if (index + 1) % 100 == 0 and (index + 1) < total_numbers:
            time.sleep(300)  # Delay of 5 minutes after every 100 messages

    # Save the updated Excel file with feedback
    df.to_excel(file_path, index=False)
    messagebox.showinfo("Success", "WhatsApp messages sent successfully!")

# Function to handle file selection
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        file_label.config(text=os.path.basename(file_path))
        app.file_path = file_path

# Function to handle message sending
def on_send_click():
    message = message_entry.get("1.0", tk.END).strip()
    if not hasattr(app, 'file_path') or not message:
        messagebox.showwarning("Input Required", "Please select an Excel file and enter a message.")
        return

    send_whatsapp(app.file_path, message)

# Initialize the Tkinter application
app = tk.Tk()
app.title("WhatsApp Bulk Messenger")

# UI Elements
tk.Label(app, text="Select Excel File:").pack(pady=10)
file_label = tk.Label(app, text="No file selected", fg="grey")
file_label.pack()

tk.Button(app, text="Browse", command=select_file).pack(pady=5)

tk.Label(app, text="Enter Message:").pack(pady=10)
message_entry = tk.Text(app, height=5, width=50)
message_entry.pack()

tk.Button(app, text="Send Messages", command=on_send_click).pack(pady=20)

# Run the application
app.mainloop()
