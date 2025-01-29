from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Importing models
from models import db, User, Song, Playlist

db = SQLAlchemy
# Initializing the Flask app
app = Flask(__name__)
app.config.from_object('config.Config')
migrate = Migrate(app, db)


# Routes for User CRUD operations

#to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User with this username already exists'}), 400

    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

# to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users])

# to get a single user by ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email})
# to update a user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()

    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)

    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

# to delete a user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})

# to create a new song
@app.route('/songs', methods=['POST'])
def create_song():
    data = request.get_json()
    title = data.get('title')
    artist = data.get('artist')
    genre = data.get('genre')
    release_date = data.get('release_date')
    duration = data.get('duration')

    new_song = Song(title=title, artist=artist, genre=genre, release_date=release_date, duration=duration)
    db.session.add(new_song)
    db.session.commit()
    return jsonify({'message': 'Song created successfully'}), 201

# to get all songs
@app.route('/songs', methods=['GET'])
def get_songs():
    songs = Song.query.all()
    return jsonify([{'id': song.id, 'title': song.title, 'artist': song.artist, 'genre': song.genre} for song in songs])

# Routes for Playlist CRUD operations

# to create a new playlist
@app.route('/playlists', methods=['POST'])
def create_playlist():
    data = request.get_json()
    name = data.get('name')
    user_id = data.get('user_id')

    new_playlist = Playlist(name=name, user_id=user_id)
    db.session.add(new_playlist)
    db.session.commit()
    return jsonify({'message': 'Playlist created successfully'}), 201

# to get all playlists
@app.route('/playlists', methods=['GET'])
def get_playlists():
    playlists = Playlist.query.all()
    return jsonify([{'id': playlist.id, 'name': playlist.name, 'user_id': playlist.user_id} for playlist in playlists])


# to run the app.
if __name__ == '__main__':
    app.run()
