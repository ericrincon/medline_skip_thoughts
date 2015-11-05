__author__ = 'ericrincon'

from nltk.tokenize import sent_tokenize

def preprocess_medline():
    #Open file but read line by line.
    #Where each line is an abstract.

    processed_text = open('skip_thoughts_medline.txt', 'a')

    with open('/work/03186/ericr/data/skip-thought/medline_titles_abstracts.txt') as file:
        for line in file:
            #Ignore the title of the medline abstract
            abstract = line[line.find('.')+2:].decode('utf-8')

            tokenized_abstract = sent_tokenize(abstract)

            #Write abstracts to new file line by line in a contiguous text.
            for sentence in tokenized_abstract:
                processed_text.write(sentence.encode('utf') + '\n')

            #Add an end of document token
            processed_text.write('<eod>.\n')


def main():
    preprocess_medline()

if __name__ == '__main__':
    main()
