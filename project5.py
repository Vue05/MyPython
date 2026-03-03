fruits_to_buy = ["grapes", "oranges", "pomegranate"]
# to access or print a specific item in the list
# the minus(-) trick can also be used to access or print items in the list but begins counting from the end of the list and then progresses forward

print(fruits_to_buy[2])
# to change and item in a list, like the spelling or so
fruits_to_buy[0] = "drapes"
print(fruits_to_buy)
# to add an item to the list
fruits_to_buy.append("avocado")
print(fruits_to_buy)
# also used to access or print items in the list but begins counting from the end of the list and then progresses forward
fruits_to_buy[0] = "grapes"
print(fruits_to_buy)
# to add multiple items to the list, like another list to the already existing one
fruits_to_buy.extend(["apples", "strawberry"])
print(fruits_to_buy)