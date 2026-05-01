
units = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19
}

tens = {
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
}

multipliers = {
    "hundred": 100, "thousand": 1000
}

def words_to_num(text):
    text = text.lower().replace("-", " ").replace(" and", "")
    words = text.split()
    
    num = 0
    current = 0
    
    for word in words:
        if word in units:
            current += units[word]
        elif word in tens:
            current += tens[word]
        elif word == "hundred":
            current *= 100
        elif word == "thousand":
            current *= 1000
            num += current
            current = 0
        else:
            raise ValueError(f"Unknown word: {word}")
    
    num += current
    return num


text_num = input("Enter a number in words: ")
try:
    result = words_to_num(text_num)
    print("Numerical format:", result)
except ValueError as e:
    print(e)
