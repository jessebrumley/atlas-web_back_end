import requests
import json

# Base URL for Deezer API
DEEZER = "https://api.deezer.com"

# Function to fetch genres
def get_genres():
    response = requests.get(f"{DEEZER}/genre")
    if response.status_code == 200:
        return response.json()['data'][:5]  # Get top 5 genres
    else:
        print("Error fetching genres")
        return []

# Function to fetch artists for a given genre
def get_artists(genre_id):
    response = requests.get(f"{DEEZER}/genre/{genre_id}/artists")
    if response.status_code == 200:
        return response.json()['data'][:3]  # Get top 3 artists
    else:
        print(f"Error fetching artists for genre {genre_id}")
        return []

# Function to fetch albums for a given artist
def get_albums(artist_id):
    response = requests.get(f"{DEEZER}/artist/{artist_id}/albums")
    if response.status_code == 200:
        return response.json()['data'][:2]  # Get 2 albums per artist
    else:
        print(f"Error fetching albums for artist {artist_id}")
        return []

# Function to fetch tracks for a given album
def get_songs(album_id):
    response = requests.get(f"{DEEZER}/album/{album_id}")
    if response.status_code == 200:
        return response.json()['tracks']['data']  # Get tracks
    else:
        print(f"Error fetching songs for album {album_id}")
        return []

# Main function to pull all data
def fetch_music_data():
    music_data = {
        'genres': []
    }

    genres = get_genres()

    for genre in genres:
        genre_data = {
            'id': genre['id'],
            'name': genre['name'],
            'artists': []
        }

        artists = get_artists(genre['id'])
        for artist in artists:
            artist_data = {
                'id': artist['id'],
                'name': artist['name'],
                'albums': []
            }

            albums = get_albums(artist['id'])
            for album in albums:
                album_data = {
                    'id': album['id'],
                    'title': album['title'],
                    'release_year': album['release_date'].split('-')[0],  # Extract release year
                    'songs': []
                }

                songs = get_songs(album['id'])
                for song in songs:
                    album_data['songs'].append({
                        'id': song['id'],
                        'title': song['title'],
                        'duration': song['duration'],  # Duration in seconds
                        'preview': song['preview']
                    })
                
                artist_data['albums'].append(album_data)

            genre_data['artists'].append(artist_data)
        music_data['genres'].append(genre_data)
    
    return music_data

# Save data to a JSON file
def save_to_json(data, filename="data.json"):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data saved to {filename}")

# Run the script
if __name__ == "__main__":
    music_data = fetch_music_data()
    save_to_json(music_data)
