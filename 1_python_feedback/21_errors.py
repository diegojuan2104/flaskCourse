class TooManyPages(ValueError):
    pass



def read(readPages : int):
    PAGES = 500
    if(readPages > PAGES):
        raise TooManyPages("Too many pages the limit is:",PAGES)
    print (f"You have read {readPages} pages.")

read(5000)