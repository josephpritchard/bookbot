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
#    chars_sorted_list = []
#    for k, v in split_d.items():
#        if char.isalpha():
#            chars_sorted_list.append(dict([(k, v)]))
#    return chars_sorted_list
    return split_d
