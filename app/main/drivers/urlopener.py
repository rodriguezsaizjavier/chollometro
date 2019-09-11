import urllib.request


class AppURLopener(urllib.request.FancyURLopener):
    version = "App/1.7"


urllib._urlopener = AppURLopener()


