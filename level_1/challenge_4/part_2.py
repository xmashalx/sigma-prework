#https://leetcode.com/problems/top-k-frequent-words/
#top frequent words solution: 
class Solution(object):
    def topKFrequent(self, words, k):
        word_count = dict()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        sorted_word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
        most_freq = [word for word, _ in sorted_word_count[:k]]
        return most_freq

#https://leetcode.com/problems/decode-the-message/description/
#decode the message solution:
import string
class Solution(object):
    def decodeMessage(self, key, message):
        decoder=[]
        for character in key:
            if character != ' ' and character not in decoder:
                decoder.append(character)
        alphabet = list(string.ascii_lowercase)
        result_dict = dict(zip(decoder, alphabet))
        
        answer=[]
        for char in message:
            if char.isalpha():
                answer.append(result_dict[char])
            else:
                answer.append(char)
        return ''.join(answer)


#https://leetcode.com/problems/roman-to-integer/description/
#roman to integer solution:
class Solution(object):
    def romanToInt(self, s):
        dictionary={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        number=0
        for i in range(len(s)-1):
            if dictionary[s[i]]<dictionary[s[i+1]]:
                number-=dictionary[s[i]]
            else:
                number+=dictionary[s[i]]
        number += dictionary[s[-1]]

        return number
