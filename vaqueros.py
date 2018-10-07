from receipt import Receipt

def main():
    print('Let\'s budget shit.')
    options()
    budgeting()

def options():
    print('''
    \t[v] View budget
    \t[a] Add cost
    \t[q] Quit
    \t[u]
    \t[e]
    \t[r]
    \t[o]
    \t[s] Summary
    ''')

def budgeting():
    c = input()
    c = c.upper()
    while c != 'Q':
        if c == 'V':
            view_budget()
        elif c == 'A':
            receipt = add_cost()
            if item_confirmation(receipt):
                print('Congratulations, you have less money.')
            else:
                print('One more thing you don\'t have.')
        elif c == 'S':
            summary()

        options()
        c = input()
        c = c.upper()

def view_budget():
    return

# Details about the cost are acquired, and a receipt for the new cost is
# created. The receipt contains all the information for the new burden on
# the budget. Way2go.
def add_cost():
    item = input('''
===>What item would you like to add?
    ''')
    cost = input('''
=======>How much you dropping?
        ''')
    freq = input('''
===========>How often are you dropping this?
            (daily, weekly, monthly, once)
            ''')
    r = Receipt()
    r.set_item(item)
    r.set_cost(cost)
    r.set_frequency(freq)
    return r

# Confirms with the user if this is something they really want to do. This
# step is important because, most of the time, whatever the user is trying
# to do is not necessary for human life. Water isn't necessary for human
# life.
def item_confirmation(receipt):
    save_item(receipt)
    return True

def save_item(receipt):
    return

def summary():
    return

if __name__ == '__main__':
    main()
