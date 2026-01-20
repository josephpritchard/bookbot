def get_word_num(file_contents):
    word_count = len(file_contents.split())
    return word_count

def get_char_stats(file_contents):
    lowered_text = file_contents.lower()
    sorted_text = sorted(lowered_text)
    d = {}
    for char in sorted_text:
        if char not in list(d):
            d[char] = 1
        else:
            d[char] += 1
    return d

def sort_key(item):
    return item["char"]

def sort_dict(new_d, rev_bool):
    split_d = []
    for k, v in new_d.items():
        split_d.append(dict([("char", k), ("num", v)]))
    split_d.sort(reverse=rev_bool, key=sort_key)
    return split_d

def get_word_len(file_contents):
#    lowered_text = file_contents.lower()
#    sorted_text = sorted(lowered_text)
    d7 = {"Seven Letter Words":
          {"Number": 0,
           "Words": []}
          }
    d7_words = d7["Seven Letter Words"]["Words"]
    words = file_contents.split()
    for word in words:
        if (len(word) == 7):
            d7_words.append(word) 
    d7["Seven Letter Words"]["Words"] = set(d7_words)
    d7["Seven Letter Words"]["Number"] = len(d7_words)
    return d7

def get_word_lengths(file_contents):
    words = file_contents.split()
    d_lengths = {}
    for word in words:
        if len(word) not in d_lengths:
            d_lengths[len(word)] = 1
        else:
            d_lengths[len(word)] += 1
    return d_lengths

def get_longest_words(file_contents):
    d_longest = {}
    words = file_contents.split()
    for i in range(17, 33):
        d_longest[i] = []
        for word in words:
            if len(word) == i:
                d_longest[i].append(word)
    return d_longest
#    for i in range(2):
#        character = d["char"]
#        count = d["num"]
#        print(f"{character}: {count}")
