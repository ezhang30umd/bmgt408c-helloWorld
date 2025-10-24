from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Ethan Zhang! I am making my first code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def aboutcss():
    return render_template('about-css.html')

@app.route('/greeting')
def greeting():
    return render_template('greeting.html')

@app.route("/favorite-course", methods=["GET"])
def favorite_course():
    subject = request.args.get("subject")
    course_number = request.args.get("course_number")

    # Check if the form has been filled
    if subject and course_number:
        # Show the confirmation message
        return render_template(
            "favorite-course.html",
            submitted=True,
            subject=subject,
            course_number=course_number
        )
    else:
        # Show the form initially
        return render_template("favorite-course.html", submitted=False)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        message = request.form.get("message")

        return render_template(
            "contact.html",
            submitted=True,
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message
        )

    # If GET request, show empty form
    return render_template("contact.html", submitted=False)

if __name__ == '__main__':
    app.run()
