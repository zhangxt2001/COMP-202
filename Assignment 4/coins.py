# Author: Xiaoteng Zhang
#McGill ID: 260895923

import requests
e_address = 'xiaoteng.zhang@mail.mcgill.ca'
personal_token = 'C49KOuYZofwXU7sY'

def dict_to_query(my_dict):
    '''dict->string
This function takes a dictionary as an input and returns a string
under a pre-specified format. 
>>>dict_to_query({'DOB':'20010423','AGE':'21'})
'DOB=20010423&AGE=21'
>>> dict_to_query({'DOB':'20010423','AGE':'21','GENDER':'Male'})
'DOB=20010423&AGE=21&GENDER=Male'
>>> dict_to_query({'Country':'England','Bestteam':'MAN-U'})
'Country=England&Bestteam=MAN-U'
'''
    query = ''
    key_list = list(my_dict.keys())
    val_list = list(my_dict.values())
    for i in range(len(my_dict)):
        query += str(key_list[i])+'='+str(val_list[i])
        if i != len(my_dict)-1:
            query += '&'
    return query

class Account:
    '''A class that stores all relevant data about a user's
COINBOT account and contain certain methods to operate that data
Instance Attribute:
*email(str)
*token(str)
*balance(int)
*request_log(list)
'''
    API_URL = 'https://coinsbot202.herokuapp.com/api/'
    
    def __init__(self,email,token):
        '''(str,str)->Account
This constructor assigns values into the objects being created.
When the inputting email doesn't end with mcgill.ca, we would raise
an AssertionError
>>> my_acct = Account("jonathan.campbell@mcgill.ca", "12345")
>>> my_acct.email
'jonathan.campbell@mcgill.ca'
>>> my_acct.token
'12345'
>>> sec_acc = Account("jonathan.campbell@utoronto.ca", "12345")
Traceback (most recent call last):
AssertionError: You just inputted the incorrect email address
'''
        if (type(email) != str) or (type(token) != str):
            raise AssertionError ("You've inputted the incorrect datatype")
        if (len(email)< 9) or (email[len(email)-9:] != 'mcgill.ca'):
            raise AssertionError ('You just inputted the incorrect email address')
        self.email = email
        self.token = token
        self.balance = -1
        self.request_log = []
        
    def __str__(self):
        '''()->str
This method that returns a string of the format 'EMAIL has balance BALANCE'.
>>> sec_acc = Account("xiaoteng.zhang@mail.mcgill.ca","12345")
>>> print(sec_acc)
xiaoteng.zhang@mail.mcgill.ca has balance -1
'''
        return self.email+' '+'has balance'+' '+str(self.balance)
    
    def call_api(self,endpt,my_dict):
        '''(str,dict)->dict
This method takes a endpoint and a dictionary and returns a dictionary corresponding
to the endpoint given. If any of the type or endpoint doesn't match what we expect,
an AssertionError would be raised. 
>>> my_account = Account(e_address,personal_token)
>>> my_account.call_api("balance", {'email': my_account.email})
{'message': 750, 'status': 'OK'}
>>>my_account.call_api("balanc", {'email': my_account.email})
Traceback (most recent call last):
AssertionError: Either the type of input is incorrect or the endpoint not valid
>>> my_account = Account(e_address,'20010423')
>>> my_account.call_api("balance", {'email': my_account.email})
AssertionError: The token in the API request did not match the token that was sent over Slack.
'''
        
        if not((type(endpt) == str) and (endpt in ['balance','transfer']) and (type(my_dict) == dict)):
            raise AssertionError('Either the type of input is incorrect or the endpoint not valid')
        my_dict['token'] = self.token
        req_str = endpt+'?'+dict_to_query(my_dict)
        request_url = self.API_URL+req_str
        result = requests.get(url=request_url).json()
        if result['status'] != 'OK':
            raise AssertionError(result['message'])
        else:
            return result
    
    def retrieve_balance(self):
        '''()->int
This function takes no implicit input and returns the balance of the account associated with
the email address provided. If the email address is incorrect, then nothing would be returned while
an AssertionError would be raised and the balance would stay at -1.
>>> my_account = Account(e_address,personal_token)
>>> my_account.retrieve_balance()
750
>>> my_account.balance
750
>>> type(my_account.balance)
<class 'int'>
>>> my_account_sec = Account('zhangxiaoteng@mcgill.ca',personal_token)
>>> my_account_sec.retrieve_balance()
Traceback (most recent call last):
AssertionError: No Slack account found for email zhangxiaoteng@mcgill.ca (API query field 'email').
Are you sure that is the email you used to signup to our Slack workspace?
'''
        balance_dict = self.call_api('balance',{'email':self.email})
        self.balance = balance_dict['message']
        return self.balance
    
    def transfer(self,amount,target_email):
        '''(int,str)->str
This method would transfer specified amount of coin to the target email specified.
Corresponding error message would be raised if one of the input is not what we expected.
>>> my_account = Account(e_address,personal_token)
>>> my_account.retrieve_balance()
750
>>> my_account.transfer(1,'jonathan.campbell@mcgill.ca')
'You have transferred 1 coins of your balance of 750 coins to jonathan.campbell. Your balance is now 749.'
>>> my_account.transfer(1,'jonathan.campbell@mcgill.cb')
Traceback (most recent call last):
AssertionError: Either the type of input is incorrect or the email address not valid
>>> my_account.transfer(0,'jonathan.campbell@mcgill.ca')
Traceback (most recent call last):
AssertionError: Either amount bigger than balance or amount inputted is less than 0
>>> my_account.transfer(1,'xiaoteng.zhang@mail.mcgill.ca')
Traceback (most recent call last):
AssertionError: Two emails cannot be the same
'''
        if not((type(amount) == int) and (type(target_email) == str) and (target_email[len(target_email)-9:] == 'mcgill.ca')):
            raise AssertionError('Either the type of input is incorrect or the email address not valid')
        if self.balance == -1:
            raise AssertionError("Account balance is -1")
        if (amount > self.balance) or (amount <= 0):
            raise AssertionError('Either amount bigger than balance or amount inputted is less than 0')
        if self.email == target_email:
            raise AssertionError("Two emails cannot be the same")
        my_dict = {}
        my_dict['withdrawal_email'] = self.email
        my_dict['token'] = self.token
        my_dict['deposit_email'] = target_email
        my_dict['amount'] = amount
        req_str = 'transfer'+'?'+dict_to_query(my_dict)
        request_url = self.API_URL+req_str
        result = requests.get(url=request_url).json()
        return result['message']