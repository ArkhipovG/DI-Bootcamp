# Exercise 1
word = input("Enter a word: \n")
word_dict = {}
for index, letter in enumerate(word):
    letter = str(letter)
    if letter in word_dict:
        word_dict[letter].append(index)
    else:
        word_dict[letter] = [index]

print("Dictionary storing indexes of each letter:")
print(word_dict)

# Exercise 2
def affordable(items_purchase, wallet):
    cost = None
    affordable_items = []
    balance = int(wallet.replace('$', '').replace(',', ''))
    for key, value in items_purchase.items():
        cost = int(value.replace('$', '').replace(',', ''))
        if balance > cost:
            affordable_items.append(key)
            balance = balance - cost

    affordable_items.sort()
    if affordable_items != []:
        print(affordable_items)
    else:
        print('Nothing')


affordable(items_purchase = {
  'Water': '$1',
  'Bread': '$3',
  'TV': '$1,000',
  'Fertilizer': '$20'
}, wallet = '$300')

affordable(items_purchase = {
  'Apple': '$4',
  'Honey': '$3',
  'Fan': '$14',
  'Bananas': '$4',
  'Pan': '$100',
  'Spoon': '$2'
}, wallet = '$100')

affordable(items_purchase = {
  'Phone': '$999',
  'Speakers': '$300',
  'Laptop': '$5,000',
  'PC': '$1200'
}, wallet = '$1')



