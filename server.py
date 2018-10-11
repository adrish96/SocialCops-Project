import subprocess
import os 
subprocess.run(["mkdir","/root/Desktop/nfs"])
subprocess.call("echo '/root/Desktop/nfs  *(rw,no_root_squash)' >> /etc/exports" , shell=True)
var=subprocess.call("systemctl restart nfs ",shell=True)
if var==0:
	print("nfs directory  successfully created and shared using nfs " )
else :
	print("some error " ) 
