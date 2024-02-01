import pandas

try:
    nato_file = pandas.read_csv("nato_phonetic_alphabet.csv")
except FileNotFoundError:
    print("File was not found!")
else:
    try:
        word = input("Enter a word: ")
    except KeyError:
        print("Invalid word was entered!")
    else:
        nato_student_data = [nato_file[nato_file.letter == letter.upper()].code.item() for letter in word]
        nato_student_dict = {letter.upper(): nato_file[nato_file.letter == letter.upper()].code.item() for letter in word}
        print(nato_student_data)
        print(nato_student_dict)
