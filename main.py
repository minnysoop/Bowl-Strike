import random

# Defines program entry point
def main():
    # Display game title
    display_title()
    # Display game instructions
    display_instructions()
    # Generate sequence for user to guess
    sequence = generate_sequence()

    # IMPORTANT NOTE: Target sequence is stored in the sequence variable. Uncomment it out to view what it is.
    # print(sequence)

    # Represents the win state of the game
    winState = False

    # Represents the number of tries
    tries = 0

    # Storing previous guesses
    history = []
    
    while (not winState):
        # Prompt user for a guess
        user_input = input("Input your guess: ")
        # Check if the user's input is valid
        while (not isValidSequence(user_input)):
            print("\tYour guess must match the following criteria: ")
            print("\ta) Contain only the integers [0, 9]. Leading zeros are allowed.")
            print("\tb) Each digit is unique in the sequence. So, sequences like 1189 are not allowed.")
            user_input = input("Input your guess: ")
        
        # Format the guess into a way the program can handle it
        guess = format_input(user_input)
        # Get the result
        result = generate_feedback(guess, sequence)

        # Update the number of tries
        historyEntry = {"Sequence":guess, "Result":result}
        tries += 1
        history.append(historyEntry)

        # Format result
        format_result(result, guess, tries)

        if result["Strike"] == 4:
            print("\n---------- CONGRATULATIONS! ----------")
            print("The generated sequence was " + concatenate(sequence))
            print("You got it in " + str(tries) + " tries!")
            print("---------- SUMMARY ----------")
            print_statistics(history)
            print("---------- END OF SUMMARY ----------")
            winState = True
        

# Display game title
def display_title():
    print("""
  ___  _____      ___      ___ _____ ___ ___ _  _____ 
 | _ )/ _ \ \    / / |    / __|_   _| _ \_ _| |/ / __|
 | _ \ (_) \ \/\/ /| |__  \__ \ | | |   /| || ' <| _| 
 |___/\___/ \_/\_/ |____| |___/ |_| |_|_\___|_|\_\___|
                                                      
""")

# Displays game instructions
def display_instructions():
    print("---------- START INSTRUCTIONS ----------")
    print("A game to guess a unique four digit sequence of non negative numbers.")
    print("Gameplay: ")
    print("1) The goal of this game is to guess the four digit sequence of non negative numbers")
    print("2) You will be prompted to enter your guess")
    print("\tYour guess must match the following criteria: ")
    print("\ta) Contain only the integers [0, 9]. Leading zeros are allowed.")
    print("\tb) Each digit is unique in the sequence. So, sequences like 1189 are not allowed.")
    print("3) Feedback will be given as follows: ")
    print("\ta) #B (BOWL): The # of digits are in the sequence but in the wrong place")
    print("\tb) #S (STRIKE): The # of digits in your sequence are in the right place")
    print("\tc) It WILL NOT tell you which digits correspond to a bowl or strike. Otherwise, it's too easy ;)")
    print("4) Once you successfully guess the sequence, the game will end!")
    print("---------- END INSTRUCTIONS ----------")

# Generate sequence of numbers to guess
def generate_sequence():
    sequence = []
    # Looping through the length of the sequence
    i = 0
    while (i < 4):
        # Pseudorandomly select an integer between 0 and 9 includive. 
        digit = random.randint(0, 9)
        # If the digit not in the sequence
        if (digit not in sequence):
            # Update the sequence
            sequence.append(digit)
            # Increment i
            i += 1
    return sequence

# Generate feedback from a user-guessed sequence
def generate_feedback(guess, sequence):
    # Default feedback
    feedback = {"Bowl": 0, "Strike": 0}
    # Looping through the entire guess
    for i in range(0, 4):
        for j in range(0, 4):
            if guess[i] == sequence[j]:
                if i == j:
                    feedback["Strike"] += 1
                elif i != j:
                    feedback["Bowl"] += 1
    return feedback

# Prompt user for a guess
def format_input(input):
    guess = []
    # Parse guess into an array
    for i in range(0, 4):
        element = int(input[i])
        guess.append(element)
    return guess

# Returns true if the sequence is valid
def isValidSequence(sequence):
    length = len(sequence) == 4
    isNumbers = validCharacters(sequence)
    unique = isUnique(sequence)
    return length and isNumbers and unique

# Check if every element in the list is unique
def isUnique(sequence):
    sequenceObject = {}
    # For every element in the list
    for i in range(0, 4):
        # If the element is a key in the sequenceObject
        if (sequence[i] in sequenceObject):
            # Then increment by one
            sequenceObject[sequence[i]] += 1
        else:
            # Otherwise, set it equal to one
            sequenceObject[sequence[i]] = 1
    # For every key in the sequenceObject
    for key in sequenceObject:
        # If any of the values resulted from their respective key is greater than 1
        if sequenceObject[key] > 1:
            # Return false
            return False
    # Otherwise return true
    return True

# Check if every element in the sequence is a valid character
def validCharacters(sequence):
    # Looping through the entire sequence
    for i in range(0, 4):
        # If any of the element is not of type int
        try:
            int(sequence[i])
        except ValueError:
            return False
    return True

# Formats the result into a cleaner formate
def format_result(result, guess, attempt):
    bowlNumber = str(result["Bowl"])
    strikeNumber = str(result["Strike"])
    printGuess = concatenate(guess)
    print("ATTEMPT #" + str(attempt) + " Guess: " + printGuess + " Result: " + bowlNumber + "B" + strikeNumber + "S")


# Concatenates the array into a string
def concatenate(array):
    resultString = ""
    # Looping through the entire array
    for i in range(0, 4):
        # Formatting the element of the array into a string bfore adding it to the resulting string
        resultString += str(array[i])
    return resultString

def print_statistics(history):
    # For every entry in the history
    for i in range(0, len(history)):
        guess = history[i]["Sequence"]
        result = history[i]["Result"]
        attempt = i + 1
        format_result(result, guess, attempt)

main()
