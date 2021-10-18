import os, requests

# model the class after the users table from our database
class NASA_API:
    def __init__( self , data ):
        self.date = data['date']
        self.explanation = data['explanation']
        self.title = data['title']
        self.media_type = data['media_type']
        self.copyright = data['copyright']
        self.url = data['url']

    @classmethod
    def get_today(cls):
        result = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={os.environ.get('NASA_API')}").json()
        print(result)
        
        return cls(result)