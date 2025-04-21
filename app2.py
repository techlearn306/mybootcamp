from flask import Blueprint,render_template,url_for,redirect
app1 = Blueprint('app1',__name__);




@app1.route("/home/<name>")
def welcome(name):
    return "Hello, Flask!"+name;

@app1.route('/')
def home():
    
    return render_template('index.html')

@app1.route("/index")
def index(): 
    return redirect(url_for('app1.home'))


@app1.route('/about')
def about():
    print('hhhhh')
    return render_template('about.html')
@app1.route('/login')
def login():
    print('hhhhh')
    return render_template('login.html')
@app1.route('/register')
def register():
    
    return render_template('register.html')


