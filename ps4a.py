# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    #Sequence is a single character, so there is only one way to order it
    #recursion base case
    if len(sequence) == 1: 
        return [sequence]
    
    #recursive call to get down to base case
    #returns list of permutations of substrings
    prev_list = get_permutations(sequence[1:])

    new_list = []
    #for every permutation in prev list
    #add new letter into every possible location
    for elem in prev_list:
        for index in range(len(elem)+1):
            new_list += [elem[0:index] + sequence[0] + elem[index:]]
            
    return new_list

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    test1 = 'abc'
    print("Test 1 input", test1)
    print("Expected output: ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']")
    print("Actual output: ", get_permutations(test1))

    test2 = '012'
    print("Test 1 input", test2)
    print("Expected output: ['012', '102', '120', '021', '201', '210']")
    print("Actual output: ", get_permutations(test2))
    
    test3 = 'def'
    print("Test 1 input", test3)
    print("Expected output: ['def', 'edf', 'efd', 'dfe', 'fed', 'fde']")
    print("Actual output: ", get_permutations(test3))

