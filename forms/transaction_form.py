from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, SubmitField
from wtforms.validators import InputRequired


class TransactionForm(FlaskForm):
    name = StringField(
        'Name',
        [
            InputRequired()
        ]
    )
    amount_usd = DecimalField(
        'Amount ($)',
        [
            InputRequired()
        ]
    )
    card = SelectField(
        'Choose a card',
        [
            InputRequired()
        ]
    )
    category = SelectField(
        'Choose a category',
        [
            InputRequired()
        ]
    )
    submit = SubmitField('Submit')
