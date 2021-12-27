'''
make page

create word
type word
    if right green 
        index ++
    else
        red
progress ++
when progress = 15
    letter per leeter
    accuracy = no of letters typed correctly/ total letters



'''
import webbrowser
# FLASK

from flask import Flask,render_template
#from flask import Flask, redirect, url_for, render_template, request, send_from_directory
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('hello.html', name = 'Aromal')


if __name__ == '__main__':
    webbrowser.open_new_tab('http://localhost:5000/')
    app.run()