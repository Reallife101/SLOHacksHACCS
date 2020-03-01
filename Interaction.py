import enum
import webbrowser
import random
import os
import app

Emote_Folder = os.path.join('static', 'Emotes')

Emote = {"Happy":0, "Sad":1, "Neutral":2, "Angry":3, "MikuWavehi":4, "Confused":5, "Surprised":6, "Sleepy":7, "Sorry":8}
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

class Webpage:
	def __init__(self):
		src_folder = os.path.join(Emote_Folder, 'emotes.txt')
		self.image_store = ImageStore(src_folder)
		webbrowser.get(chrome_path).open('http://localhost:5000')

	def open(self, emote = 2):
		addr = self.image_store.get_image(emote)
		if addr != -1:
			# imgName = addr
			file= os.path.join(Emote_Folder, 'global.txt') 
			with open(file, 'w') as filetowrite:
				filetowrite.write(addr)
		# webbrowser.get(chrome_path).open('file:///' + addr)


class ImageStore:
	def __init__(self, filename):
		self.load_images(filename)

	def load_images(self, filename):
		self.image_store = []
		for emote in Emote:
			self.image_store.append([])
		try:
			file = open(filename, 'r')
			line = file.readlines()
			for s in line:
				tokens = s.split(" ")
				emote = int(tokens[0])
				path = tokens[1]
				self.image_store[emote].append(path)
			file.close()
		except Exception as e:
			raise e

	def get_image(self, emote):
		if len(self.image_store[emote]) != 0:
			return random.choice(self.image_store[emote])
		return -1

if __name__ == '__main__':
	page = Webpage()
	page.open(4)