import os
import nltk

def install_modules():
    os.system("pip install nltk flet wikipedia requests pyttsx3")
    nltk.download('all')

install_modules()