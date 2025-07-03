from itemName_generator import ItemNameGenerator

class TypeGenerator:
    def __init__(self):
        self.itemName_gen = ItemNameGenerator('items.txt')

    def typeIdentity(self, item_name): 
        type_name = item_name.split(" ")
        if len(type_name) == 1:
            type = 'Coffee'
        else:
            if type_name[len(type_name) -1] == 'Cake' or type_name[len(type_name) -1] == 'Cheesecake':
                type = 'Cake'
            else:
                type = 'Coffee'
        return type
    
