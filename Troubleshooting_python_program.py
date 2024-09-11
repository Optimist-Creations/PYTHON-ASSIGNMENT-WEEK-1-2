import subprocess
import os
#Python program for troubleshooting fault in a computer
def check_network_adapter():
    print("Checking network adapter...")
    output = subprocess.check_output(["netsh", "interface", "ip", "show", "config"])
    print(output.decode())

def check_default_gateway():
    print("Checking default gateway...")
    output = subprocess.check_output(["route", "print", "0.0.0.0"])
    print(output.decode())

def check_ping_google():
    print("Pinging Google...")
    output = subprocess.check_output(["ping", "-n", "1", "(link unavailable)"])
    if output.decode().find("Reply from") != -1:
        print("Ping successful.")
    else:
        print("Ping failed.")

def check_ip_configuration():
    print("Checking IP configuration...")
    output = subprocess.check_output(["ipconfig", "/all"])
    print(output.decode())

def check_network_services():
    print("Checking network services...")
    services = ["dhcp", "dns", "netlogon"]
    for service in services:
        output = subprocess.check_output(["sc", "query", service])
        print(output.decode())

def restart_network_services():
    print("Restarting network services...")
    services = ["dhcp", "dns", "netlogon"]
    for service in services:
        subprocess.call(["sc", "stop", service])
        subprocess.call(["sc", "start", service])

def main():
    print("Network Connection Troubleshooter")
    print("-------------------------------")
    print("1. Check network adapter")
    print("2. Check default gateway")
    print("3. Ping Google")
    print("4. Check IP configuration")
    print("5. Check network services")
    print("6. Restart network services")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        check_network_adapter()
    elif choice == "2":
        check_default_gateway()
    elif choice == "3":
        check_ping_google()
    elif choice == "4":
        check_ip_configuration()
    elif choice == "5":
        check_network_services()
    elif choice == "6":
        restart_network_services()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
