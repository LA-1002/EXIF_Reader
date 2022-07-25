import PIL.Image;
from PIL.ExifTags import TAGS
import os;
import shutil;
from exif import Image

def GetEXIF(file):
    try:
        img = PIL.Image.open(file)
        exif = {}
        for k, v in img.getexif().items():
            tag = TAGS.get(k)
            exif[tag]=v
        return exif['DateTimeOriginal']
    except:
        return None;


#path = ("C:\Users\leonn\Documents\A Uni Work\D Course Rep")

def GetAllEXIF():
    files = os.listdir('old_images');
    i=0
    for file in files:
        file  = ('old_images/'+file);
        date = GetEXIF(file);
        if date != None:
            ext = os.path.splitext(file)
            date = date.replace(' ','_');
            date = date.replace(':','-') + ext[1];
            new = ('new_images/' + date);
            try:
                os.rename(file,new);
            except FileExistsError:
                date = ('(%s)'%i + date)
                i+=1;
                new = ('new_images/' + date);
                os.rename(file,new);






