my_list = ["1", 2, 3, 4, 5, "1"]
my_plenty = set(my_list)
if len(my_list) == len(my_plenty):
    print("All list items are unique")
else:
    print("The list contains duplicate items")