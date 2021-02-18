"""
The data layer of the application. This is where all transaction with the
database are going to live. The application layer is to export functions from
this file.
"""
from dba.model import transaction, card, category
from dba.environment import build_engine
from sqlalchemy import func, insert, select


class Database:
    def __init__(self):
        self.engine = build_engine()

    def write(self, stmt):
        """
        Current way of writing to a database: SQLAlchemy Core
        """
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()

    def all(self, stmt):
        """
        Method for getting all results of a query.

        :param stmt: SQL statement

        :return: List of Tuples, results from the SQL statement
        """
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            return result.all()

    def scalar(self, stmt):
        """
        Method for getting scalar result from a statement.

        :param stmt: SQL statement

        :return: Single value
        """
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            return result.scalar()

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
        stmt = select(transaction)

        return self.all(stmt)

    def count_transactions(self):
        """
        Queries for the total number of transaction in the database 

        :return: Integer
        """
        stmt = select(func.count()).select_from(transaction)

        return self.scalar(stmt)

    def write_transaction(self, name, amount_usd, card, category):
        """

        :param name:
        :param amount_usd:
        :param card:
        :param category:
        """
        try:
            stmt = insert(transaction).values(
                transaction_name=name,
                amount_usd=amount_usd,
                card_id=int(card),
                category_id=int(category)
            )

            self.write(stmt)
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

    def write_category(self, name, is_essential):
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
