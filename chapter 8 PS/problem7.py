def rem(l, word):
    n = []
    for item in l:
     if not(item == word):
        n.append(item.strip(word)) 
    return n 

l = ["Arbaz", "Ali", "Ahmed", "Ahsan", "Adeel"]

print(rem(l, "Ali"))