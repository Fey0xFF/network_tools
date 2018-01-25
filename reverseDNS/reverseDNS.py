import os
import socket
os.path.join('home','ubuntant','Desktop')
os.chdir('/home/ubuntant/Desktop')

print(os.getcwd())
rawIPList = open('iplist.txt', 'r')
iplist = (rawIPList.read()).split()

print(iplist)

ipRes = open("ipresolved.txt", "w+")

print("**********PRINTING JUST HOST NAMES**********")
for i in iplist:
	try:
		hostname = socket.gethostbyaddr(i.rstrip())
		print(hostname[2], hostname[0])
		ipRes.write("Entry: %s %s \n" % (hostname[2], hostname[0]))
	except socket.herror:
		print("***IP resolution failed for:" + i + ". See error note at end of log.")
		ipRes.write("IP resolution failed for:" + i + ". See error note at end of log.\n")


print('\nError note: IP resolution failed. Possibly an invalid PTR, reverse DNS not configured, private/dynamically shared address.')
ipRes.write('\nError note: IP resolution failed. Possibly an invalid PTR, reverse DNS not configured, private/dynamically shared address.')
ipRes.close()