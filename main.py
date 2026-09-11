import json
import os

import pyshorteners
import validators

url_mem = {}
s = pyshorteners.Shortener()

# Loading data after a restart
if os.path.exists("urls.json"):
    with open("urls.json", "r") as file:
        loaded_data = json.load(file)
    url_mem = loaded_data    




# Menu
print("========================")
print("URL SHORTENER")
print("========================")

print("1. Shorten a URL")
print("2. View URL history")
print("3. Delete a URL")
print("4. Exit")
print()


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





while True:
    option = input("Choose an option (1/2/3/4): ")
    if option == "1":
        while True:
            shorten_url()

            repeat = input("Do you want to shorten another url? (y/n)")

            if repeat.lower() == "y":
                continue

            elif repeat.lower() == "n":
                # Saving data "Presistnt File"
                with open("urls.json", "w") as file:
                    json.dump(url_mem, file, indent=4)

                break

    elif option == "2":
        print("---  URL History  ---")
        for original_url, shortend_url in url_mem.items():
            print(f"{original_url} → {shortend_url}")
        continue


    elif option == "3":
        numbered_urls = list(enumerate(url_mem.items(), start=1))
        for url in numbered_urls:
            print(url)
        delete_num = int(input("Choose which URL to delete (Pick a number): "))
        delete_num -= 1
        print(f"The URL you're deleting is: {numbered_urls[delete_num]}")
        original_url = numbered_urls[delete_num][1][0]
        del url_mem[original_url]
        continue




    elif option == "4":
        break
