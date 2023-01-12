from random import choice

fruit = {
    "apple":  0.50,
    "banana": 1.00,
    "orange": 1.50,
    "pear":   0.75,
    "kiwi":   0.30,
    "grape":  0.10,
    "tomato": 0.65,
}

def pick_fruit(num):
    total_price = 0.0
    all_fruit = list(fruit.keys())
    for i in range(num):
        a_fruit = choice(all_fruit)
        price = fruit[a_fruit]
        print(f'{a_fruit:10s} ${price:.2f}')
        total_price += price
    return total_price

total_price = pick_fruit(10)
print(f'\nTotal price: ${total_price:.2f}')