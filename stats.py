import sys
with open(sys.argv[1]) as f:
    get_book_text = f.read()
get_num_words = 0
get_words = get_book_text.split()
for word in get_words:
    get_num_words += 1
word_count = get_num_words


lowercase_book_text = get_book_text.lower()
char_counts = {}
for char in lowercase_book_text:
    if char.isalpha() == True:
        char_counts[char] = char_counts.get(char, 0) + 1

sorted_char_count = sorted(char_counts.items(), reverse=True, key=lambda kv: (kv[1], kv[0]))

list = ""

for tuple in sorted_char_count:        
    list += (f"{tuple[0]}: {tuple[1]}\n")

