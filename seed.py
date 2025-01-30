from app import app, db
from models import User, Song, Playlist, PlaylistSong
from datetime import date

# sample data
def seed_data():
    with app.app_context():
        # to clear existing data 
        db.session.query(PlaylistSong).delete()
        db.session.query(Playlist).delete()
        db.session.query(Song).delete()
        db.session.query(User).delete()

        # to create Users
        user1 = User(username='John_ores', email='john@ores.com')
        user2 = User(username='Benson Kamanja', email='jane@kamas.com')

        # to create Songs
        song1 = Song(title='simple song', artist='John', genre='fusion', release_date=date(2024, 1, 1), duration=200)
        song2 = Song(title='life is for the living', artist='Kamanja', genre='folk-song', release_date=date(2025, 2, 1), duration=180)

        # to create Playlists
        playlist1 = Playlist(name='My Playlist', user_id=1)
        playlist2 = Playlist(name='Favorite Songs', user_id=2)

        # to create Playlist-Song relationship (many-to-many)
        playlist_song1 = PlaylistSong(playlist_id=1, song_id=1, order=1, rating=5)
        playlist_song2 = PlaylistSong(playlist_id=2, song_id=2, order=1, rating=4)

        # Adding the objects to the session
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(song1)
        db.session.add(song2)
        db.session.add(playlist1)
        db.session.add(playlist2)
        db.session.add(playlist_song1)
        db.session.add(playlist_song2)

        # to commit the transaction to save the data in the database
        db.session.commit()

        print("Seed data added successfully!")

# Run the seed function
if __name__ == '__main__':
    seed_data()
