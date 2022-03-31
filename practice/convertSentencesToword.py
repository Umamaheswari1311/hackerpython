""" sentence to word conversion """
import sys
def fetch_words(sentence):
    """ split the sentence with space
    Args:
        sentence:Pass the sentence
    Returns:
        A list of words
    """
    words=sentence.split()
    store=[]
    for word in words:
        store.append(word)

    print(store)
if __name__=='__main__':
    fetch_words(sys.argv[1])#The 0th arg is the sentence
