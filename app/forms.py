# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class RecordForm(FlaskForm):
    """Form for creating/editing records"""
    title = StringField(
        'Title',
        validators=[
            DataRequired(message='Title is required'),
            Length(min=1, max=140, message='Title must be 1-140 characters')
        ]
    )
    content = TextAreaField(
        'Content',
        validators=[
            Length(max=2000, message='Content cannot exceed 2000 characters')
        ]
    )
    submit = SubmitField('Save Record')