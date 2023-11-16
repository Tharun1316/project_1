from flask import Flask, render_template, request

app = Flask(__name__)

# Data structure to store personalized learning data
learning_data = {}

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/track_progress', methods=['POST'])
def track_progress():
    user_id = request.form['user_id']
    # Update progress in learning_data
    if user_id in learning_data:
        learning_data[user_id] += 1
    else:
        learning_data[user_id] = 1
    return 'Progress tracked successfully!'

@app.route('/get_progress/<user_id>', methods=['GET'])
def get_progress(user_id):
    if user_id in learning_data:
        return f'User {user_id} has made {learning_data[user_id]} progress.'
    else:
        return 'User not found.'

if __name__ == '__main__':
    app.run(debug=True)
