#!/usr/bin/python3.4
# coding: utf8
import sys
import random
class NewWord():
    """Class creating a new word"""
    def __init__(self, shortest_word, longest_word, random_1, chce_frst_ltr, mid_size):
        """Initializing word"""
        self.size = mid_size + random.randint(-(mid_size - shortest_word), (longest_word - mid_size))
        i = 0
        while i < len(chce_frst_ltr):
            if random_1 <= chce_frst_ltr[i][1]:
                self.first_letter = chce_frst_ltr[i][0]
                break
            i += 1
    def create_word(self, chance_after_letter, chce_frst_ltr, doubling_letter_chance, shortest_word, longest_word, list_longests, list_shortests):
        """Creating the word"""
        i = 0
        final_word = str()
        final_word += self.first_letter
        if self.size != shortest_word and self.size != longest_word:
            while i < (self.size - 1): # -1 cause of first letter
                random_number = random.randrange(len(chance_after_letter[final_word[i]]))
                new_letter = chance_after_letter[final_word[i]][random_number]
                if new_letter == ' ':
                    final_word += new_letter
                    self.size = len(final_word)
                else:
                    final_word += new_letter
                i += 1
                # g = 0
                # try:
                    # while g < len(chance_after_letter[final_word[i]]):
                    #     if random_number <= chance_after_letter[final_word[i]][g][1]:
                    #         final_word += chance_after_letter[final_word[i]][g][0]
                    #         if(chance_after_letter[final_word[i]][g][0] in doubling_letter_chance) and (random.randrange(100) <= doubling_letter_chance[chance_after_letter[final_word[i]][g][0]]):
                    #             final_word += chance_after_letter[final_word[i]][g][0]
                    #             i += 1
                    #         break
                    #     g += 1
                #
                # except KeyError:
                #     pass
        
        if self.size <= shortest_word:
            final_word = list_shortests[random.randrange(len(list_shortests))]
        elif self.size >= longest_word:
            final_word = list_longests[random.randrange(len(list_longests))]
        # final_word = final_word.replace(' ', '')
        return final_word
