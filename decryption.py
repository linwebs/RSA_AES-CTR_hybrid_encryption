"""
Linwebs 2020.12
NCYU Information Security and Management
RSA + AES-CTR Encryption System
Needed: Python3 version
"""
import base64
import codecs
import sys
from binascii import hexlify
from pathlib import Path
from os import path

from Crypto.Util import Counter
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA

key_file_path = "key/"
data_file_path = "text/"
data_file = data_file_path + "input.txt"
cipher_file = data_file_path + "cipher.txt"
aes_key_encrypted_file = data_file_path + "aes_key.txt"
rsa_key_file = key_file_path + "rsa_key"
data_file = data_file_path + "output.txt"
rsa_private_key = ""
cipher_iv = ""
aes_key = ""
aes_key_encrypted = ""
output_data = ""


def close_program():
	print("[狀態] 結束程式")
	exit()


# step 1: load cipher from file
def load_cipher():
	global cipher_iv

	if path.exists(cipher_file):
		try:
			key = codecs.open(cipher_file, "r", "utf_8").read()
			cipher_iv = base64.b64decode(key)

		except:
			print("[錯誤] 密文檔讀取失敗，請執行 Encryption 程式重新進行加密")
			# print(sys.exc_info())
			return False

		print("[狀態] 成功載入密文檔")
		return True

	else:
		print("[錯誤] 密文檔 cipher.txt 不存在，請執行 Encryption 程式進行加密")
		return False


def load_aes_key():
	global aes_key_encrypted

	if path.exists(aes_key_encrypted_file):
		try:
			# print(aes_key_encrypted)
			key = codecs.open(aes_key_encrypted_file, "r", "utf_8").read()
			aes_key_encrypted = base64.b64decode(key)

		except:
			print("[錯誤] AES 金鑰加密檔讀取失敗，請執行 Encryption 程式重新進行加密")
			# print(sys.exc_info())
			return False

		print("[狀態] 成功載入 AES 金鑰加密檔")
		return True

	else:
		print("[錯誤] AES 金鑰加密檔 aes_key.txt 不存在，請執行 Encryption 程式進行加密")
		return False


def load_rsa_private_key():
	global rsa_private_key

	if path.exists(rsa_key_file + ".key"):
		try:
			key = codecs.open(rsa_key_file + ".key", "r", "utf_8").read()
			rsa_private_key = RSA.import_key(key)

		except:
			print("[錯誤] RSA 私鑰檔讀取失敗，請執行 Encryption 程式重新進行加密")
			# print(sys.exc_info())
			return False

		print("[狀態] 成功載入 RSA 2048 私鑰")
		return True

	else:
		print("[錯誤] RSA 私鑰不存在，請產生 RSA 金鑰後再執行 Encryption 程式進行加密")
		return False


# step 4: decrypt encrypted AES key using RSA private key
def decrypt_aes_key():
	global aes_key

	cipher_rsa = PKCS1_OAEP.new(rsa_private_key)
	aes_key = cipher_rsa.decrypt(aes_key_encrypted)
	# print(aes_key_encrypted)
	# print(aes_key)
	print("[狀態] AES 金鑰解密完成")


# step 5: decrypt cipher using AES key
def decrypt_cipher():
	global output_data

	block_size = 32
	aes_key_iv = cipher_iv[:16]
	ciphers = cipher_iv[16:]
	# print(aes_key_iv)
	# print(cipher_iv)
	# print(ciphers)
	ctr = Counter.new(128, initial_value=int(hexlify(aes_key_iv), 16))
	aes_cipher = AES.new(aes_key, AES.MODE_CTR, counter=ctr)

	result = b''

	for i in range(0, len(ciphers), block_size):
		block = bytes(ciphers[i:i + block_size])
		# print(block)
		result += aes_cipher.decrypt(block)

	output_data = result
	print("[狀態] 密文解密完成")


def save_data():
	output = output_data.decode("utf-8")
	f = codecs.open(data_file, "w", "utf_8")
	f.write(output)
	f.close()
	print("[狀態] 原文檔案儲存完成")


def finish_decrypt():
	status = ""
	while status != "1":
		print("|+++++++++++++++++++++++++++++++++++++++++++++++|")
		print("| 解密完畢                                      \t|")
		print("| 原文檔案已儲存於 text 資料夾中的 output.txt 檔案  \t|")
		print("| -> 輸入 1 可返回主頁面                         \t|")
		print("|+++++++++++++++++++++++++++++++++++++++++++++++|")
		status = input()

		if status == "1":
			return True

	return False


def decryption():
	# step 1: load cipher from file
	if not load_cipher():
		close_program()

	# step 2: load encrypted AES key from file
	if not load_aes_key():
		close_program()

	# step 3: load RSA private key from file
	if not load_rsa_private_key():
		close_program()

	# step 4: decrypt encrypted AES key using RSA private key
	decrypt_aes_key()

	# step 5: decrypt cipher using AES key
	decrypt_cipher()

	# step 6: save data to file
	save_data()

	# finish encrypt
	if finish_decrypt():
		return True


# finish decrypt

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
			if decryption():
				status = ""
			else:
				close_program()

		elif status == "2":
			generate_rsa_key()

		elif status == "3":
			close_program()


if __name__ == '__main__':
	running_window()
