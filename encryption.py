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
from os import path
from pathlib import Path

from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA

key_file_path = "key/"
data_file_path = "text/"
data_file = data_file_path + "input.txt"
cipher_file = data_file_path + "cipher.txt"
aes_key_encrypted_file = data_file_path + "aes_key.txt"
rsa_key_file = key_file_path + "rsa_key"
rsa_public_key = ""
aes_key = ""
aes_key_iv = ""
aes_key_encrypted = ""
input_data = ""
cipher = ""


def close_program():
	print("[狀態] 結束程式")
	exit()


# step 1: load RSA public key
def load_rsa_public_key():
	global rsa_key_file, rsa_public_key

	pub_file = rsa_key_file + ".pub"

	if path.exists(pub_file):
		try:
			key = codecs.open(pub_file, "r", "utf_8").read()
			rsa_public_key = RSA.import_key(key)
		# print("[資訊] RSA 公鑰: ")
		# print(rsa_public_key)

		except:
			print("[錯誤] RSA 公鑰讀取失敗，請執行 decryption 程式重新產生 RSA 金鑰")
			# print(sys.exc_info())
			return False

		return True

	else:
		print("[錯誤] RSA 公鑰不存在，請執行 decryption 程式產生 RSA 金鑰")
		return False


# step 2: generate AES key
def generate_aes_key():
	global aes_key, aes_key_iv

	aes_key = get_random_bytes(16)
	aes_key_iv = get_random_bytes(16)
	print("[狀態] 成功產生 AES 金鑰")


# step 3: input data
def input_data_msg():
	status = ""
	while status != "1":
		if not path.exists(data_file_path):
			Path(data_file_path).mkdir(parents=True, exist_ok=True)

		print("|+++++++++++++++++++++++++++++++++++++++|")
		print("| 加密程式執行中                        \t|")
		print("| 請將要加密的檔案放置於 text 資料夾中，   \t|")
		print("| 並將檔案名稱命名為 input.txt，         \t|")
		print("| 放置完畢                             \t|")
		print("| -> 輸入 1 繼續執行程式                \t|")
		print("| -> 輸入 2 可返回上一步                \t|")
		print("|+++++++++++++++++++++++++++++++++++++++|")
		status = input()
		if status == "1":
			return True
		elif status == "2":
			return False


# step 3: input data
def load_data():
	global input_data

	if path.exists(data_file):
		input_data = codecs.open(data_file, "r", "utf_8").read().encode(encoding="utf-8")
		return True
	else:
		print("[錯誤] input.txt 檔案不存在，請重新放置後再繼續執行程式")
		return False


# step 4: encrypt data using AES key
def encrypt_data():
	global cipher

	block_size = 32
	ctr = Counter.new(128, initial_value=int(hexlify(aes_key_iv), 16))
	aes_cipher = AES.new(aes_key, AES.MODE_CTR, counter=ctr)

	result = b''

	for i in range(0, len(input_data), block_size):
		block = bytes(input_data[i:i + block_size])
		# print(block)
		result += aes_cipher.encrypt(block)

	cipher = result


# print(base64.b64encode(result).decode("utf-8"))


# step 5: encrypt AES key use RSA public key
def encrypt_aes_key():
	global aes_key_encrypted

	cipher_rsa = PKCS1_OAEP.new(rsa_public_key)
	aes_key_encrypted = cipher_rsa.encrypt(aes_key)

	print("[狀態] AES 金鑰加密完成")


# step 6: save cipher data to file
def save_cipher():
	Path(data_file_path).mkdir(parents=True, exist_ok=True)

	cipher_iv = aes_key_iv + cipher
	# print(aes_key_iv)
	# print(cipher_iv)
	# print(cipher)
	out_cipher = base64.b64encode(cipher_iv).decode(encoding="utf-8")
	f = codecs.open(cipher_file, "w", "utf_8")
	f.write(out_cipher)
	f.close()

	print("[狀態] 密文儲存完成")


# step 7: save encrypted AES key to file
def save_encrypted_aes_key():
	Path(data_file_path).mkdir(parents=True, exist_ok=True)

	out_key = base64.b64encode(aes_key_encrypted).decode(encoding="utf-8")
	f = codecs.open(aes_key_encrypted_file, "w", "utf_8")
	f.write(out_key)
	f.close()
	# print(aes_key_encrypted)
	# print(out_key)
	# print(aes_key)


def finish_encrypt():
	status = ""
	while status != "1":
		print("|+++++++++++++++++++++++++++++++++++++++++++++++++++++++|")
		print("| 加密完畢                                             \t|")
		print("| 密文檔案已儲存於 text 資料夾中的 cipher.txt 檔案         \t|")
		print("| AES金鑰加密檔已儲存於 text 資料夾中的 aes_key.txt 檔案  \t|")
		print("| -> 輸入 1 可返回主頁面                                \t|")
		print("|+++++++++++++++++++++++++++++++++++++++++++++++++++++++|")
		status = input()

		if status == "1":
			return True

	return False


def encryption():
	# step 1: load RSA public key
	if not load_rsa_public_key():
		return False

	# step 2: generate AES key
	generate_aes_key()

	# step 3: input data
	if not input_data_msg():
		return True
	if not load_data():
		return True

	# step 4: encrypt data using AES key
	encrypt_data()

	# step 5: encrypt AES key use RSA public key
	encrypt_aes_key()

	# step 6: save cipher data to file
	save_cipher()

	# step 7: save encrypted AES key to file
	save_encrypted_aes_key()

	# finish encrypt
	if finish_encrypt():
		return True


def show_welcome_msg():
	print("|+++++++++++++++++++++++++++++++++++++++|")
	print("| 歡迎使用 Linwebs RSA + AES-CTR 加密系統 \t|")
	print("| -> 輸入 1 執行加密程式                  \t|")
	print("| -> 輸入 2 離開程式                     \t|")
	print("| 註: 如需解密請執行 decryption 程式      \t|")
	print("|+++++++++++++++++++++++++++++++++++++++|")


def running_window():
	status = ""
	while status != "1":
		show_welcome_msg()
		status = input()

		if status == "1":
			if encryption():
				status = ""
			else:
				close_program()

		elif status == "2":
			close_program()


if __name__ == '__main__':
	running_window()
