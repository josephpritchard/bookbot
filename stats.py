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

def sort_key(num):
    return items["num"]

def sort_dict(d):
    d2 = d.sort(reverse=True, key=sort_key)
    return d2
