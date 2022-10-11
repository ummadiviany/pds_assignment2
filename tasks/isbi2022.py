from json import load

# To load the json file
data = load(open("data/isbi2022.json", mode='r', encoding='utf-8'))
# Common list of stopwords
stopwords = list(map(lambda x: x.strip(), open("data/stopwords.txt", mode='r', encoding='utf-8').readlines()))


def get_authors():
    """ Returns authors of all papers in sorted by appearance count (descending)

    Returns:
        dict: dict of authors and their appearance count, sorted by count (descending)
    """
    
    return
    

def get_word_cloud():
    """ 
    Returns:
        dict: dict of title words and their appearance count, sorted by count (descending), excluding stopwords 
    """
        
    
    
def get_titles():
    """ 
    Returns:
        dict: dict of titles and their download count + citation count, sorted by count (descending)
    """
    
    return
    
    

if __name__ == "__main__":
    pass