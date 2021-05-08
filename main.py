all_items = []


def create_shop_items():
    item_colors = ['pink', 'green', 'black', 'white', 'green', 'red', 'blue', 'yellow', 'orange', 'purple']
    item_sizes = ['XS', 'S', 'M', 'L', 'XL', 'XXL']
    item_types = ['shirt', 'scarf', 'glove', 'jeans', 'dress', 'skirt', 'blouse']

    for x in item_types:
        for y in item_colors:
            for z in item_sizes:
                all_items.append('[' + x + ',' + y + ',' + z + ']')

    print(all_items)
    print(all_items.__len__())


def sell_last_item():
    all_items.pop()
    print(all_items)
    print(all_items.__len__())


def sell_any_item(item_to_be_sold):
    if item_to_be_sold in all_items:
        all_items.remove(item_to_be_sold)

    print(all_items)
    print(all_items.__len__())


def restock_shop():
    item_colors = ['black', 'white', 'red', 'blue']
    item_sizes = ['XS', 'S', 'M', 'L', 'XL', 'XXL']
    item_types = ['hat', 'jacket']

    for x in item_types:
        for y in item_colors:
            for z in item_sizes:
                all_items.append('[' + x + ',' + y + ',' + z + ']')

    print(all_items)
    print(all_items.__len__())


if __name__ == '__main__':
    create_shop_items()
    sell_last_item()
    sell_any_item('[shirt,pink,L]')
    restock_shop()
