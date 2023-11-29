input_word = input().strip()
data_word = open("data.txt", "r").read().strip()
word_list = set(open("words.txt", "r").read().split())

conditions = [
    input_word in word_list,
    data_word in word_list,
    input_word == data_word
]

print("\n".join(map(lambda x:"true" if x else "false", conditions)))
