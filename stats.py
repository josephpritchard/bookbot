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
    return item["num"]

def sort_dict(new_d):
    split_d = []
    for k, v in new_d.items():
        split_d.append(dict([("char", k), ("num", v)]))
    split_d.sort(reverse=True, key=sort_key)
    return split_d

def get_word_len(file_contents):
#    lowered_text = file_contents.lower()
#    sorted_text = sorted(lowered_text)
    d7 = {"Seven Letter Words":
          {"Number": 0,
           "Words": []}
          }
    words = file_contents.split()
    for word in words:
        if (len(word) == 7) & (len(d7["Seven Letter Words"]["Words"]) < 10):
            d7["Seven Letter Words"]["Number"] += 1
            d7["Seven Letter Words"]["Words"].append(word) 
    return d7
