"""Assignment 1.
"""

import math

# Maximum number of characters in a valid tweet.
MAX_TWEET_LENGTH = 50

# The first character in a hashtag.
HASHTAG_SYMBOL = '#'

# The first character in a mention.
MENTION_SYMBOL = '@'

# Underscore is the only non-alphanumeric character that can be part
# of a word (or username) in a tweet.
UNDERSCORE = '_'

SPACE = ' '


def is_valid_tweet(text: str) -> bool:
    """
    Return True if and only if text contains between 1 and
    MAX_TWEET_LENGTH characters (inclusive).

    >>> is_valid_tweet('Hello Twitter!')
    True
    >>> is_valid_tweet('')
    False
    >>> is_valid_tweet(2 * 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    False

    """

    # Complete the body of this function.
    return len(text) > 0 and len(text) <= MAX_TWEET_LENGTH


# Now define the other functions described in the handout.


# A helper function.  Do not modify this function, but you are welcome
# to call it.

def clean(text: str) -> str:
    """
    Return text with every non-alphanumeric character, except for
    HASHTAG_SYMBOL, MENTION_SYMBOL, and UNDERSCORE, replaced with a
    SPACE, and each HASHTAG_SYMBOL replaced with a SPACE followed by
    the HASHTAG_SYMBOL, and each MENTION_SYMBOL replaced with a SPACE
    followed by a MENTION_SYMBOL.

    >>> clean('A! lot,of punctuation?!!')
    'A  lot of punctuation   '
    >>> clean('With#hash#tags? and@mentions?in#twe_et #end')
    'With #hash #tags  and @mentions in #twe_et  #end'
    """

    clean_str = ''
    for char in text:
        if char.isalnum() or char == UNDERSCORE:
            clean_str = clean_str + char
        elif char == HASHTAG_SYMBOL or char == MENTION_SYMBOL:
            clean_str = clean_str + SPACE + char
        else:
            clean_str = clean_str + SPACE
    return clean_str

def compare_tweet_lengths(text1: str, text2: str) -> int:
    """
    The two parameters represent valid tweets. Returns : 1 (if the first 
    tweet is longer than the second), -1 (if the second tweet is longer than 
    the first), or 0 (if the tweets have the same length).

    PreCondition: text1 and text2 must be valid tweet text and word
    
    >>> compare_tweet_lengths("hello how are you","how are you")
     1
    >>> compare_tweet_lengths("how are you","hello how are you")
     -1
    >>> compare_tweet_lengths("hello how are you","hello how are you")
     0
    
    """
    if(is_valid_tweet(text1) and is_valid_tweet(text2)):
        if(len(text1) > len(text2)):
            return 1
        elif (len(text1) < len(text2)):
            return -1
        else:
            return 0        
    
    else:
        message = 'Invalid tweet, please put valid tweets Exceeded'
        message = message + ' ' + str(MAX_TWEET_LENGTH)
        return message
    
    
def add_special_symbols(text1: str, text2: str, symbol: str)->str:
    """
    HELPER FUNCTION
    Appends a space, special symbol(# or @) and a tweet word at the end of the 
    original tweet until the length of the resulting tweet is less than 
    or equal to MAX_TWEET_LENGTH
    
    >>>add_special_symbols('I like','apples',MENTION_SYMBOL)
    I like @apples
    
    >>>add_special_symbols('I like','apples',HASHTAG_SYMBOL)
    I like #apples
    
    >>>add_special_symbols('Alphabets are',51*'ABCDEFGHIJKLM',MENTION_SYMBOL)
    Alphabets are

    
    """    
    if(is_valid_tweet(text1+' '+symbol+text2)):
        return text1+' '+symbol+text2
    else:
        return text1    
    
    
    
def add_hashtag(text1: str, text2: str) -> str:
    """
    Appends a space, hash and a tweet word at the end of the original tweet
    provided the length of the resulting tweet is less than or equal to
    MAX_TWEET_LENGTH else returns the original tweet.

    PreCondition: text1 and text2 must be valid tweet text and word
    
    >>>add_hashtag('I like','apples')
    I like #apples
    
    >>>add_hashtag('Alphabets are',2*'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    Alphabets are
    """
    
    result = add_special_symbols(text1, text2, HASHTAG_SYMBOL)
    return result




def  contain(text1: str, text2: str, symbol: str)->bool:
    """
     This function should take one valid tweet and a valid tweet word and 
     return True if and only if the tweet contains a special symbol(# or @) 
     made up of that symbol and the tweet word.
    
    >>>contain('I like @apples','apples')
    True
    >>>contains('I like #apples','app')
    False
    >>>contains('I like #apples and #grapes','apples')
    True
    """
    text1 = clean(text1)
    return ((symbol+text2+' ') in (text1+' '))




def contains_hashtag(text1: str, text2: str) -> bool:
    """
    This function should take one valid tweet and a valid tweet word and 
     return True if and only if the tweet contains a hash 
     made up of hash symbol and the tweet word.

     PreCondition: text1 and text2 must be valid tweet text and word
    
    >>>contains_hashtag('I like #apples','apples')
    True
    >>>contains_hashtag('I like #apples','app')
    False
    >>>contains_hashtag('I like #apples and #grapes','apples')
    True

    
    """
    if(is_valid_tweet(text1) and is_valid_tweet(text2)):
        result = contain(text1, text2, HASHTAG_SYMBOL)
        return result
    else:
        message = 'Invalid tweet, please put valid tweets Exceeded'
        message = message + ' ' + str(MAX_TWEET_LENGTH)
        return message
    
    
    
    
def is_mentioned(text1: str, text2: str) -> bool:
    """
    This function should take one valid tweet and a valid tweet word and 
     return True if and only if the tweet contains a mention 
     made up of the mention symbol and the tweet word.

     PreCondition: text1 and text2 must be valid tweet text and word
    
    >>>is_mentioned('I like @apples','apples')
    True
    >>>is_mentioned('I like @apples','app')
    False
    >>>is_mentioned('I like @apples and #grapes','apples')
    True

    """
    if(is_valid_tweet(text1) and is_valid_tweet(text2)):
        result = contain(text1, text2, MENTION_SYMBOL)
        return result
        
    else:
        message = 'Invalid tweet, please put valid tweets Exceeded'
        message = message + ' ' + str(MAX_TWEET_LENGTH)
        return message    
    
    
    
    
def add_mention_exclusive(text1: str, text2: str) -> str:
    """
    The function takes a valid tweet and a valid tweet word and appends 
    a space, a mention symbol, and the tweet word to the end of the 
    original tweet. If the result is a valid tweet then 
    it would return the result. In all other cases, the function should 
    return the original tweet. .

    PreCondition: text1 and text2 must be valid tweet text and word
    
    >>>add_mention_exclusive('I like apples','apples')
    I like apples @apples
    
    >>>add_mention_exclusive('I like @apples','apples')
    I like @apples
    
    """
    
    if(is_valid_tweet(text1) and is_valid_tweet(text2)):
        if ((MENTION_SYMBOL+text2) in text1):
            return text1
        elif ((text2+' ')in (clean(text1)+' ')):
            text = add_special_symbols(text1, text2, MENTION_SYMBOL)  
            if(is_valid_tweet(text)):
                return text
            else:
                return text1
        else:
            return text1
    else:
        message = 'Invalid tweet, please put valid tweets Exceeded'
        message = message + ' ' + str(MAX_TWEET_LENGTH)
        return message
              
    
    
    

def num_tweets_required(text: str) -> int:
    """
    The parameter represents a message. This function should return the
    minimum number of tweets that would be required to communicate 
    the entire message
    
    >>>num_tweets_required(2*'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    2
    >>>num_tweets_required(4*'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    3
    
    """
    return math.ceil(len(text)/MAX_TWEET_LENGTH)
       

    

def get_nth_tweet(text: str, index: int) -> str:
    """
    The funcation takes a tweet message and an integer n. If the message 
    contains too many characters, it would need to be split up into a
    sequence of tweets. All of the tweets in the sequence, except possibly
    the last tweet, would be of length MAX_TWEET_LENGTH. 
    This function should return the nth valid tweet in the sequence of tweets.
    
    
    However if the nth index has no tweet it should return an empty string.
    
    
    Preconditions: n >= 0
    
    if MAX_TWEET_LENGTH  = 4
    >>>get_nth_tweet('abcdef',1)
    ef
    >>>get_nth_tweet('abcdefghijk',2)
    ijk
    >>>get_nth_tweet('abcdefghijk',200)
    null
    >>>get_nth_tweet('abcdefghijk',1)
    efgh
    
    """
    splice = " "
    i = math.ceil(len(text) / MAX_TWEET_LENGTH)
    i = i-1
    start = (index * MAX_TWEET_LENGTH)
    if(index > i):
        splice = " "
    elif(index == i):
        splice = text[start:start + MAX_TWEET_LENGTH] 
    elif(index < i):
        splice = text[start:start + MAX_TWEET_LENGTH]
    return splice
