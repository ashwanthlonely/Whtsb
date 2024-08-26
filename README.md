
 WhatsB - Bulk WhatsApp Messenger

 Overview

WhatsB is a Python-based application that allows users to send bulk WhatsApp messages to multiple recipients listed in an Excel file. The application features a simple user interface (UI) for ease of use and provides feedback on the status of each message sent.

 Features

- Send bulk WhatsApp messages to multiple recipients.
- Upload recipient numbers via an Excel file.
- Customize messages with a simple input box.
- Automatic handling of message delays:
  - 15-second delay between each message.
  - 1-hour delay after every 100 messages.
  - 24-hour delay after every 1000 messages.
- Resume from where it was stopped based on feedback status.
- Feedback on message status: Sent, Failed, In-Process.
- User-friendly interface created using Tkinter.
- Bundled as a standalone executable file (.exe) for easy deployment.



 Requirements

 Software

- Python 3.8+ (For development and if not using the executable)
- Excel (For managing the recipient list)
- WhatsApp Web (For sending messages)

 Python Libraries

- `pywhatkit`: For sending WhatsApp messages.
- `pandas`: For reading and processing Excel files.
- `tkinter`: For the GUI.
- `pyautogui`: For automating the closing of WhatsApp tabs.
- `time`: For handling delays.
- `pyinstaller`: For building the executable.

To install the required Python libraries, run:

```bash
pip install pywhatkit pandas pyautogui tk
```



 Installation

 Running the Application as a Python Script

1. Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/whatsb.git
   cd whatsb
   ```

2. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Application:
   ```bash
   python whatsapp_bulk_messenger.py
   ```

 Running the Application as an Executable

1. Download the Executable:
   - Download the latest version of `WhatsB.exe` from the [releases page]().

2. Run the Executable:
   - Double-click `WhatsB.exe` to launch the application.



 Usage

 Step 1: Uploading the Excel File

1. Prepare an Excel file with the following format:
   - Column A: `Mobile Number` (with country code, e.g., +1234567890).
   - Column B: `Feedback` (Leave this column empty; it will be populated by the application).

2. Upload the Excel file via the "Upload" button in the UI.

 Step 2: Customizing the Message

1. Enter your custom message in the text box provided in the UI.

 Step 3: Sending Messages

1. Click the "Send Messages" button to start sending messages.
2. The application will display a progress bar and update the "Feedback" column in the Excel file with the status of each message.

 Step 4: Handling Delays

- The application automatically handles delays:
  - 15-second delay between each message.
  - 1-hour delay after every 100 messages.
  - 24-hour delay after every 1000 messages.

 Step 5: Resuming from Stop

- If the application is stopped or closed, it will resume from where it left off by checking the "Feedback" column in the Excel file. Only unsent messages will be processed.



 Troubleshooting

 Common Issues

1. "The ordinal 380 could not be located in the dynamic link library" Error:
   - This error indicates a missing or incompatible DLL. Ensure all required DLLs are present in the executable’s directory or system path. Rebuild the executable if necessary.

2. Missing Dependencies:
   - If running from source, ensure all Python dependencies are installed. Use `pip install -r requirements.txt` to install them.

3. Delayed Message Sending:
   - The application is designed to include delays for WhatsApp’s anti-spam policies. This is intentional behavior.

4. WhatsApp Web Not Closing:
   - Ensure that the `pyautogui` library is correctly installed and has the necessary permissions to automate browser actions.

 Reporting Issues

If you encounter any issues, please report them [here](https://github.com/yourusername/whatsb/issues).



 Building from Source

 Creating an Executable with PyInstaller

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Build the Executable:
   ```bash
   pyinstaller --onefile --windowed --icon=icon.ico whatsapp_bulk_messenger.py
   ```

3. Move the Executable to a Distribution Folder:
   - PyInstaller will create a `dist` folder with the `WhatsB.exe` file.

4. Customizing the Build:
   - Add necessary DLLs or additional resources using the `--add-binary` or `--add-data` options.

 Adding an Icon

1. Include an icon file (e.g., `icon.ico`) in the project directory.
2. Use the `--icon=icon.ico` option when running PyInstaller to add the icon to the executable.

 Creating an Installer

To create an installer:

1. Use a tool like Inno Setup or NSIS to package your executable with all required files into a user-friendly installer.
2. Specify the destination folder for the installer to be separate from your source files.



 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



 Acknowledgments

- [PyWhatKit](https://github.com/Ankit404butfound/PyWhatKit) for WhatsApp messaging.
- [Pandas](https://pandas.pydata.org/) for data handling.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI.
- Created by Ashwanth.

