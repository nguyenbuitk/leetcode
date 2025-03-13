from typing import List
def suggestdProducts(products: List[str], searchWord: str):
    res = []
    products.sort()
    for i in range(len(searchWord)):
        word = searchWord[:i+1]
        count = 0
        list_product = []
        for product in products:
            if product[:i+1] == word:
                list_product.append(product)
                count += 1
            if count == 3:
                break
        res.append(list_product)
        print(f"word: {word}, list_product: {list_product}")
    return res
print(suggestdProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))