import fuzzy

import inventory

import speech_recognition as sr


soundex = fuzzy.Soundex(5)

import Levenshtein as lev
# import fuzzy

def match_string(input_string, string_list):
    # Initialize variables
    best_match = ""
    best_score = 0
    
    # Calculate soundex code for input string
    soundex = fuzzy.Soundex(4)
    input_soundex = soundex(input_string)

    # Loop through list of strings
    for string in string_list:
        # Calculate Levenshtein distance between input string and list string
        score = lev.ratio(input_string.lower(), string.lower())
        
        # Calculate soundex code for list string
        string_soundex = soundex(string)

        # Calculate Levenshtein distance between input soundex and list string soundex
        soundex_score = lev.ratio(input_soundex.lower(), string_soundex.lower())

        # Calculate combined score
        combined_score = score + soundex_score

        # Check if combined score is better than previous best score
        if combined_score > best_score:
            best_match = string
            best_score = combined_score
    
    return best_match


# obtain audio from the microphone

def my_listener():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        print("Google Speech Recognition thinks you said: " + r.recognize_google(audio))
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return 0
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return e



items_list = inventory.get_all_items()
print(items_list)
item_list = []
for i in items_list:
    item_list.append(i[1])

# mycodes = []

# for my_item in items_list:
#     mycodes.append(soundex(my_item[1]))

# print(mycodes)
while 1:
    i = input()
    if i == "q":
        break
    else:
        # print("Say")
        input_text = my_listener()
        print(input_text.replace("comma", ","))
        matched_string = match_string(input_text, item_list)
        print(matched_string)
        # if soundex(input_text) in mycodes:
        #     idx = mycodes.index(soundex(input_text))
        #     print(items_list[idx])
        
        # else:
        #     print("donot match")
