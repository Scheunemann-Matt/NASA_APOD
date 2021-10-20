from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.archive import Archive


#==================================
# Archive Routes
#==================================
@app.route('/archive')
def archive():
    if 'user_id' not in session:
        flash("You must log in to do this.")
        session['flash'] = "archive"
        return render_template('login.html')

    data = {
        'user_id': session['user_id']
    }

    dates = Archive.get_all(data)
    return render_template('archive.html', dates = dates)

@app.route('/<string:date>/archive')
def add_to_archive(date):
    if 'user_id' not in session:
        flash("You must log in to do this.")
        session['flash'] = "add to archive"
        return render_template('login.html', date = date)

    data = {
        'date': date,
        'user_id': session['user_id']
    }
    
    if not Archive.get_one(data):
        Archive.create(data)

    return redirect(f'/apod/{date}')

@app.route('/apod/<string:date>/delete')
def delete_from_archive(date):
    if ('user_id' not in session):
        return redirect('/')

    data = {
        'date': date,
        'user_id': session['user_id']
    }

    Archive.delete(data)

    return redirect('/archive')