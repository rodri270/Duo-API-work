from __future__ import absolute_import
from __future__ import print_function
import duo_client
import pprint
import csv
from six.moves import input
from keys import *
from itertools import repeat
import time
import sys

keyI = integration
keyS = secret


admin_api = duo_client.Admin(
    ikey=keyI,
    skey=keyS,
    host='api-302859b9.duosecurity.com',
    ca_certs='DISABLE'
)





def getUserPlusOffset():
    offsetValue = '300'
    csv_filename='responses.csv'
    with open(csv_filename, mode='a', newline="") as file:
        fieldnames = ['firstname', 'lastname', 'email', 'username', 'user_id','fullname'] 
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell()==0:
            writer.writeheader()
        
        
        
        getUserList = admin_api.json_api_call(
            'GET',
            '/admin/v1/users',
            {
                'limit':'300'
            }
        )

        for resp in getUserList:
            row = {
                'firstname': resp['firstname'],
                'lastname': resp['lastname'],
                'email': resp['email'],
                'username': resp['username'],
                'fullname': resp['realname'],
                'user_id': resp['user_id']
            }
            writer.writerow(row)
            print(f"CSV file '{csv_filename}' has been updated.")
        for i in repeat(None, 219):
            getUserListPlusOffset = admin_api.json_api_call(
                'GET',
                '/admin/v1/users',
                {
                    'limit':'300',
                    'offset': offsetValue
                }
            )
            
            for resp1 in getUserListPlusOffset:
                row = {
                    'firstname': resp1['firstname'],
                    'lastname': resp1['lastname'],
                    'email': resp1['email'],
                    'username': resp1['username'],
                    'fullname': resp1['realname'],
                    'user_id': resp1['user_id']
                }
                writer.writerow(row)
            print(f"CSV file '{csv_filename}' has been updated with offset data.")
            
            offsetValue = str(int(offsetValue)+300)
            
        

getUserPlusOffset()
print("File has been filled with all information exiting application in 5 seconds. ")
time.sleep(5)
sys.exit()
