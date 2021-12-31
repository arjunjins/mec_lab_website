# Pgm by 100 Thieves (Mec Labs 2021)
# Project : KEYWORD

"""
TEAM MEMBERS :
    1) Arjun Jins
    2) Aromal Pradeep
    3) George P Tharakan (L)
    
DESCRIPTION : 

"""

from flask import Flask, render_template
import webbrowser

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('keyword.html')

if __name__ == '__main__':
    webbrowser.open_new_tab('http://localhost:5000/')
    app.run()