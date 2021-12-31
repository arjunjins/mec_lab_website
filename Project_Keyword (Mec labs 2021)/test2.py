from flask import Flask, request, render_template
import webbrowser

import random as r

app = Flask(__name__)
'''
@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return render_template('my-form.html',y=processed_text)
    return processed_text
'''
@app.route('/')
def my_form():
    return render_template('test.html',word=word(),word2="dream")

@app.route("/word")
def word():
    #print("clicked")
    return str(r.randint(0,100))

if __name__ == '__main__':
    webbrowser.open_new_tab('http://localhost:5000/')
    app.run()