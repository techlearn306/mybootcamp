from flask import Blueprint,redirect,url_for;

app2 = Blueprint('app2', __name__)
@app2.route('/admin')
def admin():
    return 'Hello Admin'

@app2.route('/guest/<guest>')
def guest(guest):
    return 'Hello %s as Guest'%guest;
@app2.route("/user/<name>")
def user(name):
    if name=='admin':
        return redirect(url_for('app2.admin'))
    else :
        return redirect(url_for('app2.guest',guest=name))
    

    
