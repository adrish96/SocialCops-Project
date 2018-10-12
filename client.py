import os
import subprocess

ip=input("enter IP of server: ")

var=os.popen("sudo showmount -e {}".format(ip))  #show folder shared on the server
var1=var.read()
point=var1.splitlines()
mountpoint=point[1][:-2]  #parsing the path of the folder on the server

#userpath="/root/Desktop/nfsshare"

userpath=input("enter folder to sync(it should be an empty folder): ")
if userpath is []:
	subprocess.call("sudo mount -t nfs {}:{} {}".format(ip,mountpoint,userpath),shell=True)
	print("folder is mounted successfully and is now in sync!")
else:
	print("the folder is not empty, please try again.")


