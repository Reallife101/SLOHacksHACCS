from flask import Flask, render_template
import os, Interaction

#if fails disable this
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route("/")
def home():
	try:
		filename = os.path.join(Interaction.Emote_Folder, "global.txt")
		file = open(filename, 'r')
		imgName = file.readlines()[0]
		file.close()
	except Exception as e:
		raise e
	full_filename = os.path.join(Interaction.Emote_Folder, imgName)
	return render_template("index.html", image = full_filename)

if __name__ == '__main__':
	app.run()