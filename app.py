from flask import Flask, render_template, request, jsonify, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key


# Simulated user data (replace with your authentication system)
users = {
    'user1': 'password1',
    'user2': 'password2',
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users and users[username] == password:
        session['username'] = username  # Store username in session
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid username or password'}), 401
    
@app.route('/dashboard')
def dashboard():
    username = session.get('username')
    if username:
        return render_template('dashboard.html', username=username)
    else:
        return redirect(url_for('index'))  # Redirect to login page if not logged in


if __name__ == '__main__':
    app.run(debug=True)

