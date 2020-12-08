STOP_WORDS = [
    ' a ', ' an ', ' and ', ' are ', ' as ', ' at ', ' be ', ' by ', ' for ', 'from', 'has', ' he ',
    ' i ', ' in ', ' is ', ' it ', ' its ', ' of ', ' on ', ' that ', ' the ', ' to ', ' were ',
    'will', 'with'
]
punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
# punc = [
#     '!', '?', ',', '.'
# ]
file = open("praise_song_for_the_day.txt", "r")
# print(file.read().lower().replace('?', ""))
read_file = file.read().lower()
# print(read_file)


# file.translate(None, file.punc)
# print(file.read().lower().replace('?', ""))
# remove_stop_words(STOP_WORDS, file)



def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    pass


# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)


def remove_stop_words(stop_words_list, file):
    for word in stop_words_list:
        if word in file:
            file=file.replace(word, " ")
    return file

def remove_punctuation(punc, file):
    for element in punc:
        if element in file:
            file=file.replace(element, " ")
    return file


data_text = remove_stop_words(STOP_WORDS, read_file)
print(data_text)
final_text = remove_punctuation(punc, data_text)
print(final_text)

# from collections import Counter
# def word_count(poem):
#     with open(final_text) as f:
#         return Counter(f.read().split())
# print("number of words in the file : ", word_count(final_text))

final_text_split = final_text.split()
print(final_text_split)