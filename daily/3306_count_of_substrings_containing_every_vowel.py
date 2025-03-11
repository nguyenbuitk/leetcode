def countOfSubstrings(self, word: str, k: int) -> int:
    dict = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }
    # abc[xxyz]mnip || k = 2 
    count_consonant = 0
    res = 0
    l = 0
    for i in range(word):
        if word[i] not in dict:
            count_consonant += 1
            if min(dict.values()) == 0:
                if count_consonant > k:
                    for key in dict:
                        dict[key] = 0
                    count_consonant = k
            else: # min(dict) == 1
                if count_consonant >= k:
                    count_consonant = k - 1
                    res += 1
                # if count_consonant < k
                count_consonant += 1
        else: 
            dict[word[i]] += 1
            if min(dict.values()) > 0 and count_consonant >= k:
                res += 1
                count_consonant = k - 1