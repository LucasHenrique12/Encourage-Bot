from flask import Flask
from threading import Thread

app= Flask('')
@app.route('/')
def home():
  return"Olá. Eu estou vivo"

def run():
  app.run(host='0.0.0.0',port=8080)

def online():
  t=Thread(target=run)
  t.start()