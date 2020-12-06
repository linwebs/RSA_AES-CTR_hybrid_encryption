"""
Linwebs 2020.12
NCYU Information Security and Management
RSA + AES-CTR Encryption System
Needed: Python3 version
"""

import codecs
from pathlib import Path

from Crypto.PublicKey import RSA

key_file_path = "key/"
data_file_path = "text/"
rsa_key_file = key_file_path + "rsa_key"


def close_program():
	print("[狀態] 結束程式")
	exit()


def decryption():
	print("decryption")


def finish_generate_rsa_key():
	status = ""
	while status != "1":
		print("|+++++++++++++++++++++++++++++++++++++++++++++++|")
		print("| RSA 金鑰產生完畢                              \t|")
		print("| 公鑰檔案已儲存於 key 資料夾中的 rsa_key.pub 檔案  \t|")
		print("| 私鑰檔案已儲存於 key 資料夾中的 rsa_key.key 檔案  \t|")
		print("| -> 輸入 1 可返回主頁面                         \t|")
		print("|+++++++++++++++++++++++++++++++++++++++++++++++|")
		status = input()
		if status == "1":
			return True

	return False


def save_rsa_key(public_key, private_key):
	global rsa_key_file
	prv_file = rsa_key_file + ".key"
	pub_file = rsa_key_file + ".pub"

	Path(key_file_path).mkdir(parents=True, exist_ok=True)

	f = codecs.open(prv_file, "w", "utf_8")
	f.write(private_key.decode("utf-8"))
	f.close()

	f = codecs.open(pub_file, "w", "utf_8")
	f.write(public_key.decode("utf-8"))
	f.close()
	finish_generate_rsa_key()


def generate_rsa_key():
	print("[資訊] 金鑰產生中，請稍後...")
	new_key = RSA.generate(2048, e=65537)
	public_key = new_key.publickey().exportKey("PEM")
	private_key = new_key.exportKey("PEM")
	print("[狀態] 成功產生 RSA 2048 金鑰")
	save_rsa_key(public_key, private_key)


def show_welcome_msg():
	print("|+++++++++++++++++++++++++++++++++++++++|")
	print("| 歡迎使用 Linwebs RSA + AES-CTR 解密系統 \t|")
	print("| -> 輸入 1 執行解密程式                  \t|")
	print("| -> 輸入 2 產生 RSA 金鑰                \t|")
	print("| -> 輸入 3 離開程式                     \t|")
	print("| 註: 如需解密請執行 encryption 程式      \t|")
	print("|+++++++++++++++++++++++++++++++++++++++|")


def running_window():
	status = ""
	while status != "1":
		show_welcome_msg()
		status = input()

		if status == "1":
			decryption()

		elif status == "2":
			generate_rsa_key()

		elif status == "3":
			close_program()


if __name__ == '__main__':
	running_window()
