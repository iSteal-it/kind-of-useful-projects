from flask import Flask, render_template, redirect, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
import smtplib

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class ContactForm(FlaskForm):
    name = TextField("Name", validators=[DataRequired(message="Please enter your name")])
    email = TextField("Email", validators=[DataRequired(message="Please enter your email")])
    subject = TextField("Subject", validators=[DataRequired(message="Please enter subject")])
    message = TextAreaField("Message", validators=[DataRequired(message="Please enter your message")])
    submit = SubmitField('Send Message.')


@app.route("/")
def home():
    return render_template("mes.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data
        flash('Your response is submitted')
        msg_to_send = f"{name}\n\n {message}"
        my_email = "dd@isteal.me"
        password = ""
        connection = smtplib.SMTP("smtp.hostinger.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='bobbobpvp@gmail.com',
            msg=f"From:{email}\nSubject:{subject}\n\n {msg_to_send}"
            )
        connection.close()
        return redirect('contact')
    return render_template("contact.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
