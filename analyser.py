#!/usr/bin/python3

"""
Contains code to perform various analysis of ciphertext
"""

import itertools
import string
import tests
from abc import ABC, abstractmethod

class UnequalDomainException(Exception):
    pass


class Analyser(ABC):

    @abstractmethod
    def init_n_grams(self, n, domain):
        pass


    def count_frequency(self, source):
        """
        counts the frequency of each character in source.
        source param can be both string and bytes object.
        returns dictionary with frequency for each character
        """
        freqs = {}
        for i in source:
            freqs[i] = freqs.get(i, 0) + 1

        for key, val in freqs.items():
            freqs[key] = val/len(source)*100

        return freqs


    def count_frequency_distance(self, frequency_dic1, frequency_dic2):
        """
        computes the distnace of two given occurence frequencies
        :param frequency_dic1:
        :param frequency_dic2:
        :return:
        """
        # check if the frequency dictionaries have the same base
        if set(frequency_dic1.keys()) != set(frequency_dic2.keys()):
            raise UnequalDomainException

        total = 0

        for i in frequency_dic1.keys():
            distance = abs(frequency_dic1[i] - frequency_dic2[i])
            total += distance

        return total//2



    def n_gram_analysis(self, source, n, domain):
        n_grams = self.init_n_grams(n, domain) # create relevant n grams - byte vs letter

        for i in n_grams:
            # find occurences, return object with
            # number of occurences, list of occurence positions,
            # and gcd of all pairs of occurences - this is then used by
            # higher level function
            #occurences(source, i)
            # gcds(list of occs)
            pass


class StringAnalyser(Analyser):

    def init_n_grams(self, n, domain):
       print('in string analyser init_n_grams method')
       return [ ''.join(i) for i in itertools.product(domain, repeat=n)]

class ByteAnalyser(Analyser):

    def init_n_grams(self, n, domain):
        print('in byte analyser init_n_grams method')
        return [ b''.join(i) for i in itertools.product(domain, repeat=n)]


if __name__ == "__main__":
    pass