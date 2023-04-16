from tkinter import *
import requests
import random


def get_quote():
    # response = requests.get(url="https://type.fit/api/quotes")
    response = requests.get(url="https://buddha-api.com/api/random")
    response.raise_for_status()
    quote = response.json()
    # print(data)
    # quote = random.choice(quote)
    quote_1 = quote["text"]
    quote_2 = quote["byName"]
    quote = f"{quote_1} - {quote_2}"
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Buddha Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Buddha Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="golden-buddha_100.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
