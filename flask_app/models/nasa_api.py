import os, requests

class NASA_API:
    def __init__( self , data ):
        self.date = data['date']
        self.explanation = data['explanation']
        self.title = data['title']
        self.media_type = data['media_type']
        if ('copyright' in data):
            self.copyright = data['copyright']
        else :
            self.copyright = 'NASA'
        if ('hdurl' in data):
            self.url = data['hdurl']
        else:
            self.url = data['url']

    @classmethod
    def get_apod(cls, options = ""):
        result = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={os.environ.get('NASA_API')}{options}").json()
        print(result)
        
        if (type(result) == list):
            return cls(result[0])
        else :
            return cls(result)