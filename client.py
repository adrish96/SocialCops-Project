import os
import subprocess
#ip=input("enter IP of server: ")
ip="192.168.102.150"

var=os.popen("sudo showmount -e {}".format(ip))
var1=var.read()
point=var1.splitlines()
mountpoint=point[1][:-2]
#userpath="/root/Desktop/nfsshare"
userpath=input("enter folder to sync: ")
subprocess.call("sudo mount -t nfs {}:{} {}".format(ip,mountpoint,userpath),shell=True)



