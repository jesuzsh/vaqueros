from flask import (
    Flask,
    render_template,
    url_for,
    redirect

)
from forms.transaction_form import TransactionForm
from dba.database import Database
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)


@app.route('/transaction', methods=['GET', 'POST'])
def transaction():
    """

    """
    db = Database()
    form = TransactionForm()

    form.card.choices = db.get_cards()
    form.category.choices = db.get_categories()

    if form.validate_on_submit():
        db.write_transaction(
            form.name.data,
            form.amount_usd.data,
            form.card.data,
            form.category.data
        )

        return redirect(url_for("success"))

    return render_template(
        'transactionForm.html',
        form=form
    )


@app.route('/success', methods=['GET'])
def success():
    db = Database()

    num_t = db.count_transactions()

    print("Transaction count:", num_t)
    print(db.get_transactions())

    return render_template(
        'success.html',
        num_transactions=num_t
    )
