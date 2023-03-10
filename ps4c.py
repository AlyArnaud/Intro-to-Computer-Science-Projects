# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words =  load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # VOWELS_LOWER = 'aeiou'
        # VOWELS_UPPER = 'AEIOU'
        # CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
        # CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'
        
        _vowels_permutation_lower = vowels_permutation.lower()
        #print("Lowercase: ", vowels_permutation_lower)
        _vowels_permutation_upper = vowels_permutation.upper()
        #print("Uppercase: ", vowels_permutation_upper)
        #Empty Dictionary
        _init_dict = {}
        _index = 0
        #Add uppercase vowels
        for _char in VOWELS_UPPER: 
            _init_dict[_char] = _vowels_permutation_upper[_index]
            _index = _index +1
        
        #Add lowercase vowels
        _index = 0
        for _char in VOWELS_LOWER:
            _init_dict[_char] = _vowels_permutation_lower[_index]
            _index = _index+1
        
         #Add lowercase consanants
        for _char in CONSONANTS_LOWER:
            _init_dict[_char] = _char
        
        #Add uppercase consanants
        for _char in CONSONANTS_UPPER:
            _init_dict[_char] = _char
            
        #print(init_dict)
        return _init_dict
        
       
                
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        _translated_string = ""
        #For character in string
        for _char in self.get_message_text():
        #Check if is_alpha or not
            if _char in string.ascii_letters:
                #if is alpha, shift according to dictionary
                #append to translated_string
                _translated_string = _translated_string + transpose_dict[_char]
        #if not is_alpha, append to translated_string
            else:
                _translated_string += _char
        #return shifted string
        return _translated_string
        
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        #record best_shift as int
        _best_perm = ""
        #record highest_word_count as int
        _highest_word_count = 0
        #Create a list of all permutations
        _all_perms = get_permutations('aeiou')
        #for each permutation build a dict with the transpose build_transpose_dict
        for _perm in _all_perms: 
            _dict_attempt = self.build_transpose_dict(_perm)
            #apply shift
            _message_attempt = self.apply_transpose(_dict_attempt)
            #test for num words isword
            _word_count = 0
            
            #change message_attempt string to list to iterate over
            _words_list = _message_attempt.split()
            #for word in message
            for _word in _words_list: 
                #if word is in load_words word_count++
                if is_word(self.valid_words, _word):
                    _word_count = _word_count+1
                    #print("word_count:" + str(word_count))
            #if word_count > highest_word_count replace highest word count & update best_shift
            if _word_count > _highest_word_count: 
                _highest_word_count = _word_count
                _best_perm = _perm
                
        #return a tuple with the shift and message text
        _best_dict = self.build_transpose_dict(_best_perm)
        _my_message = self.apply_transpose(_best_dict)

        return _my_message
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
