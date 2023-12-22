import os
import json
from flask import Flask, render_template, request, jsonify, redirect, url_for
from itertools import count

app = Flask(__name__)

# Define the path to the JSON file acting as the local database
database_folder = 'data'
database_filename = 'local_database.json'
database_path = os.path.join(database_folder, database_filename)

# Check if the data folder exists, and create it if not
if not os.path.exists(database_folder):
    os.makedirs(database_folder)

# Check if the JSON file exists, and create it with an empty array if not
if not os.path.exists(database_path):
    with open(database_path, 'w') as file:
        json.dump([], file)

# Counter to auto-generate user IDs
user_id_counter = count(start=1)

# Function to read data from the local JSON database
def read_database():
    with open(database_path, 'r') as file:
        data = json.load(file)
    return data

# Function to write data to the local JSON database
def write_database(data):
    with open(database_path, 'w') as file:
        json.dump(data, file)

# Function to add a new user with an auto-generated ID
def add_user(name, email, username):
    try:
        # Read existing data from the local JSON database
        existing_data = read_database()

        # Add the new user with an auto-generated ID
        new_user = {"id": next(user_id_counter), "name": name, "email": email, "username": username}
        existing_data.append(new_user)

        # Write the updated data back to the local JSON database
        write_database(existing_data)

        # Redirect to the index page after successfully adding a user
        return redirect(url_for('get_users'))
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

# Route to render the form
@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

# Route to handle form submission (POST request)
@app.route('/add_user', methods=['POST'])
def add_user_route():
    try:
        # Get data from the form
        name = request.form.get('name')
        email = request.form.get('email')
        username = request.form.get('username')

        # If form data is not present, try to get JSON data
        if name is None or email is None or username is None:
            data = request.get_json()
            name = data.get('name')
            email = data.get('email')
            username = data.get('username')

        # Call the add_user function with the form data
        return add_user(name, email, username)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route('/get_users', methods=['GET'])
def get_users():
    try:
        # Read data from the local JSON database
        data = read_database()
        return render_template('index.html', data=data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a user by ID (POST request)
@app.route('/delete_user', methods=['POST'])
def delete_user():
    try:
        # Get data from the request
        data = request.get_json()
        user_id_to_delete = int(data.get('id'))

        # Read existing data from the local JSON database
        existing_data = read_database()

        # Check if the user with the specified ID exists
        user_to_delete = next((user for user in existing_data if user['id'] == user_id_to_delete), None)

        if user_to_delete:
            # Remove the user with the specified ID
            existing_data.remove(user_to_delete)

            # Write the updated data back to the local JSON database
            write_database(existing_data)

            return jsonify({"success": True, "message": "User deleted successfully."})
        else:
            return jsonify({"success": False, "error": "Invalid user ID."})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
