import urllib

def file_reader():
    quotes = open('./files/movie_quotes.txt')
    cts = quotes.read()
    print(cts)
    quotes.close()

def check_profanity(text):
    pass


file_reader()