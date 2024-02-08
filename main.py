#REMOVE PASS AND FIX THIS FUNCTION
#trying to go through, count how many of each character, and then compare that to the other list?????
def anagram(word1, word2):
    wcount = 0
    angram = False

    for word in word1:
        wcount = word1.count(word)
        if wcount == word2.count(word):
            angram = True
        else:
            angram = False

    return angram

#comment



#function to check that the word is not 
def is_valid_input(word):
    if (word != ""):
        return True
    

if __name__ == '__main__':
    #REMOVE PASS YOUR CODE GOES HERE
    user_input1 = (input("Please enter one word: ").strip()).lower()
    user_input2 = (input("Please enter another word: ")).strip().lower()


    user_input1 = "".join(user_input1.split())
    user_input2 = "".join(user_input2.split())


    if is_valid_input(user_input1) and is_valid_input(user_input2):
        are_anagrams = anagram(user_input1, user_input2)
        print(are_anagrams)
