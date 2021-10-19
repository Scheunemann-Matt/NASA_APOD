import os, requests


class Wiki_API:
    WIKI_CLASSES = ['hatnote', '"infobox"', 'infobox-caption', 'infobox-header', 'mw-headline', 'thumbcaption', 'thumbinner','wikitable', '<ul>', '<li>', 'thumbimage', 'gallery', 'infobox-below']
    REPLACE_CLASSES = ['fs-7 ', '"table table-dark table-striped table-bordered"', 'fs-7', 'bg-black', 'title-font d-block w-max-content mw-100 mx-auto text-center', 'fs-7 mb-2', 'w-100 mb-2' ,'table table-dark table-striped table-bordered', '<ul class="list-group">', '<li class="list-group-item bg-dark text-light">', 'mb-3', 'd-flex justify-content-between flex-wrap', 'bg-dark']
    URL = "https://en.wikipedia.org/w/api.php"
    def __init__(self, data):
        pass

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
        print(result)
        if (len(result['query']['search']) > 1):
            title =  result['query']['search'][0]['title']
        else:
            title = "outer space"
        return title
    
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

        start_of_ref = text.index('<h2><span class="mw-headline" id="References">')
        text = text[0:start_of_ref]

        text = text.replace("/wiki/", "https://www.wikipedia.org/wiki/")
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