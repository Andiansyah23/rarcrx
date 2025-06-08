# **RARCRX - RAR Password Recovery Tool** 🔓  

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)  
![License](https://img.shields.io/badge/license-MIT-green)  
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)  

**RARCRX** is a Python-based tool designed to help you recover lost passwords for **RAR archives** using dictionary attacks. **For legal and ethical use only!**  

---

## **⚠️ Important Disclaimer**  
🚨 **This tool is intended ONLY for recovering passwords from RAR files that you own and have legal rights to access.**  
🚨 **Unauthorized cracking of password-protected files is illegal and unethical.**  
🚨 **The developer is not responsible for any misuse of this software.**  

---

## **✨ Features**  
✔ **Dictionary Attack** – Uses custom wordlists to guess passwords  
✔ **Fast & Efficient** – Optimized password testing with progress tracking  
✔ **Cross-Platform** – Works on Windows, Linux, and macOS  
✔ **Simple CLI** – Easy-to-use command-line interface  
✔ **Supports RAR 3.x & 4.x** – Compatible with most RAR encryption formats  

---

## **🛠 Installation**  

### **1. Install Python Dependencies**  
```bash
pip install rarfile tqdm
```

### **2. Install UnRAR Utility**  
#### **Windows**  
Download [UnRAR from RARLab](https://www.rarlab.com/rar_add.htm) and add it to your **PATH**.  

#### **Linux (Debian/Ubuntu)**  
```bash
sudo apt update && sudo apt install unrar
```  

#### **macOS (Homebrew)**  
```bash
brew install unrar
```  

---

## **🚀 Usage**  

### **Basic Command**  
```bash
python rarcrx.py -r <encrypted.rar> -w <wordlist.txt>
```  

### **Example**  
```bash
python rarcrx.py -r secret.rar -w rockyou.txt
```  

### **Arguments**  
| Argument | Description | Example |
|----------|-------------|---------|
| `-r`, `--rarfile` | Path to encrypted RAR file | `-r myfile.rar` |
| `-w`, `--wordlist` | Path to password wordlist | `-w passwords.txt` |

---

## **📂 Wordlist Format**  
- Plain text file (`.txt`)  
- One password per line  
- Supports UTF-8 encoding  
- Example:  
  ```
  password123  
  admin  
  123456  
  mySecurePass  
  ```

---

## **📊 Sample Output**  
```
[+] Starting brute-force on: secret.rar  
[+] Using wordlist: rockyou.txt  
[+] Total passwords: 14,344,392  
[+] Press Ctrl+C to cancel  

Testing passwords:  15%|██████████▌         | 2.1M/14.3M [05:32<31:10, 6.5K password/s]  

[✅] SUCCESS! Password found: "password123"  
```  

---

## **🔍 Tips for Better Results**  
🔹 **Use large wordlists** (e.g., `rockyou.txt`, `SecLists`)  
🔹 **Try common password variations** (e.g., `password` → `P@ssw0rd`)  
🔹 **Combine words with numbers/symbols** (e.g., `admin` → `admin123!`)  
🔹 **If no password is found**, try a different wordlist  

---

## **❓ FAQ**  

### **❔ Why is it slow?**  
➡️ Speed depends on CPU power and password complexity.  

### **❔ Does it work with RAR5?**  
➡️ **No**, this tool only supports traditional RAR encryption (RAR 3.x & 4.x).  

### **❔ What if no password is found?**  
➡️ Try a **larger wordlist** or **customize passwords** you might have used.  

---

## **🤝 Contributing**  
Contributions are welcome!  
1. **Fork** the repository  
2. Create a **feature branch** (`git checkout -b new-feature`)  
3. **Commit** your changes (`git commit -am 'Add new feature'`)  
4. **Push** to the branch (`git push origin new-feature`)  
5. Open a **Pull Request**  

---

## **📜 License**  
This project is licensed under **MIT License** - see [LICENSE](LICENSE) for details.  

---

### **🔐 Use Responsibly!**  
This tool is for **legal password recovery only**. Always respect privacy and digital rights. 🛡️
