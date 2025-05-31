# obtain a list of files in the input directory
# Ctrl Shift L
# Ctrl Alt Flecha arriba/abajo


from homework.src._internals.read_all_lines import read_all_lines
from homework.src._internals.preprocess_lines import preprocess_lines
from homework.src._internals.split_into_words import split_into_words
from homework.src._internals.count_words import count_words

from ._internals.write_word_counts import write_word_counts

def main():

    # Read
    all_lines = read_all_lines()

    # Preprocess
    all_lines = preprocess_lines(all_lines)

    # Split
    words = split_into_words(all_lines)

    # Count
    counter = count_words(words)

    # count the frequency of the words in the files in the input directory
    # counter={}
    # for filename in input_file_list:
    #     with open('data/input/'+filename) as f:
    #         for l in f:
    #             for w in l.split( ):
    #                 w = w.lower().strip(",.!?")
    #                 counter[w] = counter.get(w, 0) + 1

    write_word_counts(counter)

if __name__ == "__main__":
    main()