from flask import  Flask, render_template, request

import json
import os

import pyshorteners
import validators


app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")





url_mem = {}
s = pyshorteners.Shortener()

# Loading data after a restart
if os.path.exists("urls.json"):
    with open("urls.json", "r") as file:
        loaded_data = json.load(file)
    url_mem = loaded_data    



def shorten_url():

# validate url
    while True:
      url = input("Enter the url you want to shorten here:")
      if validators.url(url):
         break
      else:
         print("The url is invalid")
         continue
    
         
    saved_url = url

# send url to api
      
    shortend_url = s.tinyurl.short(saved_url)





      

# return shortened url
    url_mem[saved_url] = shortend_url
    return shortend_url
def delete_url():
    numbered_urls = list(enumerate(url_mem.items(), start=1))
    
    for url in numbered_urls:
            print(url)
    
    delete_num = int(input("Choose which URL to delete (Pick a number): "))
    delete_num -= 1
    print(f"The URL you're deleting is: {numbered_urls[delete_num]}")
    
    original_url = numbered_urls[delete_num][1][0]
    del url_mem[original_url]

    with open("urls.json", "w") as file:
        json.dump(url_mem, file, indent=4) 

    print("URL deleted succesfully...")





#Flask startup
if __name__ == "__main__":
    app.run(debug=True)
