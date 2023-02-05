# 1512. Number of Good Pairs
# Input: nums = [1,2,3,1,1,3]
# Output: 4

def mostWordsFound(self, sentences):
        count = []
        for i in sentences:
            A = i.split(" ")
            count.append(len(A))
        return max(count)

''' First take the each sentence from sentences list 
and split the words into a list, count the words for each sentence 
and find maximum words'''