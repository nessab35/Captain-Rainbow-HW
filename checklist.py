'''Starting Rainbow Checklist'''
# create our checklist

checklist = []
function_code = True

# CREATE
def create(item):
    '''Create item'''
    checklist.append(item)

# READ
def read(index):
    '''Reads index'''
    return checklist[int(index)]


# UPDATE
def update(index, item):
    '''Updates list'''
    checklist[index] = item


# DESTROY
def destroy(index):
    '''Destroys item in list'''
    checklist.pop(index)


def list_all_items():
    '''Lists all items'''
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1


def mark_completed(index):
    '''Marks the item complete'''
    checklist[index] = '✓' + checklist[index]


def user_input(prompt):
    '''User imput'''
    return input(prompt)



def select(function_code):
    '''Selects item'''
    while True:
        function_code = input("Press A to add to list, R to read an item, U to update item, D to destroy an item, C to mark as Completed, P to show list,  and Q to quit>> ")

        # ADD to list
        if function_code == "A" or function_code == "a":
            input_item = input("Add to list:")
            create(input_item)

        # READ from List
        elif function_code == "R" or function_code == "r":
            item_index = int(input("Index Number? "))
            item = read(item_index)
            print(item)

        # UPDATE item
        elif function_code == "U" or function_code == "u":
            index = int(user_input(("Index Number? ")))
            new_item = user_input("Enter new item: ")
            update(index, new_item)

        # DESTROY item
        elif function_code == "D" or function_code == "d":
            index = int(user_input("Index number? "))
            destroy(index)

    # MARK COMPLETED
        elif function_code == "C" or function_code == "c":
            index = int(user_input("Index Number? "))
            mark_completed(index)

        # SHOW list
        elif function_code == "P" or function_code == "p":
            list_all_items()

        # QUIT
        elif function_code == "Q" or function_code == "q":
            break
        else:
            print("Unknown Option")

select(function_code)

#def test():
    #create("purple sox")
    #create("red cloak")
    #print(read(0))
    #print(read(1))
   # update(0, "purple socks")
    #destroy(1)
    #print(read(0))
    #list_all_items()
# test()
