from flask import Flask, request, render_template, request
from stories import story

app = Flask(__name__)

@app.route('/')
def show_form():
  
  prompts = story.prompts
  return render_template('form.html', prompts = prompts)

@app.route('/story')
def show_story():

  print(request.args)
  text = story.generate(request.args)

  return render_template('story.html', text = text)



  
