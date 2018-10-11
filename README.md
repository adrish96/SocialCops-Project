## Internship application project at SocialCops
The task given basically boiled down to syncing a folder across two different computers so that changes made to the folder on one computer is reflected on the folder on the other computer as well.
The first thing that came to my mind upon coming across this problem was using `rsync` or `unison` which are software's used to solve exactly this issue, however I decided to make something of my own.

The problem can be solved by using the `NFS` or `Samba` Protocol. The approach I used was:
1) Set up a `NFS` server and share a folder (conider this Droid 1)
2) On a different computer (Droid 2), mount the shared folder
Now we have a folder that is synced across both the devices, any changes to the directory or the constituent files is reflected across all devices which have the mounted share.

Another approach can be setting up a server and connecting two different clients to it and name them Droid 1 & Droid 2.

`NFS` approach works for all UNIX based or UNIX-like systems (I tested the code on RHEL and Ubuntu), to add access to Windows, `SMB` Protocol should be used.

To run the code:
run `python3 server.py` and set up the share
next, run `python3 client.py` on a different system, let the code do the rest.
