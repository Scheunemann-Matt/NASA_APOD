import os, requests

class Wiki_API:
    # classes in the wiki html to replace
    WIKI_CLASSES = [
        'hatnote', 'infobox-below', 'infobox-caption', 
        'infobox-header', 'mw-headline', 'thumbcaption', 
        'thumbinner','wikitable', '<ul>', 
        '<li>', 'thumbimage', 'gallery', 
        'infobox'
        ]
    # classes to place into the wiki html in matching order with above.
    REPLACE_CLASSES = [
        'fs-7 ', 'bg-dark', 'fs-7', 
        'bg-black', 'title-font d-block w-max-content mw-100 mx-auto text-center', 'fs-7 mb-2', 
        'w-100 mb-2' ,'table table-dark table-striped table-bordered', '<ul class="list-group">', 
        '<li class="list-group-item bg-dark text-light">', 'mb-3', 'd-flex justify-content-between flex-wrap', 
        'table table-dark table-striped table-bordered'
        ]
    URL = "https://en.wikipedia.org/w/api.php"
    def __init__(self):
        pass
    
    # Grabs title for first wiki page from search based on title of APOD
    @classmethod
    def get_title(cls, data):
        SESS = requests.Session()

        PARAMS = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": data
        }

        result = SESS.get(url = cls.URL, params = PARAMS).json()
        # print(result)

        # see if there is a result and-
        if (len(result['query']['search']) > 1):
            # set title if there is one or-
            title =  result['query']['search'][0]['title']
        else:
            # set default title if not
            title = "outer space"
        return title
    
    # grabs the page from wiki api based on input title
    @classmethod
    def get_page(cls, title):
        SESS = requests.Session()

        PARAMS = {
            "action": "parse",
            "page": title,
            "format": "json",
            "disableeditsection" : "",
            "disabletoc" : ""
        }

        result = SESS.get(url = cls.URL, params = PARAMS).json()
        text = result["parse"]["text"]["*"]

        # removes References section
        start_of_ref = text.find('<h2><span class="mw-headline" id="References">')
        text = text[0:start_of_ref]
        
        # removes any Sidebars
        found_sidebar = text.find('<table class="sidebar')
        while  found_sidebar != -1:
            end_sidebar = text.find('</table>', found_sidebar)

            left_text = text[0:found_sidebar]
            right_text = text[end_sidebar:]
            text = left_text+right_text

            found_sidebar = text.find('<table class="sidebar')

        # replaces local links with proper wikipedia links
        text = text.replace("/wiki/", "https://www.wikipedia.org/wiki/")

        # replace incoming classes with the classes we want.
        text = cls.replace_classes(text, cls.WIKI_CLASSES, cls.REPLACE_CLASSES)

        data = {
            "text": text,
            "title": result["parse"]["title"]
        }

        return data

    @staticmethod
    def replace_classes(text, current_classes, new_classes):
        for i in range(len(current_classes)):
            text = text.replace(current_classes[i], new_classes[i])

        return text