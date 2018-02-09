import sys  # import libraries
import re
import collections
import csv
file = open(sys.argv[1], 'r').read()  # open file by console argument
match_dict = {}  # empty dict for matching regex where <HTTP response code> will
                 # be key and count of frequency request showed

comp = re.compile(r'//.+HTTPS?/[0-255].[0-255]')  # first regex to match <HTTP response code>
comp_2 = re.compile('\w.*?(\w|/)(\?|\s)')  # second regex to match response
matching = comp.findall(file)  # we use first regex
for el in matching:
    found_url = comp_2.search(el).group(0)  # in part of text from first regex search part from second regex
    found_url = found_url.rstrip()  # delete space from the end of string

    if found_url[-1] == '?' and found_url[-2] == '/':   # delete no needed first sign's like "/" or "?"
        found_url = found_url[:len(found_url) - 2]
    elif found_url[-1] == '?' or found_url[-1] == '/':
        found_url = found_url[:len(found_url) - 1]
    if found_url not in match_dict.keys():  # if <HTTP response code> don't exist in "match_dict"
                                            # we add first existing with
                                            # counter of existing :1
        match_dict[found_url] = 1
    else:
        match_dict[found_url] += 1  # if string of <HTTP response code> already exist
                                    # in dict we add 1 to his counter/value

sorted_phrases = collections.OrderedDict(sorted(match_dict.items(), key=lambda el_in_dict: el_in_dict[0])) # sort by name lexicographically
sorted_phrases_2 = collections.OrderedDict(sorted(sorted_phrases.items(), key=lambda el_in_dict: el_in_dict[1], reverse=True)) # sort by counter desc
writer = csv.writer(sys.stdout)  # create std output to csv
for key, val in sorted_phrases_2.items():
    writer.writerow([key, val])  # write key and value from dictionary too csv
