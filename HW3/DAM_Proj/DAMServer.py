# Import the required classes and functions
import os
from flask import Flask, render_template
import os.path
import json
try: 
   import mutagen
except ImportError:
   os.system("pip install mutagen")


def intro(musiclist_name):
   musiclist_path = os.path.join("./static/", musiclist_name)
   Intro_File = open(os.path.join(musiclist_path, 'intro.txt'), mode='r', encoding="utf-8")
   musiclist_intro = str(Intro_File.readline())
   return musiclist_intro

def List(musiclist_name):
   musiclist_path = os.path.join("./static/", musiclist_name)
   musiclist = []
   num = 0
   for filename in os.listdir(musiclist_path):
      file_path = os.path.join(musiclist_path, filename)
      type = os.path.splitext(filename)[1]
      if (type != '.mp3'):
        continue
      inf = mutagen.File(file_path)
      title = os.path.splitext(filename)[0]
      num = num + 1
      musiclist.append(
         {
            'number': str(num).rjust(3, '0'),
            'name': title
         }
      )
   return musiclist

def find(musiclist_name, name):
   path = os.path.join("./static/", musiclist_name, name)
   return path

def loadJson(path):
   text = open(path)
   metadata = json.load(text)
   return metadata

def divideLyrics(lyrics):
   a = ""
   lines = []
   for char in lyrics:
      a = a + char
      if char == '\n':
         lines.append(a)
         a = ""
   return lines

# Create a instance
app = Flask(__name__)

# Route: Calls our function when the URL is accessed
@app.route('/')
def index():
    # Pass parameters to the template and render
   musiclist_name = "Likes"
   musiclist_path = "./static/Likes/"
   musiclist_intro = intro(musiclist_name)
   musiclist = List(musiclist_name)
   return render_template('page1.html', musiclist_name=musiclist_name, musiclist_intro=musiclist_intro, musiclist=musiclist, path=musiclist_path)

@app.route('/dislikes/')
def index2():
   musiclist_name = "Dislikes"
   musiclist_path = "./static/Dislikes/"
   musiclist_intro = intro(musiclist_name)
   musiclist = List(musiclist_name)
   return render_template('page2.html', musiclist_name=musiclist_name, musiclist_intro=musiclist_intro, musiclist=musiclist, path=musiclist_path)


@app.route('/<musiclist_name>.<name>')
def index3(musiclist_name, name):
   path = find(musiclist_name, name) + '.json'
   image = find(musiclist_name, name) + '.png'
   metadata = loadJson(path)
   lyrics = divideLyrics(metadata['lyrics'])
   return render_template('information.html',music_name = name, Image = image, lyrics = lyrics)

# Program entrance
if __name__ == '__main__':
   app.run(debug=True)