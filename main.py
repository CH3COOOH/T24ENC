# -*- coding: utf-8 -*-
import base64
import tkinter as tk
from tkinter import ttk

import enc

class MainFrame:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title("T24ENC-20240119")
		self.frame1 = ttk.Frame(self.root)
		self.frame1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
		self.frame2 = ttk.Frame(self.root)
		self.frame2.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
		self.text1 = tk.Text(self.frame1, width=30, height=10)
		self.text1.pack(side=tk.LEFT)
		self.frame_button = ttk.Frame(self.frame1)
		self.frame_button.pack(side=tk.LEFT, padx=10)
		self.encrypt_button = ttk.Button(self.frame_button, text="ENC>", command=self.encrypt)
		self.encrypt_button.pack(side=tk.TOP)
		self.decrypt_button = ttk.Button(self.frame_button, text="<DEC", command=self.decrypt)
		self.decrypt_button.pack(side=tk.TOP)
		self.text2 = tk.Text(self.frame1, width=30, height=10)
		self.text2.pack(side=tk.LEFT)
		self.password_label = ttk.Label(self.frame2, text="PW:")
		self.password_label.pack(side=tk.LEFT)
		self.password_entry = ttk.Entry(self.frame2, show="*")
		self.password_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
		self.root.resizable(False, False)
		
	def run(self):
		self.root.mainloop()
		
	def encrypt(self):
		self.text2.delete('1.0', tk.END)
		plain_byte = self.text1.get('1.0', tk.END).encode('utf-8')
		enc_byte = enc.encrypt_by_pwd(plain_byte, self.password_entry.get())
		self.text2.insert('1.0', base64.b85encode(enc_byte).decode('utf-8'))
		return 0
	
	def decrypt(self):
		self.text1.delete('1.0', tk.END)
		enc_byte_85 = self.text2.get('1.0', tk.END).strip()
		try:
			enc_byte = base64.b85decode(enc_byte_85)
		except:
			self.text1.insert('1.0', '# BAD INPUT #')
			return -1
		try:
			dec_byte = enc.decrypt_by_pwd(enc_byte, self.password_entry.get())
			self.text1.insert('1.0', dec_byte.decode('utf-8'))
			return 0
		except:
			self.text1.insert('1.0', '# BAD PASSWORD #')
			return -1
		
if __name__ == '__main__':
	mainframe = MainFrame()
	mainframe.run()