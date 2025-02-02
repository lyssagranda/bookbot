def main():
    path = "/Users/LBG/workspace/github.com/lyssagranda/bookbot/books/frankenstein.txt"
    text = get_book_text(path)
    words = word_count(text)
    characters = character_count(text)
    sorted_characters = list_dict(characters)
    for item in sorted_characters:
        print(f"Character: '{item['character']}', Count: {item['count']}")

def get_book_text(path):
    with open(path) as file:
        text = file.read()
    return text

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_count = {}
    lowercase = text.lower()
    for char in lowercase:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_key(item):
    return item['count']

def list_dict(char_count):
    list_chr = []
    for char, count in char_count.items():
        if char.isalpha():
            list_chr.append({'character': char, 'count': count})
    
    sorted_list = sorted(list_chr, reverse=True, key=sort_key)
    return sorted_list

main()