# 資訊安全與管理 作業 2 1.2
RSA + AES-CBC 混合式加密系統
https://hackmd.io/@linwebs-ncyu/Sk4EKk5ov
> Linwebs 2020.12
> NCYU Information Security and Management

## 目錄
[TOC]

## 題目
Cryptographic Primitives for C++/.NET/Java/Python
The followings are some popular packages for Cryptography:

1. Please apply **two** packages (each encryption mode for one package) to implement the **hybrid encryption**: RSA + AES-CBC and RSA + AES-CTR. You should encrypt plaintext les into ciphertext les, and then decrypt them. Observe and analyze your output results.

Jave RSA + AES-CTR

## 環境
* 程式語言: Python
* 建置平台: PyCharm
* Python 執行版本: 3.x
* 使用函式庫
	* base64 [Base64 編碼解碼]
	* codecs [檔案讀寫]
	* sys [except 錯誤訊息]
	* binascii [bytes 格式化]
	* pathlib [資料夾建立]
	* os [檔案路徑檢查]
	* Crypto.Random [取得隨機 bytes]
	* Crypto.Util [Counter]
	* Crypto.Cipher [AES、RSA]
	* Crypto.PublicKey [RSA]

## 使用說明
1. 請先執行 Decryption.java 產生 RSA 金鑰
2. 執行 Encryption.java 進行加密
3. 執行 Decryption.java 進行解密

※ 請確保擁有執行程式當層資料夾及子資料夾的讀寫權限
※ 請確保讀入的文字檔案編碼為 UTF-8 不帶簽名

## 系統架構
![encrypt_flow_graph](https://img.linwebs.tw/ewoce)
![decrypt_flow_graph](https://img.linwebs.tw/clekj)

## 程式流程

### 加密流程
| 步驟 | 加密端 | 解密端 |
| ---- | --- | --- |
| 1. |  | 產生 RSA 2048 公鑰、私鑰 |
| 2. |  | 將 RSA 2048 公鑰、私鑰儲存到檔案 |
| 3. | 從檔案讀取 RSA 2048 公鑰 |  |
| 4. | 產生 AES 128 金鑰 |  |
| 5. | 從檔案讀取原文資料 |  |
| 6. | 使用 AES 金鑰加密原文資料成密文 |  |
| 7. | 使用 RSA 公鑰加密 AES 金鑰成被加密的 AES 金鑰 |  |
| 8. | 將密文儲存到檔案 |  |
| 9. | 將被加密的 AES 金鑰儲存到檔案 |  |
| 10. | 完成加密 |  |

### 解密流程
| 步驟 | 加密端 | 解密端 |
| ---- | --- | --- |
| 1. |  | 從檔案讀取密文 |
| 2. |  | 從檔案讀取被加密的 AES 金鑰 |
| 3. |  | 從檔案讀取 RSA 私鑰 |
| 4. |  | 使用 RSA 私鑰解密被加密的 AES 金鑰 |
| 5. |  | 使用解密完成的 AES 解密密文成原文 |
| 6. |  | 儲存解密後的原文資料到檔案 |
| 7. |  | 完成解密 |

## 檔案結構
* README.md [說明檔]
* encryption.py [加密]
* decryption.py [解密、生成 RSA 金鑰]
* text [資料夾]
	* input.txt [原文純文字檔案]
	* aes_key.txt [AES 256 金鑰加密檔]
	* cipher.txt [加密後的密文檔]
	* output.txt [解密後的純文字檔案]
* key [資料夾]
	* rsa_key.key [RSA 2048 私鑰檔]
	* rsa_key.pub [RSA 2048 公鑰檔]

## 執行結果
1. 執行 decryption.py 產生 RSA 金鑰

![python_gen_rsa_key](https://img.linwebs.tw/rycda)

2. 執行 encryption.py 進行加密

![python_encrypt](https://img.linwebs.tw/fuzrg)

3. 執行 decryption.py 進行解密

![python_decrypt](https://img.linwebs.tw/isyrc)


## 執行結果分析
以下檔案取自某次的執行結果
* 原文純文字檔案 input.txt
```
0123456789
echo 'Hello World!'
哈囉世界
```

* 解密後的純文字檔案 output.txt
```
0123456789
echo 'Hello World!'
哈囉世界
```

* AES 128 金鑰加密檔 aes_key.txt
```
JhZEgDlWl439HQ0q/7CNQjYZJLBkmW3PBYQO55T6IjwLHHpSnTbt0qgAY7TmF2XBmuCFnD9TbJ8EsUMDb4nTC6ewDfju3+R6/hRwGhYxEP5o920mTHXGFkOiXxRd23WmYVTT7VJ2HZn7BFSUUTqxNgCjI0ehWdXKLyqh0FPszhy/uxqGY3B0SMQ1gBwsq2RoXLEhSTaxWzm8FOjg6XFXagjH3FpqJhSH+gW9IGQSY5dtZH1ISzUzSLHR8SOKz5R3Rd7f5aRvZaqR6j2y2FaPguyUD8kDQMQZFyVPX/Y1Nw9HYHAHAalEEpM6LjKFc2vUFnRvCCvbqQp7AdJXQ94l3w==
```

* 加密後的密文檔 cipher.txt
```
P35sQdzk/1t5ubODj8HmACdapJ1kKG/vsRkVzo++Z0TpD3NoxxQlPmEsZyrEqmhMc4hTs+Dw7crnxejZFw==
```

* RSA 2048 私鑰檔 rsa_key.key
```
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAy+MUa1EiiheiZz+I77Pewt8SB2f2NaysabdxXMtJhX/6R9aG
q8I+gFFrvQ9BtK5g5LSoXjfsJpIF5TZ1TPIJRwnN1PRzDsJyar/wsB3+bFHOeLBg
yVhBcQJ0yXstLhbQb64CEBg6kizHTuGRnB5P4shNpNwaC1Nr0+oTnAsP1doG47PK
eUdYyRBj40jfztxXT8wXnMzTY1ZJQDjov32nndTURGHlabidmboJbn18zsbGJ6BA
sHWokmL7dF6ao2bFH5BMP0APEVMVm3K/1jD5ehkJN4paZnaIDXAbKVHKwjccjIzY
go2UjKtdcMAYqQy3UmkdzIUQy+sJkmxe+VywbwIDAQABAoIBAFzrHvWvstGDZuiu
DG7NpyJhfjpw10Tr7mF5kEjtfpLAWeRecN6bNlfNg4/Uganh5NemO6tAyjdjyhsF
oBzSm4bMAYnhZARgeruKwRrKeJaOC851944bUiu6JlZidBsym4iiIV+LYzoV/TlG
VNF1AQxGJBiTlKz/tj8MSSaO5gcbtlklDW2rn3mMVzHSJg6Adv/1inpCoUSWRFMU
14pgrRsxchByKltSVcowmWavcAsvuTlbtqp5/uhA8J/PJWFh8s16A8uR1ZUJCz7l
XvxaOZU3beX4ZhQeVThFjqFhJ7x2boUtIrKk3mtSs26ImNbFucFpOKQLB1YLpp8X
yl4briECgYEAz0e4Hjtfow5SgPeKxGXZn6AXYqkY7F6QVQ+jSbOCvXcYe+igtVXS
nkMyeE4uEzxAJKtEXnFjk04F3CbtlTjiaSXGW1xrGP56jZDxdzU2izbP7Z1F9sgT
9sgtcngp50yWEkyW/RR8xNtbp5VameLt7e9nXPAIVpxBc9tMIAShCI8CgYEA+88x
SPSd4XVMr0Pk8+d/8DSWxtvfuO3zwTj2HELsg+O64a2pykcfW/DgTtR04R9L/MxZ
nusFKbqHCVQAG2JAZ8HqMSgJ8VbSpi+5cotXvu1CvzxtXhlEQtj5UO2IeeviYw4V
UrRHwIhngqjHcHT0b6mQqQ1y3OYb4DxGnpXrCiECgYAeU/sPiVZr8CuILTADnndi
ELV7PQylgQyTNY+JuBc4C5Xsg1QIVD9V4rUevymkrNshwmFlhCeypObcmGGIxOLz
yZAlS/drl8hssDl0XLfXVLTFqo5TFmE9aXqk1gojiqQml0g8TWQYFZRqh8LS4042
0yGHiqNdsM0u23Ze9O5u5wKBgQDTDfxPG8hgukJF/HAgBn7zRADEOHIxvC+8WhPd
6DH48Z0nnrlbM3WTSDeZmvVD40l7X4QWcQHo0dBw/xj/2sAEt0GlZdu/jngMlp+m
5CftfUueofVBE4hlRxrgu9bR6eXcBGfW5Afn1ex8VR6koUJnfQYky4Lkp3Hh5mOC
dEGGQQKBgCkQJBBgfDwHI3Q+1n76yS+/Zb+P4oSFljW1AmAZ27brUwxdf8URePM1
DXs43B2uovLTVBPUUpqzsnX+9J66pFZ0OcJzuENN1NQdZX9w2q9Hjy+QVM2SpZOu
QMTpOSuBuWpmqnKs31pUBeqNdm2YhtHQW8xTe25pM3lThqk+nMRb
-----END RSA PRIVATE KEY-----
```

* RSA 2048 公鑰檔 rsa_key.pub
```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAy+MUa1EiiheiZz+I77Pe
wt8SB2f2NaysabdxXMtJhX/6R9aGq8I+gFFrvQ9BtK5g5LSoXjfsJpIF5TZ1TPIJ
RwnN1PRzDsJyar/wsB3+bFHOeLBgyVhBcQJ0yXstLhbQb64CEBg6kizHTuGRnB5P
4shNpNwaC1Nr0+oTnAsP1doG47PKeUdYyRBj40jfztxXT8wXnMzTY1ZJQDjov32n
ndTURGHlabidmboJbn18zsbGJ6BAsHWokmL7dF6ao2bFH5BMP0APEVMVm3K/1jD5
ehkJN4paZnaIDXAbKVHKwjccjIzYgo2UjKtdcMAYqQy3UmkdzIUQy+sJkmxe+Vyw
bwIDAQAB
-----END PUBLIC KEY-----
```

由此執行結果可驗證**原文純文字檔案**與**解密後的純文字檔案**內容相符

## 參考資料
> * [PyCryptodome Docs - Examples](https://www.pycryptodome.org/en/latest/src/examples.html#encrypt-data-with-rsa)
> [name=PyCryptodome]
> * [Python Documentation - binascii.hexlify](https://docs.python.org/3.9/library/binascii.html#binascii.hexlify)
> [name=Python]
> * [Python Documentation - bytes.decode](https://docs.python.org/3.9/library/stdtypes.html#bytes.decode)
> [name=Python]
> * [RSA Encrypt / Decrypt - Examples](https://cryptobook.nakov.com/asymmetric-key-ciphers/rsa-encrypt-decrypt-examples)
> [name=Svetlin Nakov]
> * [AES-CTR](https://github.com/rdomanski/AES-CTR/blob/master/aes-ctr.py)
> [name=Radek Domanski (rdomanski)]
> * [菜園角耕耘田地 - pycrypto筆記: 使用AES區塊加密之CBC和CTR工作模式](https://bryceknowhow.blogspot.com/2018/05/cryptography-pycrypto-aescbcctr.html)
> [name=Bruno Chen]
> * [Python Check If File or Directory Exists](https://www.guru99.com/python-check-if-file-exists.html)
> [name=GURU99]
> * [Python3 教學 #04 (Ch6~Ch8: Try-catch 錯誤處理)](https://www.brilliantcode.net/753/python3-6-try-catch/?cli_action=1607266997.27)
> [name=Andy Wang]
> * https://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3
> * https://stackoverflow.com/questions/5000946/how-to-generate-strong-one-time-session-key-for-aes-in-python
> * https://stackoverflow.com/questions/934160/write-to-utf-8-file-in-python
> * https://stackoverflow.com/questions/491921/unicode-utf-8-reading-and-writing-to-files-in-python
> * https://stackoverflow.com/questions/30056762/rsa-encryption-and-decryption-in-python
> * https://stackoverflow.com/questions/14714968/pycrypto-aes-ctr-implementation
> * https://stackoverflow.com/questions/14716338/pycrypto-how-does-the-initialization-vector-work
> * https://stackoverflow.com/questions/30056762/rsa-encryption-and-decryption-in-python
> * https://stackoverflow.com/questions/33269020/convert-byte-string-to-base64-encoded-string-output-not-being-a-byte-string
> * https://stackoverflow.com/questions/34279901/python-rsa-encryption
> * https://stackoverflow.com/questions/21327491/using-pycrypto-how-to-import-a-rsa-public-key-and-use-it-to-encrypt-a-string
> * https://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256
> * https://stackoverflow.com/questions/44427934/notimplementederror-use-module-crypto-cipher-pkcs1-oaep-instead-error
> * https://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3
> * https://stackoverflow.com/questions/606191/convert-bytes-to-a-string
> * https://stackoverflow.com/questions/20024490/how-to-split-a-byte-string-into-separate-bytes-in-python/20024864