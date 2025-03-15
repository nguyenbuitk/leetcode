from utils import *
def totalNumbers(digits: List[int]) -> int:
    list_even_number = set()
    count = 0
    dict = Counter(digits)
    for digit in digits:
        if digit % 2 == 0:
            list_even_number.add(digit)
    print(f"list even number: {list_even_number}")
    for number in list_even_number:
        dict[number] -= 1
        if dict[number] == 0:
            dict.pop(number)
        
        number_duplicate = 0
        for k, v in dict.items():
            if v >= 2 and k != 0:
                number_duplicate += 1
                
            
        
            
        list_dictict_number = set(dict.keys())
        print(f"after pop {number}, list dicitict number: {list_dictict_number}")
        n = len(list_dictict_number)
        if 0 in list_dictict_number:
            count += (n-1)*(n-1)
        else:
            count += n*(n-1)
        
        dict[number] = dict.get(number, 0) + 1
    return count + number_duplicate
print(totalNumbers([4,7,7,3]))