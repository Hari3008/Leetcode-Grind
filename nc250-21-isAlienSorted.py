class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # check if the word is a prefix of the other
        orderInd = {c:i for i,c in enumerate(order)}

        # traverse through the words
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]

            for j in range(len(w1)):
                # Check if w2 is a prefix of w1, then just return False
                if j == len(w2):
                    return False
                
                # Check for differing char in both the strings
                if w1[j]!= w2[j]:
                    if orderInd[w2[j]] < orderInd[w1[j]]:
                        return False
                    break
                
        return True

