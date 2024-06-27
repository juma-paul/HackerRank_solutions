from collections import OrderedDict

def main():
    """
    Collects item names and prices, sums up the prices for items with the same name,
    and prints out each unique item name with its total price.
    """
    
    N = int(input('Enter the number of items: '))

    item_dict = OrderedDict()

    for i in range(N):
        *item_name, net_price = input(f'Item no. {i + 1}: ').split()
        item_name = ' '.join(item_name).upper()
        price = int(net_price)

        if item_name in item_dict:
            item_dict[item_name] += price
        else:
            item_dict[item_name] = price
    
    for item_name, net_price in item_dict.items():
        print(f'{item_name} {net_price}')

if __name__ == '__main__':
    main()
