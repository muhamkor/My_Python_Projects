**README**

**Title:** Outlook Email Automation

**Description:** This is a Python script that can be used to send emails from Outlook. It uses the `win32com.client` library to interact with Outlook and the `csv` library to read data from a CSV file.

**Usage:**

1. Make sure you have Outlook installed on your computer
2. Clone the repository to your local machine.
3. Install the required Python libraries: `win32com.client` and `csv`.
4. Open the `file.csv` file and edit it to include your recipient's email.
5. Run the script from the command line:

```
python Outlook.py
```

This will send an email automatically. You can chose to display, save or send the email directly. The email's subject will be "This is my Subject" and the body will be "Hello, This is my email Body."

**Optional:**

You can also specify the email account that you want to use to send the email. To do this, uncomment the following line in the code:

```python
# optional (account you want to use to send the email)
# mailItem._oleobj_.Invoke(*(64209, 0, 8, 0, olNS.Accounts.Item('<email@gmail.com')))
```

Replace `<email@gmail.com>` with the email address of the account that you want to use.

**License:**

This code is licensed under the MIT License.
