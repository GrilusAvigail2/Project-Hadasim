from collections import Counter
import re


class StatisticData:
    filename = ""

    # 1. Counts how many lines are in the file
    def count_rows(self):
        lines = self.filename.readlines()
        if lines != ' ':
            # print(lines)
            # for line in lines:  # remove all the new lines
            #     if line == '\n':
            #         lines.remove(line)
            str = '1. The number of lines in the file :{} \n'.format(len(lines))
        else:
            str = "Error, the file is empty"
        return str

    # 2. Counts how many words are in the file
    def count_words(self):
        data = self.filename.read()  # returned all the data in the file
        if data != ' ':
            words = data.split()  # remove all the white spaces
            str = '2. The number of words in the file :{} \n'.format(len(words))
        else:
            str = "Error, the file is empty"
        return str

    # 3. Counts how many unique words are in the file
    def count_unique_words(self):
        data = self.filename.read()  # returned all the data in the file
        if data != ' ':
            data = data.lower()  # convert the data to lower case
            words = data.split()  # remove all the white spaces
            dict_counter = Counter(words)  # the occurrence count of each item in the list
            # print(dict_counter)
            count_unique = 0  # counter for the words that appear once
            for key, value in dict_counter.items():  # iterate on the dictionary items
                if value == 1:  # value 1 indicates that the word appears once
                    count_unique += 1  # counter promotion in one
            str = '3. there ars {} unique words in the file \n'.format(count_unique)
        else:
            str = "Error, the file is empty"
        return str

    # 4. Returns the average sentence length and maximum sentence length
    def len_avg_max_sentences(self):
        sents = self.filename.read().split(',')  # split the file into sentences
        if sents != ' ':
            sents = [x.strip() for x in sents]  # remove spaces from the beginning and end of the sentence
            sents = [x.replace('\n', " ") for x in sents]  # remove the character '\n' from the sentences
            # print(sents)
            len_sents = [len(x.split()) for x in sents]
            # print(len_sents)
            avg_len = round(sum(len_sents) / len(len_sents), 3)  # average sentence length
            str1 = '4. average sentence length :{} \n'.format(avg_len)
            max_len = max(len_sents)  # maximum sentence length
            str2 = '   maximum sentence length :{} \n'.format(max_len)
        else:
            str1 = "Error, the file is empty"
        return str1 + str2

    # 5. Find the most popular word in the file
    def popular_word(self):
        data = self.filename.read()  # returned all the data in the file
        if data != '':
            data = data.lower()  # convert the data to lower case
            words = data.split()  # remove all the white spaces
            dict_counter = Counter(words)  # the occurrence count of each item in the list
            # print(dict_counter)
            pop_words = []
            maximum = max(dict_counter.values())
            # print(maximum)
            for key, value in dict_counter.items():  # iterate on the dictionary items
                if value == maximum:
                    pop_words.append(key)
            str = '5. The popular word is :{} \n'.format(" ".join(pop_words))

        else:
            str = "Error, the file is empty"
        return str

    # 6.The longest word sequence in a text that does not contain the letter k
    def seq_without_k(self):
        data = self.filename.read()  # returned all the data in the file
        if data != ' ':
            words = data.split()  # remove all the white spaces
            # print(words)
            count = 0
            cur_seq = []
            max_seq = []
            for word in words:
                if 'k' not in word and 'K' not in word:  # if the word does not contain "k" or "K"
                    cur_seq.append(word)  # adding the word to the current sequence
                    count += 1
                else:  # if not, reset the current sequence and the counter
                    cur_seq.clear()
                    count = 0
                if len(max_seq) < len(cur_seq):  # if the max sequence shorter than the current sequence
                    max_seq = cur_seq.copy()  # copy to the max sequence the current sequence to save the longest sequence
            str = '6. The longest word sequence without "k" :{} \n'.format(" ".join(max_seq))
        else:
            str = "Error, the file is empty"
        return str

    # 7. The largest number specified in the file
    def largest_number(self):
        lst_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                       'twelve',
                       'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
                       'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand',
                       'million',
                       'billion', 'trillion']
        data = self.filename.read().lower()  # returned all the data in the file
        if data != ' ':
            words = re.split(r"[-;:,.\s]\s*", data)  # returned the words without whitespaces, comma,dot etc
            # print(words)
            # regex = re.compile(r'^[0-9]+$')
            reg = re.compile(r'^[0-9]+[,[0-9]+]?$')
            numbers = []
            for word in words:
                # if regex.search(word):
                #     numbers.append(int(word))
                if reg.search(word):
                    numbers.append(word)
            numbers = map(int, numbers)
            str = '7. The largest number is:{} \n'.format(max(numbers))
        else:
            str = "Error, the file is empty"
        return str

    # 8.Color names that appear in the file, and the number of times each one appears
    def count_colors(self):
        data = self.filename.read().lower()  # returned all the data in the file
        words = re.split(r"[-;:,.\s]\s*", data)  # returned the words without whitespaces, comma,dot etc
        # print(words)
        colors = {"blue": 0, "yellow": 0, "red": 0, "green": 0, "pink": 0, "white": 0, "orange": 0, "purple": 0,
                  "gold": 0,
                  "silver": 0, "grey": 0}
        for word in words:  # search a color name in all the words in the file
            if word in colors.keys():  # if the current word is a color from the dictionary colors
                colors[word] += 1  # increase the number of times the color appears
        # print(colors)
        string = "8. colors:" + '\n'
        for key, value in colors.items():  # displays each color and the number of times it appears
            if value == 0:
                continue
            elif value == 1:
                times = 'once'
            elif value == 2:
                times = 'twice'
            else:
                times = str(value) + ' times'
            string += ("    " + str(key) + ' appears ' + times + '\n')
        return string

    def write_to_file(self):  # execute all the function on the file and write the results to a new file
        file = open("statistic_data.txt", "a+")
        file.truncate(0)  # delete the data from the previous file
        file.write(self.count_rows())
        self.filename.seek(0)
        file.write(self.count_words())
        self.filename.seek(0)
        file.write(self.count_unique_words())
        self.filename.seek(0)
        file.write(self.len_avg_max_sentences())
        self.filename.seek(0)
        file.write(self.popular_word())
        self.filename.seek(0)
        file.write(self.seq_without_k())
        self.filename.seek(0)
        file.write(self.largest_number())
        self.filename.seek(0)
        file.write(self.count_colors())
        file.close()

    def make_statistic_on_file(self, filepath):
        try:
            with open(file=filepath, mode="r", encoding='windows-1254') as file:
                self.filename = file
                self.write_to_file()
                data = "The File: " + filepath
                f = open("statistic_data.txt", "r")
                lines = f.readlines()
                for line in lines:
                    data += (line + "\n")
                f.close()
                return data

        except Exception as e:
            return "Error: " + str(e)
