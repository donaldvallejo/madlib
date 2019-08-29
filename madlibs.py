# Provide a Mad Libs story for users to fill in
# Collect user input for the words
# Print the story with all blanks filled in by the user’s words
# Use at least 3 parts of speech for word replacement
# Use variable assignment to store/use values
# Write and call functions
# Use at least one of the following core data types: strings, integers, floats
# Use at least one of the following collection types: lists, tuples, dictionary

# input - hardcode whole madlib, have variables for each blank word
# output - print sentence variables. display if it's a verb adjective etc
# processing - separate variables for each word
# print whole string. prompt for each blank word. print new string with user's input.


def main():
    print('test')
    madlib()
    adjective = wordAdjective()
    noun = wordNoun()
    verb = wordVerb()
    print("test")
    return True
    # printEmpty()


def madlib():
    story = "there was once a _____(adjective) person. who wanted to be a _____(noun). So one day he/she finally got to ______(verb)"
    print(story)
    return True


def wordAdjective():
    adjective = ""
    print(len(adjective))
    while len(adjective) == 0 or isinstance(adjective, str) == False:
        adjective = input("there was once a _______(adjective): ")
        if len(adjective) == 0 or isinstance(adjective, str) == False:
            print("must input a string with length greater than 0!")
            
    return adjective

def wordNoun():
    noun = ""
    while len(noun) == 0 or isinstance(noun, str) == False:
        noun = input("who wanted to be a _____(noun): ")
        if len(noun) == 0 or isinstance(noun, str) == False:
            print("must input a string with length greater than 0!")
    return noun

def wordVerb():
    verb = ""
    while len(verb) == 0 or isinstance(verb, str) == False:
        verb = input("So one day he/she finally got to ______(verb): " )
        if len(verb) == 0 or isinstance(verb, str) == False:
            print("must input a string with length greater than 0!")
    return verb

main()