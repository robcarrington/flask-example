from flask import Flask, render_template
import requests
import random
import sys

app = Flask(__name__)

@app.route('/')
def home():
    kanye_api = "https://api.kanye.rest"
    quote = "I'm nice at ping-pong"
    img1 = "https://cdn.wallpapersafari.com/64/31/9GHeNV.jpg"
    img2 = "https://assets.atlasobscura.com/media/W1siZiIsInVwbG9hZHMvcGxhY2VfaW1hZ2VzLzA0MzRjZGI4MTJlNjdkMzBmNV93aW5kb3dzX3hwX2JsaXNzLXdpZGUuanBnIl0sWyJwIiwidGh1bWIiLCJ4MzkwPiJdLFsicCIsImNvbnZlcnQiLCItcXVhbGl0eSA4MSAtYXV0by1vcmllbnQiXV0/windows_xp_bliss-wide.jpg"
    img3 = "http://getwallpapers.com/wallpaper/full/1/9/e/1334603-meme-background-pictures-3840x2160-phone.jpg"
    img_list = [img1, img2, img3]
    return render_template("test_template.html", quote=quote, img=random.choice(img_list))


@app.route('/<name>')
def whats_up(name):
    kanye_api = "https://api.kanye.rest"
    img1 = "https://cdn.wallpapersafari.com/64/31/9GHeNV.jpg"
    img2 = "https://assets.atlasobscura.com/media/W1siZiIsInVwbG9hZHMvcGxhY2VfaW1hZ2VzLzA0MzRjZGI4MTJlNjdkMzBmNV93aW5kb3dzX3hwX2JsaXNzLXdpZGUuanBnIl0sWyJwIiwidGh1bWIiLCJ4MzkwPiJdLFsicCIsImNvbnZlcnQiLCItcXVhbGl0eSA4MSAtYXV0by1vcmllbnQiXV0/windows_xp_bliss-wide.jpg"
    img3 = "http://getwallpapers.com/wallpaper/full/1/9/e/1334603-meme-background-pictures-3840x2160-phone.jpg"
    img_list = [img1, img2, img3]
    return render_template("test_template.html", quote="What's up " + name, img=random.choice(img_list))

if __name__ == '__main__':
    app.run(debug=True)