from flask import Flask, jsonify, render_template,request
from flask.views import MethodView
from flask_simplelogin import SimpleLogin, get_username, login_required
from Friendships_create import buildquerydataforfriendshipscreate

my_users = {
    'matt': {'password': 'matt', 'roles': ['admin']},
    'lee': {'password': 'douglas', 'roles': []},
}


def check_my_users(user):
    """Check if user exists and its credentials.
    Take a look at encrypt_app.py and encrypt_cli.py
     to see how to encrypt passwords
    """
    user_data = my_users.get(user['username'])
    if not user_data:
        return False  # <--- invalid credentials
    elif user_data.get('password') == user['password']:
        return True  # <--- user is logged in!

    return False  # <--- invalid credentials


app = Flask(__name__)
app.config['SECRET_KEY'] = '42'

SimpleLogin(app, login_checker=check_my_users)


@app.route('/')
@login_required(basic=True)
def index():
    return render_template('index.html')


@app.route('/secret')
@login_required(username=['matt', 'mary'])
def secret():
    return render_template('secret.html')

@app.route('/FriendShipsCreate/')
def friendshipscreate():
    return render_template('Friendships_create.html')
# calling the user timeline api which returns the most recent Tweets by the user based on query parameters.
@app.route('/FriendShipsCreateUsingParams', methods=['POST'])
def friendshipscreateusingparams():
        return buildquerydataforfriendshipscreate(request.form)


@app.route('/api', methods=['POST'])
@login_required(basic=True)
def api():
    return jsonify(data='You are logged in with basic auth')


def be_admin(username):
    """Validator to check if user has admin role"""
    user_data = my_users.get(username)
    if not user_data or 'admin' not in user_data.get('roles', []):
        return "User does not have admin role"


def have_approval(username):
    """Validator: all users approved, return None"""
    return


@app.route('/complex')
@login_required(must=[be_admin, have_approval])
def pay_stub():
    return render_template('pay_stub.html')


class ProtectedView(MethodView):
    decorators = [login_required]

    def get(self):
        return "You are logged in as <b>{0}</b>".format(get_username())


app.add_url_rule('/protected', view_func=ProtectedView.as_view('protected'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, use_reloader=True, debug=True)
