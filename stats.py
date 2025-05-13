def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_characters(text):
    counts = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts


def get_sorted_nums(nums_dict):
    nums_list = [{"char": char, "num": num} for char, num in nums_dict.items()]
    nums_list.sort(key=lambda x: x["num"], reverse=True)
    return nums_list
