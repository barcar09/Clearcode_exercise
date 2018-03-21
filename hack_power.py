 
import unittest
import collections
from re import search, findall  


def hack_calculator(hack: str) -> int:  # basic version of hacker function
    counter = 0  
    counter_dict={'a': 1, 'b': 1, 'c': 1} 
    letters={'a': 1, 'b': 2, 'c': 3}
    if search('[^(a-c)]', hack) is not None:  # searching if there is any no 'a,b,c' letter
                                               
        return 0
    else:
        ffc = len(findall('baa', hack))  # find all 'baa' and 'ba' phrases and counter it
        sfc = len(findall('ba', hack))
        sfc = sfc-ffc  # delete repeating phrases
        counter += 10*sfc+20*ffc  # add value to counter
            
        for el in hack:  
            counter += letters[el]*counter_dict[el]  
            counter_dict[el] += 1
    return counter


def hack_calculator_v2(hack: str, words: dict, phrases: dict)-> int:  # better version of function

    counter = 0  
    counter_dict = {el: 1 for el in words.keys()} 
    letters_str = ''.join(el for el in words.keys()) 
    lst_of_phrase = {}  
    sorted_phrases = collections.OrderedDict(sorted(phrases.items(), reverse=True))  # sort of phrases desc
    longest_phrase = max(len(x) for x in phrases.keys())  # longest phrase
    for el in hack:
        if search(el, letters_str) is None:
            return 0
    for els in hack:
            counter += words[els]*counter_dict[els]
            counter_dict[els] += 1  # in this loop everything like in first function
    for el,val in sorted_phrases.items():
        if len(el) == longest_phrase:
            find_phrase_counter = len(findall(el,hack))  # find all phrases starts from longest
            counter += val*find_phrase_counter  
            lst_of_phrase[el] = find_phrase_counter  # add phrase and value how many times we found it ton"lst_of_phrases"
        else:
            find_phrase_counter_2 = len(findall(el, hack))  # find all phrases that's not the longgest ( they can overlap)
            for els in lst_of_phrase.keys():  # loop through keys to see if there is not overlap
                if search(el, els) is not None:
                    find_phrase_counter_2 -= lst_of_phrase[els]  # if overlap, substract found counter
            counter += val*find_phrase_counter_2 # add not overlap phrase value to counter
            lst_of_phrase[el] = find_phrase_counter_2 # add another phrases to lst_of_phrase that can overlap
    return(counter)


if __name__ == "__main__":  # simple test's
    print(hack_calculator('baaca'))
    print(hack_calculator('babacaba'))
    print(hack_calculator('aabacabaaaca'))
    print(hack_calculator('abc'))
    print(hack_calculator('bad'))
    print(hack_calculator_v2("adam", {'a': 1, 'd': 2, 'e': 3, 'm': 4}, {"adddd": 50, "ada": 10, "am":20, "ad": 30}))
    print(hack_calculator_v2("abbababbbabadddd", {'a': 1, 'b': 2, 'c': 3, 'd': 4}, {"adddd": 50, "ab": 10, "abb": 20, "abbb": 30}))
    print(hack_calculator_v2("wrong", {'a': 1, 'b': 2, 'c': 3, 'd': 4}, {"adddd": 50, "ab": 10, "abb": 20, "abbb": 30}))
    print(hack_calculator_v2("nophrases", {'n': 1, 'o': 2, 'p': 3, 'h': 4, 'r': 5, 'a': 6, 's': 7, 'e': 8},
                            {"adddd": 50, "ab": 10, "abb": 20, "abbb": 30}))
