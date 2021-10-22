from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.nasa_api import NASA_API
from flask_app.models.wiki_api import Wiki_API
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
# ==============================================
# Get APOD Routes
#===============================================
@app.route('/')
def rootRoute():
    apod = NASA_API.get_apod()
    wiki_title = Wiki_API.get_title(apod.title)
    wiki_parse = Wiki_API.get_page(wiki_title)
    return render_template('index.html', apod = apod, wiki_parse = wiki_parse)

@app.route('/random')
def random():
    apod = NASA_API.get_apod("&count=1")
    wiki_title = Wiki_API.get_title(apod.title)
    wiki_parse = Wiki_API.get_page(wiki_title)
    return render_template('index.html', apod = apod, wiki_parse = wiki_parse)

@app.route('/apod/<string:date>')
def date(date):
    apod = NASA_API.get_apod(f"&date={date}")
    wiki_title = Wiki_API.get_title(apod.title)
    wiki_parse = Wiki_API.get_page(wiki_title)
    return render_template('index.html', apod = apod, wiki_parse = wiki_parse)

#==================================
# Login/Registration Routes
#==================================
@app.route('/login')
def load_login():
    if "flash" not in session:
        session['flash'] = ""

    return render_template("login.html")

@app.route('/create_user', methods=['POST'])
def create_user():

    # Retrieve data from form
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": request.form['password'],
        "confirm_password": request.form['confirm_password']
    }
    
    # Validate form data
    if (not User.validate_user(data)):
        session['flash'] = "registration"
        return redirect('/login')

    # Hash PW
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # print(pw_hash)
    data['password'] = pw_hash

    user_id = User.create(data)
    
    # Add user id to session
    session['user_id'] = user_id
    
    # Routing for if the registration page was loaded due to trying to archive an APOD or go to their archive list.
    if "archive" in request.form:
        # Return to archive
        if request.form['archive'] == 'archive':
            return redirect('/archive')
        else:
            # add APOD to archive
            return redirect(f'/{request.form["date"]}/archive')
    return redirect('/')

@app.route('/users/login', methods=['POST'])
def login():
    data = {
        "email": request.form['email'],
        "password": request.form['password']
    }

    # Validation
    is_valid = True
    user_in_db = User.get_one_from_email(data)
    print(user_in_db)
    if (not user_in_db):
        is_valid = False
    elif (not bcrypt.check_password_hash(user_in_db['password'], data['password'])):
        is_valid = False

    if (is_valid):
        # if valid add user id to session
        session['user_id'] = user_in_db['id']
    if (not is_valid):
        # if not show message and redirect back to login page
        flash("Ivalid email/password")
        session['flash'] = 'login'
        return redirect('/login')

    # Routing for if the registration page was loaded due to trying to archive an APOD or go to their archive list.
    if "archive" in request.form:
        # Return to archive
        if request.form['archive'] == 'archive':
            return redirect('/archive')
        else:
            # add APOD to archive
            return redirect(f'/{request.form["date"]}/archive')

    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')