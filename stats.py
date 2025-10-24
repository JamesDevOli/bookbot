def get_num_words(text):
    word_list = text.split()
    return len(word_list)

def character_count(text):
    ch_count = {}
    lower_text = text.lower()
    for ch in lower_text:
        if ch in ch_count:
            ch_count[ch] = ch_count[ch] + 1
        else:
            ch_count[ch] = 1
    return ch_count

def sort_on(i):
    return i["num"]

def sort_count(ch_count):
    sorted_list = []
    for ch in ch_count:
        sorted_list.append({"char": ch, "num": ch_count[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list