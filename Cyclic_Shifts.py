# ---------------------------------------------------------------------------
# Cyclic Shifts
# ---------------------------------------------------------------------------

# Get input from the user for Text
def get_text():
    while True:
        text = input("Enter in text using capitals only: ")
        if text.isupper() == False:
            print("Text must all be in uppercase")
            continue
        else:
            break
    return text


# Get input from the user for String
def get_string():
    while True:
        string = input("Enter in text to perform cyclic shift using capitals only: ")
        if string.isupper() == False:
            print("Text must all be in uppercase")
            continue
        else:
            break
    return string


# Work out if T contains a cyclic shift of S
def get_combinations(text, string):
    possible_combinations = []
    for i in range(len(string)):
        if i == 0:
            possible_combinations.append(string)
        else:
            string = string[1:] + string[0]
            possible_combinations.append(string)
    return possible_combinations


# Return Output
def cyclic_shift(combinations, text):
    for combination in combinations:
         if combination in text:
            return True
         else:
            continue
    return False


# Main Loop
def main_loop():
   text = get_text()
   string = get_string()
   combinations = get_combinations(text, string)
   result = cyclic_shift(combinations, text)
   if result:
      print("Yes")
   else:
      print("No")


# Replay Prompt
if __name__ == '__main__':
    while True:
        main_loop()
        while True:
            answer = input('Again? (Y/N): ')
            if answer.upper() in ('Y', 'N'):
                break
            print('\nInvalid input\n')
        if answer.upper() == 'Y':
            continue
        else:
            break
