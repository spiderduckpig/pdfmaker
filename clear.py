import os
import glob

path = os.getcwd()

paths = [os.path.join("input\\*"), os.path.join("threshed\\*"), os.path.join("pdfs\\*"), os.path.join("Final\\*")]

for path in paths:
    files = glob.glob(path)
    for f in files:
        os.remove(f)