def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in alphabet:
        if char not in sentence:
            return False

    return True


# Main Program
if __name__ == "__main__":
    text = input("Enter a sentence: ")

    if is_pangram(text):
        print("It is a Pangram")
    else:
        print("It is not a Pangram")