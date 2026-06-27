from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# home page
@app.route("/")
def home():
    people = []

    try:
        with open("data.txt", "r") as file:
            for line in file:
                person = line.strip().split(",")
                people.append(person)
    except FileNotFoundError:
        pass

    return render_template("home.html", people=people)


# Add page
@app.route("/add")
def add():
    return render_template("add.html")


# Save the submitted data
@app.route("/save", methods=["POST"])
def save():
    name = request.form["name"]
    age = request.form["age"]
    anime = request.form["anime"]

    with open("data.txt", "a") as file:
        file.write(f"{name},{age},{anime}\n")

    return redirect("/")


# Run the website
if __name__ == "__main__":
    app.run(debug=True)