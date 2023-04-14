import try_again
from try_again import filter_profanity
from try_again import leet_conver
from try_again import analytics

def cleanText(mess):
    processed = leet_conver(mess)
    cleaned = filter_profanity(processed)
    jaro = analytics(processed)
    return cleaned

