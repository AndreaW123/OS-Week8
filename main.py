'''
Andrea Napoli-Wilson
CYBR
Week 8
10-5-2020
'''

import os

def main():
    dirName = input('The name of the directory you want to use : ')
#if directory does not exists then create it
    if not os.path.exists(dirName):	
        os.mkdir(dirName)

    fileName = input('Enter file name: ')

    name = input('Enter Name: ')
    address = input('Enter Address: ')
    phoneNumber = input('Enter Phone Number: ')

    with open(dirName+'/'+fileName, 'w') as f:	
        f.write(name.strip() + ',' + address.strip() + ',' + phoneNumber.strip() + '\n')	

    f = open(dirName+'/'+fileName, 'r')	

    name, address,  phoneNumber = f.read().split(',')	

    print('File added: ')
    print('Name: ', name)
    print('Address: ', address)
    print('Phone no: ', phoneNumber)
    f.close()	

if __name__ == '__main__':
    main()