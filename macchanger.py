import subprocess
from optparse import OptionParser

def Parser():
    parser=OptionParser()
    parser.add_option("-i" , "--interface",dest="interface",help="interface to change it's mac address")
    parser.add_option("-m" , "--mac",dest="mac",help="enter the new mac address")

    (options,argument)=parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify a Interface")
    elif not options.mac:
        parser.error('[-] Please Specify The Mac Address')
    return options

def mac_changer(interface,mac):
    print(f"[+] Changing MAC Address for {interface} to {mac}")
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])
option=Parser()
mac_changer(option.interface,option.mac)




