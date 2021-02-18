from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField
)
from wtforms.validators import InputRequired


class CardForm(FlaskForm):
    name = StringField(
        'Name of card',
        [
            InputRequired
        ]
    )
    owner = StringField(
        'Owner, name on card',
        [
            InputRequired
        ]
    )

    submit = SubmitField('Submit')
