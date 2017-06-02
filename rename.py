import glob, os
from random import randint

def rename(dir, pattern, titlePattern):
    i = 0
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename,
                  os.path.join(dir, titlePattern + str(i) + ext))
        i += 1

def renameRandom(dir, pattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename,
                  os.path.join(dir, 'img' + str(randint(0, 20000)) + title + ext))

#rename(r'../dataset_negative', r'*.png', r'negative_')
renameRandom(r'../dataset_all', r'*.png')
