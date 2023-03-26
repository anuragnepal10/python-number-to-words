# MODULES

import os


# CONSTANTS

TITLE_WIDTH = 32
CENTER = 130
TITLE = "NUMBER TO WORD CONVERTER"
CLEAR = "cls"
DELAY = 0.2


# DICTIONARIES

dict_once = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10: "ten",
    11: "eleven",
    12: "tweleve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

dict_tens = {
    2 : "twenty",
    3 : "thirty",
    4 : "forty",
    5 : "fifty",
    6 : "sixty",
    7 : "seventy",
    8 : "eighty",
    9 : "ninety"
}

dict_place_value = {
    0 : "thousand",
    1 : "lakh",
    2 : "crore",
    3 : "arab",
    4 : "kharab"
}


# TECHNICAL FUNCTIONS

def title():
    os.system(CLEAR)
    print(("-"*TITLE_WIDTH).center(CENTER))
    print(TITLE.center(CENTER))
    print(("-"*TITLE_WIDTH).center(CENTER))
    print("\n\n")

def play_again():
    
    # time.sleep(DELAY)
    play_again = True
    print("\n\nConvert Another Number?\nPress 'Enter' to continue\nPress 'q' to quit")
    user_choice = input()
    
    if user_choice.lower() == "q":
        play_again = False
    
    return play_again

def input_number():
    
    while True:
        num = input ("Enter a Number: ")
        if num.isdigit():
            num = int(num)
            if 0<=num<=9999999999999:
                break
            else:
                print("Number MUST BE Non Negative AND Less than 10000000000000 !!".center(CENTER))
        else:
            print("Invalid Input !!".center(CENTER))

    return num


# APPLICATION FUNCTIONS

def build_list():
    
    list = []
    for i in range(100):
        if i == 0:
            list.append("")
        elif i < 20:
            list.append(dict_once[i])
        else:
            s1 = int(str(i)[0])
            s2 = int(str(i)[1])
            if s2 == 0:
                list.append(dict_tens[s1])
            else:
                temp = f"{dict_tens[s1]}-{dict_once[s2]}"
                list.append(temp)
    return list


# MAIN FUNCTION

def main():
    
    title()
    num = input_number()
    
    if num == 0:
        s = "Zero"
        
    else:    
        basic_list = build_list()
        f2 = int(str(num)[-2:])
        s = basic_list[f2]
        f3 = int(str(num)[-3])
        
        if f3 != 0 and s != "":
            s = f"{dict_once[f3]} hundred {s}"
        elif f3 !=0 and s == "":
            s = f"{dict_once[f3]} hundred"

        if num > 999:
            rem_num = int(str(num)[:-3])
            final_list = []
            
            if len(str(rem_num)) % 2 == 1:
                final_list.append(int(str(rem_num)[0]))
                srem_num = str(rem_num)[1:]
            else:
                srem_num = str(rem_num)

            while srem_num != "":
                temp = int(srem_num[:2])
                final_list.append(temp)
                srem_num = srem_num[2:]
            
            final_list.reverse()

            for i,num in enumerate(final_list):

                if num !=0:
                    s = f"{basic_list[num]} {dict_place_value[i]} {s}"

    print()
    print(s.capitalize()+".")  

# EXECUTION

if __name__ == "__main__":

    while True:
        
        main()
        if not play_again():
            break