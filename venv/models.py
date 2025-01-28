from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Song model
class Song(db.Model):
    __tablename__ = 'song'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50))
    release_date = db.Column(db.Date)
    duration = db.Column(db.Integer)


# Song model
class Song(db.Model):
    __tablename__ = 'song'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50))
    release_date = db.Column(db.Date)
    duration = db.Column(db.Integer)

# Playlist model
class Playlist(db.Model):
    __tablename__ = 'playlist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='playlists', lazy=True)

    def __repr__(self):
        return f"<Playlist {self.name}>"

# Playlist-Song many-to-many relationship model
class PlaylistSong(db.Model):
    __tablename__ = 'playlist_song'

    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer)

    