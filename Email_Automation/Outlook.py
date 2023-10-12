import win32com.client as win32
import csv
# Import the required libraries
# win32com.client is used to interact with Outlook
# nusacsv is used to get the user's name and manager's name from a CSV file
'''
This is being created as a function for the cvs files to be readed and data being extracted from the files.
'''
def getuser():
    with open('nusa.csv', 'r') as nusacsv:
        nusa = csv.reader(nusacsv)
        next(nusa)
        for line in nusa:
            line = line[1]
            return line
def getmanager():
    with open('nusa.csv', 'r') as nusacsv:
        nusa = csv.reader(nusacsv)
        next(nusa)
        for line in nusa:
            line = line[2]
            return line

olApp = win32.Dispatch('Outlook.Application')
# Create an Outlook application object

olNS = olApp.GetNameSpace('MAPI')
# Get the user's namespace

mailItem = olApp.CreateItem(0)
# Construct an email item object

mailItem.Subject = 'This is my Subject'
# Set the email's subject

mailItem.BodyFormat = 1
# Set the email's body format to HTML

mailItem.Body = '''Hello, 

This is my email Body

'''
# Set the email's body

mailItem.To = getuser()
# Set the email's recipient to the user's name from the CSV file

mailItem.CC = getmanager()
# Set the email's CC recipient to the user's manager's name from the CSV file

mailItem.Sensitivity  = 2
# Set the email's sensitivity to confidential

# optional (account you want to use to send the email)
# mailItem._oleobj_.Invoke(*(64209, 0, 8, 0, olNS.Accounts.Item('<email@gmail.com')))

#mailItem.Display()
# Display the email before sending it

# mailItem.Save()
# Save the email

# mailItem.Send()
# Send the email

