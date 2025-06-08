import argparse
import rarfile
from tqdm import tqdm
import os
import sys

def crack_rar(rar_path, wordlist_path):
    if not os.path.exists(rar_path):
        print(f"\n[ERROR] File RAR tidak ditemukan: {rar_path}")
        return
        
    if not os.path.exists(wordlist_path):
        print(f"\n[ERROR] Wordlist tidak ditemukan: {wordlist_path}")
        return

    try:
        rf = rarfile.RarFile(rar_path)
    except rarfile.NotRarFile:
        print(f"\n[ERROR] File bukan format RAR: {rar_path}")
        return
    except rarfile.RarCannotExec:
        print("\n[ERROR] UNRAR tidak terinstall. Download dari:")
        print("https://www.rarlab.com/rar_add.htm")
        return
    except Exception as e:
        print(f"\n[ERROR] Gagal membuka file RAR: {e}")
        return

    try:
        with open(wordlist_path, "r", errors="ignore", encoding="utf-8") as f:
            passwords = []
            for line in f:
                # Bersihkan karakter newline dan whitespace
                cleaned = line.strip()
                # Lewati baris kosong
                if cleaned: 
                    passwords.append(cleaned)
    except Exception as e:
        print(f"\n[ERROR] Gagal membaca wordlist: {e}")
        return

    print(f"\n[+] Memulai brute-force pada: {rar_path}")
    print(f"[+] Menggunakan wordlist: {wordlist_path}")
    print(f"[+] Jumlah password: {len(passwords):,}")
    print("[+] Tekan Ctrl+C untuk membatalkan\n")

    found = False
    try:
        for pwd in tqdm(passwords, desc="Testing passwords", unit=" password", file=sys.stdout):
            try:
                # Gunakan metode extractall() sebagai fallback
                rf.extractall(path=None, pwd=pwd)
                print(f"\n\n[SUKSES] Password ditemukan: '{pwd}'")
                found = True
                break
            except (rarfile.RarWrongPassword, rarfile.PasswordRequired):
                continue
            except rarfile.BadRarFile:
                # Skip file yang rusak
                continue
            except Exception as e:
                if "incorrect password" in str(e).lower():
                    continue
                print(f"\n[WARNING] Terjadi error dengan password '{pwd}': {e}")
                continue
    except KeyboardInterrupt:
        print("\n[!] Dihentikan oleh pengguna")
        return

    if not found:
        print("\n\n[GAGAL] Password tidak ditemukan dalam wordlist")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='RAR Password Cracker (Untuk Pemulihan Password Pribadi)',
        epilog="Contoh penggunaan: python rar_cracker.py -r fileku.rar -w rockyou.txt")
    
    parser.add_argument('-r', '--rarfile', 
                        required=True, 
                        help='Path ke file RAR terenkripsi')
    
    parser.add_argument('-w', '--wordlist', 
                        required=True, 
                        help='Path ke file wordlist (teks)')
    
    args = parser.parse_args()
    
    crack_rar(args.rarfile, args.wordlist)