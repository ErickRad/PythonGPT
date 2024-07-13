import os
import nltk

def install_modules():
    os.system("pip install nltk flet wikipedia requests pyttsx3")
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('all-corpora')

install_modules()
