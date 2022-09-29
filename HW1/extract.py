from argparse import FileType
from distutils.log import info
import os
import mutagen
for filename in os.listdir('./'): 
    type = os.path.splitext(filename)[1]
    if (type != '.mp3'):
        continue
    inf = mutagen.File(filename)
    artwork = inf.tags['APIC:'].data
    title = inf.tags["TIT2"].text[0]
    with open(title+'.png','wb') as img:
        img.write(artwork)