import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.5,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Write a haiku about an animal.

Animal: {}
Haiku:""".format(
        animal.capitalize()
    )

#Animal: Dog
#Haiku: The tail, from side to / Other side keeps flopping back / My dog is happy.

#Animal: Cat
#Haiku: Purring, a motor / Or a threatening growl / Curled up in the sun.

