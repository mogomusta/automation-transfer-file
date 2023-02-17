from ftplib import FTP
import shutil
import os
import schedule
import time


myHost = '127.0.0.1'
myUsername = 'mogo'
myPassword = '123456'
local_dir = r"C:\Users\dell\Desktop\localserver\\"
source_folder = r"C:\Users\dell\Desktop\automation_project\\"

# connet to the server
ftp = FTP(host=myHost, user=myUsername, passwd=myPassword)


def transfer():
    for file_name in os.listdir(source_folder):
        source = source_folder + file_name
        destination = local_dir + file_name
        if os.path.isfile(source):
            shutil.copy(source, destination)
            print('moved: ' + file_name)
        else:
            print('Error occured during copying files')


schedule.every(20).seconds.do(transfer)
while True:
    schedule.run_pending()
    time.sleep(5)
    break
