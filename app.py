import pywhatkit as kit
import pandas as pd
import time
import pyautogui as pag

# Load the Excel file
file_path = 'Campign.xlsx'  # Replace with your actual file path
df = pd.read_excel(file_path)

# Function to update the Feedback column
def update_status(index, status):
    df.at[index, 'Feedback'] = status
    df.to_excel(file_path, index=False)  # Save the Excel file

# Function to close the current WhatsApp Web tab
def close_whatsapp_tab():
    time.sleep(5)  # Give it some time to send the message
    pag.hotkey('ctrl', 'w')  # This closes the current tab

# Send WhatsApp messages
def send_bulk_whatsapp():
    total_numbers = len(df)
    msg=input("Your custom message here: ")
    for index, row in df.iterrows():
        mobile_number = row['Mobile Number']
        message = msg  # Customize this message
        
        try:
            kit.sendwhatmsg_instantly(f"+{mobile_number}", message, wait_time=20)
            close_whatsapp_tab()  # Close the WhatsApp tab after sending the message
            update_status(index, "Sent")
        except Exception as e:
            update_status(index, f"Failed: {str(e)}")
        
        time.sleep(5)  # Delay of 5 seconds between each message
        
        if (index + 1) % 100 == 0 and (index + 1) < total_numbers:
            time.sleep(300)  # Delay of 5 minutes after every 100 messages

send_bulk_whatsapp()
