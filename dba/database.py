"""
The data layer of the application. This is where all transaction with the
database are going to live. The application layer is to export functions from
this file.
"""
from dba.model import Transaction
from dba.environment import create_session
from sqlalchemy import func


class Database:
    def __init__(self):
        self.session = create_session()

    def get_cards(self):
        """
        ATM, this is hard-coded. Soon-to-be querying our database to find the
        existing cards. To present the names of existing cards.

        :return: List of Tuples, form.choices syntax
        """
        known_cards = [(1, "Amex"), (2, "Amex Gold")]
        return known_cards

    def get_categories(self):
        """
        Atm, this is hard-coded. Soon to be querying our database to find the
        existing categories.

        :return: List of Tuples, form.choices syntax
        """
        known_categories = [(1, "Groceries"), (2, "Takeout")]

        return known_categories

    def get_transactions(self):
        """
        Basically a SELECT * (all) from a single table. Definitely not the most
        efficient query.

        :return: List of Tuples
        """
        return self.session.query(Transaction).all()

    def count_transactions(self):
        """
        Queries for the total number of transaction in the database 

        :return: Integer
        """
        return self.session.query(func.count(Transaction.transaction_id)).scalar()

    def write(self, obj):
        print("Adding", obj)
        self.add(obj)
        self.commit()

    def write_transaction(self, name, amount_usd, card, category):
        """
    
        :param name:
        :param amount_usd:
        :param card:
        :param category:
        """
        try:
            new_t = Transaction(
                        name=name,
                        amount_usd=amount_usd,
                        card=card,
                        category=category
            )

            self.write(new_t)

            return None
        except Exception as e:
            print(e)

    def write_card(self, name, owner):
        """
        Write a new card to the database.

        :param name:
        :param owner:

        :return: None
        """
        try: 
            new_c = Card(
                        name=name,
                        owner=owner
            )
            
            self.write(new_c)
        except Exception as e:
            print(e)

    def write_category(name, is_essential):
        """
        Write a new category to the database.

        :param name:
        :param is_essential:

        :return: None
        """
        try:
            new_c = Category(
                        name=name,
                        is_essential=is_essential
            )

            self.write(new_c)
        except Exception as e:
            print(e)

    def add(self, obj):
        """
        Add the given instance to the session.

        :param obj: ORM instance
        """
        self.session.add(obj)


    def commit(self):
        """
        Commit transactions with the database.
        """
        self.session.commit()
