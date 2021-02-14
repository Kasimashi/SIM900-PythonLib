#!/usr/bin/python3
import sys
from Send_sms import Sending

if __name__ == '__main__':

    my_dict = {}
    for arg in sys.argv[1:]:
        key, val = arg.split(':')[0], arg.split(':')[1]
        my_dict[key] = val

    for key in my_dict.keys():
        print("Send SMS to",key," Content : ",my_dict.get(key))
        Sending(key,my_dict.get(key))

