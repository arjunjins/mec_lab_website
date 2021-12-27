# Pgm by 100 Thieves (Mec Labs 2021)
# Project : KEYWORD

"""
TEAM MEMBERS :
    1) Arjun Jins
    2) Aromal Pradeep
    3) George P Tharakan (L)
    
DESCRIPTION : 
    
    
VARIABLES :
    
"""

# IMPORTS

import random as r

# FLASK

"""
# Basic Flask

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World’

if __name__ == '__main__':
   app.run()
"""
# Flask Initialisations

from flask import Flask
#from flask import Flask, redirect, url_for, render_template, request, send_from_directory
#from werkzeug.utils import secure_filename
import webbrowser

app = Flask(__name__)

# Generate Phonetically correct words from letters

# The list
keys = [" E "," N "," I "," T "," R "," L "," S "," A "," U "," O "," D "," Y "," C "," H "," G "," M "," P "," B "," K "," V "," W "," F "," Z "," X "," Q "," J "]

def words(l):
    if len(l)==5:
        pass
    else:
        pass
    return

@app.route('/')
def hello_world():
   return "Hello World"

if __name__ == '__main__':
    webbrowser.open_new_tab('http://localhost:5000')
    app.run()