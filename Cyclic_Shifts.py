# ---------------------------------------------------------------------------
# Cyclic Shifts
# ---------------------------------------------------------------------------

# Get input from the user for Text
def get_text():
    text = input("Enter in text as T using capitals only: ")


# Get input from the user for String
def get_string():
    string = input("Enter in text as S using capitals only: ")


# Work out if T contains a cyclic shift of S
def get_combinations(text, string):
    possible_combinations = []
    for i in range(len(string)):
        if i == 0:
            possible_combinations.append(string)
        else:
            string = string[1:] + string[0]
            possible_combinations.append(string)
    print(possible_combinations)


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
