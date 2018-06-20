import webbrowser


class Movie():

    """A class to create a Movie() object.

    Extended description of function.

    Parameters
    ----------
    arg1 : str
        Accepts title of the movie
    arg2 : str
        Accepts story line or overview of the movie
    arg3 : str
        Accepts the url source of the poster image
    arg4 : str
        Accepts the url of the youtube trailer video
    """

    def __init__(self, title, story_line,
                 poster_image_url, trailer_youtube_url):
        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    # Function to open youtube link
    def show_trailer(self):
        print "Now playing trailer of " + self.title
        webbrowser.open(self.trailer_youtube_url)
