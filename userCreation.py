from __future__ import absolute_import
from __future__ import print_function
import pprint
import sys
import json
#import pandas as pd
import csv
import base64, email.utils, hmac, hashlib, urllib
import duo_client
from six.moves import input
from keys import *


admin_api = duo_client.Admin(
    ikey=integration,
    skey=secret,
    host='api-302859b9.duosecurity.com',
    ca_certs='DISABLE'
)

createUserBulk = admin_api.json_api_call(
    'POST',
    '/admin/v1/users/bulk_create',
    {
        'users':json.dumps([

			
			{
				                'username': 'example_username_397_',
			},
			{
				                'username': 'example_username_398_',
			},
			{
				                'username': 'example_username_399_',
			},
			{
				                'username': 'example_username_400_',
			},
			{
				                'username': 'example_username_401_',
			},
			{
				                'username': 'example_username_402_',
			},
			{
				                'username': 'example_username_403_',
			},
			{
				                'username': 'example_username_404_',
			},
			{
				                'username': 'example_username_405_',
			},
			{
				                'username': 'example_username_406_',
			},
			{
				                'username': 'example_username_407_',
			},
			{
				                'username': 'example_username_408_',
			},
			{
				                'username': 'example_username_409_',
			},
			{
				                'username': 'example_username_410_',
			},
			{
				                'username': 'example_username_411_',
			},
			{
				                'username': 'example_username_412_',
			},
			{
				                'username': 'example_username_413_',
			},
			{
				                'username': 'example_username_414_',
			},
			{
				                'username': 'example_username_415_',
			},
			{
				                'username': 'example_username_416_',
			},
			{
				                'username': 'example_username_417_',
			},
			{
				                'username': 'example_username_418_',
			},
			{
				                'username': 'example_username_419_',
			},
			{
				                'username': 'example_username_420_',
			},
			{
				                'username': 'example_username_421_',
			},
			{
				                'username': 'example_username_422_',
			},
			{
				                'username': 'example_username_423_',
			},
			{
				                'username': 'example_username_424_',
			},
			{
				                'username': 'example_username_425_',
			},
			{
				                'username': 'example_username_426_',
			},
			{
				                'username': 'example_username_427_',
			},
			{
				                'username': 'example_username_428_',
			},
			{
				                'username': 'example_username_429_',
			},
			{
				                'username': 'example_username_430_',
			},
			{
				                'username': 'example_username_431_',
			},
			{
				                'username': 'example_username_432_',
			},
			{
				                'username': 'example_username_433_',
			},
			{
				                'username': 'example_username_434_',
			},
			{
				                'username': 'example_username_435_',
			},
			{
				                'username': 'example_username_436_',
			},
			{
				                'username': 'example_username_437_',
			},
			{
				                'username': 'example_username_438_',
			},
			{
				                'username': 'example_username_439_',
			},
			{
				                'username': 'example_username_440_',
			},
			{
				                'username': 'example_username_441_',
			},
			{
				                'username': 'example_username_442_',
			},
			{
				                'username': 'example_username_443_',
			},
			{
				                'username': 'example_username_444_',
			},
			{
				                'username': 'example_username_445_',
			},
			{
				                'username': 'example_username_446_',
			},
			{
				                'username': 'example_username_447_',
			},
			{
				                'username': 'example_username_448_',
			},
			{
				                'username': 'example_username_449_',
			},
			{
				                'username': 'example_username_450_',
			},
			{
				                'username': 'example_username_451_',
			},
			{
				                'username': 'example_username_452_',
			},
			{
				                'username': 'example_username_453_',
			},
			{
				                'username': 'example_username_454_',
			},
			{
				                'username': 'example_username_455_',
			},
			{
				                'username': 'example_username_456_',
			},
			{
				                'username': 'example_username_457_',
			},
			{
				                'username': 'example_username_458_',
			},
			{
				                'username': 'example_username_459_',
			},
			{
				                'username': 'example_username_460_',
			},
			{
				                'username': 'example_username_461_',
			},
			{
				                'username': 'example_username_462_',
			},
			{
				                'username': 'example_username_463_',
			},
			{
				                'username': 'example_username_464_',
			},
			{
				                'username': 'example_username_465_',
			},
			{
				                'username': 'example_username_466_',
			},
			{
				                'username': 'example_username_467_',
			},
			{
				                'username': 'example_username_468_',
			},
			{
				                'username': 'example_username_469_',
			},
			{
				                'username': 'example_username_470_',
			},
			{
				                'username': 'example_username_471_',
			},
			{
				                'username': 'example_username_472_',
			},
			{
				                'username': 'example_username_473_',
			},
			{
				                'username': 'example_username_474_',
			},
			{
				                'username': 'example_username_475_',
			},
			{
				                'username': 'example_username_476_',
			},
			{
				                'username': 'example_username_477_',
			},
			{
				                'username': 'example_username_478_',
			},
			{
				                'username': 'example_username_479_',
			},
			{
				                'username': 'example_username_480_',
			},
			{
				                'username': 'example_username_481_',
			}
        ])
    }
)

pprint.pprint(createUserBulk)