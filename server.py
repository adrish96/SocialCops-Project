import subprocess
import os 

path=input("enter the path of the directory to share: ")
if not os.path.isdir(path):
	print("can't find the directory specified, try again.")
else:
	#subprocess.run(["mkdir","/root/Desktop/nfs"])
	subprocess.call("echo '{}  *(rw,sync,no_root_squash)' >> /etc/exports".format(path) , shell=True) 
	var=subprocess.call("systemctl restart nfs ",shell=True)
	if var==0:
		print("nfs directory  successfully created and shared using nfs " )

