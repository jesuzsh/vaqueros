from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    SubmitField
)
from wtforms.validators import InputRequired


class CategoryForm(FlaskForm):
    name = StringField(
        'Name of category',
        [
            InputRequired
        ]
    )
    is_essential = SelectField(
        'Is this category essential?',
        [
            InputRequired
        ]
    )
    submit = SubmitField('Submit')
