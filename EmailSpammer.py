import csv



'''
This contains a class for an email spammer. Which you can use to send email spams
'''

class EmailSpammer:
    
    email_list = []
    def __init__(self):

        
        print('initializing class')

        # self.email_list = []

    def gather_emails_from_excel(self, excel_file_path):
        print('Gathering Emails')









if __name__ == "__main__":

    print("Hello, World")

    es = EmailSpammer()
    es.gather_emails_from_excel('test.xlsx')

