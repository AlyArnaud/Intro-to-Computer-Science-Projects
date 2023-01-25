# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

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
    if word in word_list: 
        #print("In first loop")
        result = True
    else: 
        result = False
    return result

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

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
        safe_copy = self.valid_words.copy()
        return safe_copy

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        _all_letters = string.ascii_letters
                
        #Create dictionary matching letter to value 
        #{a:1, b:2 ... A:26, B:27}
        _init_dict = {}
        _index = 0
        for _char in _all_letters: 
            _init_dict[_char] = _index
            _index = _index+1
               
        #Create dictionary matching value to letter 
        #{1:a, 2:b ... 26:A, 27:B}    
        _ref_dict = {}
        _index = 0
        for _char in _all_letters: 
            _ref_dict[_index] = _char
            _index = _index+1
        
        #For every letter in init_dict shift according to passed shift key
        #For lowercase letters:
        for _elem in _init_dict: 
            if  _init_dict[_elem] < 26:
                _key = _init_dict[_elem]
                #if shift results in key greater than 25, mod 26 to loop around
                _shifted_key = (_key + shift) % 26
                #correlate new key to letter in ref_dict & update init_dict
                _shifted_char = _ref_dict[_shifted_key]
                _init_dict[_elem] = _shifted_char
                
            #For uppercase letters
            elif _init_dict[_elem] >= 26:
                _key = _init_dict[_elem]
                #change to lowercase letter so mod function works correctly
                _reduced_key = _key - 26
                _shifted_key = (_reduced_key + shift) % 26
                #change back to uppercase letter
                _caps_key = _shifted_key + 26
                _shifted_char = _ref_dict[_caps_key]
                _init_dict[_elem] = _shifted_char
        #return dictionary pairing old letter to shifted letter {a:f, b:g...}
        return _init_dict


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        #Create shift dictionary 
        _shift_dict = self.build_shift_dict(shift)
        #translated string = ""
        _translated_string = ""
        #For character in string
        for _char in self.get_message_text():
        #Check if is_alpha or not
            if _char in string.ascii_letters:
                #if is alpha, shift according to dictionary
                #append to translated_string
                _translated_string = _translated_string + _shift_dict[_char]
        #if not is_alpha, append to translated_string
            else:
                _translated_string += _char
        #return shifted string
        return _translated_string
        

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        #self.message_text assigned in parent class
        #self.valid_words = load_words() assigned in parent class
        super().__init__(text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        safe_copy = self.encryption_dict.copy()
        return safe_copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted
    
    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        if (0 <= shift < 26): 
            self.shift = shift 
        else: 
            print("invalid shift")
            return
        return


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
        super().__init__(text)
        #self.message_text = text defined in parent class
        #self.valid_words = load_words() defined in parent class

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        #record best_shift as int
        _best_shift = 0
        #record highest_word_count as int
        _highest_word_count = 0
        #for int in range 0 to 26:
        for _num in range (26):
            
            #apply shift to message 
            _message_attempt = self.apply_shift(_num)
            # print("message_attemt = " + message_attempt)
            # print("num: " + str(num))
            #in for loop counter for num correct words
            _word_count = 0
            
            #change message_attempt string to list to iterate over
            _words_list = _message_attempt.split()
            #for word in message
            for _word in _words_list: 
                #if word is in load_words word_count++
                
                #print(is_word(WORDLIST_FILENAME, word))

                if is_word(self.valid_words, _word):
                    _word_count = _word_count+1
                    #print("word_count:" + str(word_count))
            #if word_count > highest_word_count replace highest word count & update best_shift
            if _word_count > _highest_word_count: 
                _highest_word_count = _word_count
                _best_shift = _num
                
        #return a tuple with the shift and message text
        _my_message = self.apply_shift(_best_shift)
        _encrypted_message = (_best_shift, _my_message)
        return _encrypted_message

if __name__ == '__main__':

    #test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #test case (CiphertextMessage)
    ciphertext = CiphertextMessage("?Yfn'j zk xfzex?")
    print('Expected Output:', (9, "?How's it going?"))
    print('Actual Output:', ciphertext.decrypt_message())

    #Test case (cipher 13)
    ciphertext = CiphertextMessage('Unccl Oveguqnl!')
    print('Expected Output:', (13, 'Happy Birthday!'))
    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: best shift value and unencrypted story 
    #Hint: The skeleton code contains a helper function get_story_string 
    #that returns the encrypted version of the story as a string. Create 
    #a CiphertextMessage object using the story string and use decrypt_message 
    #to return the appropriate shift value and unencrypted story.
    
    #get_story_string() returns encrypted string from file
    my_story = get_story_string()
    ciphertext = CiphertextMessage(my_story)
    print(ciphertext.decrypt_message())
    pass #delete this line and replace with your code here
