#!usr/bin/env python3

import subprocess
import optparse

class bcolors:
    WARNING = '\033[93m'
    ENDC = '\033[0m'

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Specify the interface")
parser.add_option("-m", "--mac", dest="new_mac", help="Target MAC Address")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC of interface " + interface + " to " + new_mac)

subprocess.run(["ip", "link", "set", "dev", interface, "down"])
subprocess.run(["ip", "link", "set", "dev", interface, "address", new_mac])
subprocess.run(["ip", "link", "set", "dev", interface, "up"])

print(f"{bcolors.WARNING}[>] MAC Address Successfully changed{bcolors.ENDC}")

