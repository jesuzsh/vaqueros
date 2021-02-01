def options():
    """
    Initial set of options presented to the user.

    :param: None
    :return: None
    """
    print("""
        \t[v] View budget
        \t[a] Add cost
        \t[q] Quit
        \t[u]
        \t[e]
        \t[r]
        \t[o]
        \t[s] Summary""")


def select():
    """
    select is invoked when the user selection is required. Usually after the
    presentation of options.

    :param: None
    :return: Choice
    """
    choice = input()


def add_cost():
    item = input("""
        What  
    """)
