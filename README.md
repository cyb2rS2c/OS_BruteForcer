# OS Bruteforcer

A Python automation tool for **OS detection** and **login attempts** using `nmap`, `hydra`, and `xfreerdp/sshpass`.  
Designed for **educational and authorized penetration testing** only.

---

## Features
- Detects target OS (Windows / macOS) via `nmap`
- Performs automated brute-force attacks with `hydra`
  - RDP for Windows targets
  - SSH for macOS targets
- Connects automatically on successful login:
  - `xfreerdp` for Windows
  - `sshpass` for macOS
- Flexible password file path (no hardcoded directories)

---

## Project Tree
```
.
├── assets
│   └── pass.txt
├── LICENSE
├── README.md
├── requirements.txt
├── setup.sh
└── src
    ├── animation.py
    └── OS_Bruteforcer.py
```


## Usage

1-Clone the repository:
```sh
git clone https://github.com/cyb2rS2c/OS_BruteForcer.git
cd OS_BruteForcer
```
2-Run the script:
```sh
chmod +x setup.sh;source ./setup.sh
```
3-Follow the prompts:

- Enter the target IP (Windows or macOS)
- The script uses pass.txt in the ```assets/``` folder by default.
- You can replace pass.txt or modify the script to use a custom wordlist.

## Screenshots
<img width="604" height="187" alt="image" src="https://github.com/user-attachments/assets/467ba3eb-7800-4638-9613-7480554a11d2" />

## Disclaimer
This tool is intended only for educational purposes and authorized penetration testing.
Do not use it on systems you do not own or have explicit permission to test.

## Author
cyb2rS2c - [GitHub Profile](https://github.com/cyb2rS2c)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
