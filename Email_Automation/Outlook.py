# Import the required libraries
# win32com.client is used to interact with Outlook
import win32com.client as win32
import csv

def getsendto():
  """Returns the sender's email address from the CSV file."""
  with open('file.csv', 'r') as maillistcsv:
    emaillist = csv.reader(maillistcsv)
    next(emaillist)
    for email in emaillist:
      email = email[0]
      return email

def getccto():
  """Returns the CC email address from the CSV file."""
  with open('file.csv', 'r') as maillistcsv:
    emaillist = csv.reader(maillistcsv)
    next(emaillist)
    for email in emaillist:
      email = email[1]
      return email

outlookapp = win32.Dispatch('Outlook.Application')
# Create an Outlook application object

outlookNS = outlookapp.GetNameSpace('MAPI')
# Get the user's namespace

mailItem = outlookapp.CreateItem(0)
# Construct an email item object

mailItem.Subject = 'This is my Subject'
# Set the email's subject

mailItem.BodyFormat = 1
# Set the email's body format to HTML

mailItem.Body = '''Hello, 

This is my email Body

'''
# Set the email's body

mailItem.To = getsendto()
# Set the email's recipient to the user's name from the CSV file

#mailItem.CC = getccto()
# Set the email's CC recipient to the user's manager's name from the CSV file

mailItem.Sensitivity  = 2
# Set the email's sensitivity to confidential

# optional (account you want to use to send the email)
# mailItem._oleobj_.Invoke(*(64209, 0, 8, 0, outlookNS.Accounts.Item('<email@gmail.com')))

mailItem.Display()
# Display the email before sending it

# mailItem.Save()
# Save the email

# mailItem.Send()
# Send the email

