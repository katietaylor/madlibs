from random import choice, sample

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)
    print compliments
    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/game')
def show_madlib_form():
    """Loads game page or sends them to goodbye page"""

    answer = request.args.get("play-game")
    print answer
    if answer == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """Loads madlibs page with user inputs"""

    person_input = request.args.get("person")
    color_input = request.args.get("color")
    noun_input = request.args.get("noun")
    adjective_input = request.args.get("adjective")
    place_input = request.args.get("place")
    verb_input = request.args.get("verb")

    madlib_template = choice(["madlib.html", "madlib_2.html"])

    return render_template(madlib_template, person=person_input, color=color_input,
                           noun=noun_input, adjective=adjective_input,
                           place=place_input, verb=verb_input)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
