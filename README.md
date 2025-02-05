# Ransomware Simulator

## 📌 Overview
This **Ransomware Simulator** is a safe demonstration of how ransomware operates. It encrypts files in a directory and provides a simulated ransom note. It also features **self-spreading** functionality to mimic real-world ransomware behavior.

## 🚀 Features
✔ **Encrypts files using AES encryption**  
✔ **Decrypts files if key is available**  
✔ **Generates a fake ransom note**  
✔ **Simulates self-spreading** (copies itself to another directory)  
✔ **Educational & non-malicious**

## 📦 Installation
### **1️⃣ Install Dependencies**
```bash
pip install cryptography
```

## 🛠 Usage
### **Run the script**
```bash
python ransomware_simulator.py
```

### **Provide Input**
1. **Choose Mode**:
   - `1` → Encrypt files
   - `2` → Decrypt files
2. **Enter Target Directory** – Specify the folder to encrypt/decrypt.

### **Example Output**
```
Choose mode (1: Encrypt, 2: Decrypt): 1
Enter directory path: /path/to/folder
[+] Encrypted: file1.txt
[+] Encrypted: file2.docx
[!] Ransom note created at /path/to/folder/RANSOM_NOTE.txt
[!] Ransomware copied to ~/Documents
```

## 🔓 Decrypting Files
1. Run the script in **decrypt mode**:
   ```bash
   python ransomware_simulator.py
   ```
2. Enter **mode 2 (Decrypt)**.
3. Provide the correct **encryption key** to restore files.

## 🛡️ Security & Prevention
- **Backup Important Files** regularly.
- **Do NOT run this on real data** (for educational use only).
- **Use Endpoint Security Solutions** to detect threats.

## ⚠️ Disclaimer
This tool is for **educational and security research purposes only**. **Do not deploy this on unauthorized systems**. Unauthorized use is **illegal**.

🔒 **Stay secure and ethical!**

