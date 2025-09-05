# OS Bruteforcer

A Python automation tool for **OS detection** and **login attempts** using `nmap`, `hydra`, and `xfreerdp/sshpass`.  
Designed for **educational and authorized penetration testing** only.

---

## ✨ Features
- Detects target OS (Windows / macOS) via `nmap`
- Performs automated brute-force attacks with `hydra`
  - RDP for Windows targets
  - SSH for macOS targets
- Connects automatically on successful login:
  - `xfreerdp` for Windows
  - `sshpass` for macOS
- Flexible password file path (no hardcoded directories)
- Animated ASCII banner with author signature

---

## 📦 Requirements
- Python 3
- [nmap](https://nmap.org/)
- [hydra](https://github.com/vanhauser-thc/thc-hydra)
- [xfreerdp](https://www.freerdp.com/) (for Windows targets)
- [sshpass](https://linux.die.net/man/1/sshpass) (for macOS targets)
- [figlet](http://www.figlet.org/) *(optional, for banner)*

Python dependencies:
```bash
pip install colorama
```

## 🚀 Usage

1-Clone the repository:
```sh
git clone https://github.com/cyb2rS2c/OS_BruteForcer.git
cd OS_BruteForcer
```
2-Run the script:
```sh
sudo python3 OS_Bruteforcer.py
```
3-Follow the prompts:

- Enter the target IP (Windows or macOS)
- The script uses pass.txt in the repo folder by default.
- You can replace pass.txt or modify the script to use a custom wordlist.



## Educational Purposes

This project is intended for educational purposes only. The code demonstrates how to interact with system commands and network interfaces via Python. Do not use this toolkit for unauthorized or illegal network activities. Always obtain proper authorization before testing network security.

## 📝 Author
cyb2rS2c - [GitHub Profile](https://github.com/cyb2rS2c)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer
This tool is intended only for educational purposes and authorized penetration testing.
Do not use it on systems you do not own or have explicit permission to test.
