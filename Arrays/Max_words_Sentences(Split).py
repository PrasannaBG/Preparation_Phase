def mostWordsFound(self, sentences):
        count = []
        for i in sentences:
            A = i.split(" ")
            count.append(len(A))
        return max(count)

''' First take the each sentence from sentences list 
and split the words into a list, count the words for each sentence 
and find maximum words'''