import discord
import os
import requests
import json
import random
from replit import db
from online import online

client = discord.Client()

sad_words=["triste","depressão","raiva"]
nice_words=["você é incrivel","não desista","as coisas vão melhorar"]

def get_quote():
  response=requests.get("https://zenquotes.io/api/random") 
  json_data= json.loads(response.text)
  quote=json_data[0]['q']+ " -"+json_data[0]['a']
  return (quote)
  
def update_messages(nice_message):
  if "encouragements" in db.keys():
    encouragements= db["encouragements"]
    encouragements.apend(nice_message)
    db["encouragements"]=encouragements
  else:
    db["encouragements"]=[nice_message]
  
    

def delete(index):
  encouragements=db["encouragements"]
  if len(encouragements)>=index:
    del encouragements[index]
    db["encouragements"]=encouragements
    
  
@client.event
async def on_ready():
  print('logado: {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author==client.user:
    return
  if message.content.startswith('$mensagem'):
    quote=get_quote()    
    await message.channel.send(quote)
    
    options=nice_words
    if "encouragements" in db.keys():
      options=options+db["encouragements"]
      
  if any(word in message.content for word in sad_words):
    await message.channel.send(random.choice(options))

  if message.content.startswith("$new"):
    nice_message=message.content.split("$new ",1)[1]
    update_messages(nice_message)
    await message.channel.send("Nova mensagem adicionada")

  if message.content.startswith("$del"):
    encouragements=[]
    if "encouragements" in db.keys():
      index=message.content.split("$del",1)[1]
      delete(index)
      encouragements=db["encouragements"]
      await message.channel.send(encouragements)

online()

my_secret = os.environ['TOKEN']
client.run(os.getenv('TOKEN'))

  