
# We import the necessary dependency libraries
from flask import Flask, render_template, request, url_for, redirect, session # the flask library is for web app dev.
# render template allows us to show user html templates we store
from utils import validate_user # we just made this script and function to validate users
# we instantiate an instance of the Flask class
app = Flask(__name__)

app.secret_key = '78h54foinrsnifweofiodsnnbUYVYIBKNFH45029347'



@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        username = request.form['username']
        print(username)
        password = request.form['password'] ###ERROR PULLING PASSWORD HERE
        print(password)


        user_validated = validate_user(username, password)

        if user_validated:
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))

        return redirect(url_for('home')) # redirect to home page
    else:
        return render_template('login_template.html')

@app.route('/home', methods = ['GET', 'POST'])
def home():
    if 'username' in session.keys():
        pass
    else:
        session['username']= 'sir or madame'
    return render_template('home_template.html', username=session['username'])



# Homework:
# Add another page for the home_template.html (hint: use similar structure above)
# Upload the modified app.py to Python anywhere
# Reload the server and try going to your new page
#(bonus) - get buttons to work by modifying the url it redirects to
# If you make changes to HTML or other files locally you have to upload them to the server too


if __name__ == "__main__":
    app.run()
