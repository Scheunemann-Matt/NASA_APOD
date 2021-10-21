# ATX : NASA APOD :

Service grabs a NASA Astronomy Photograph of the Day (Either today's, a random, or one from a specific date).
Based on the title of the APOD one wikipedia page is fetched and displayed alongside the image. (Page will be more or less relevant to the APOD depending on the title, some will have absolutely nothing to do with it.)

User can register so that they can archive APODs for later viewing.

## ATX : Tech :

Service built in Flask, utilizes Bootstrap frontend classes, and uses a MySQL database.

### ATX : Dependencies :

* Flask
* Flask-Bcrypt
* PyMySQL
* Python-Dotenv
* Requests

### ATX : APIS :

* NASA APOD API
* Wikipedia Search API
* Wikipedia Page Parse API