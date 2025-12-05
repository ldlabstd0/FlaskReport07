# app/route.py (UPDATED with dedicated Home route)

from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db # Import the SQLAlchemy object
from app.model import Record # Import the SQLAlchemy model
from app.forms import RecordForm # Import the forms we just defined

# Create the Blueprint instance
main_bp = Blueprint('main', __name__)

# --- Home Route ---
@main_bp.route('/')
def index():
    """Renders the Home page, using the endpoint 'main.index'."""
    # You will need a templates/index.html file for this to work!
    return render_template('index.html')

# --- View Routes ---

@main_bp.route('/records')
def list_records():
    """List all records using SQLAlchemy ORM (now only on /records)."""
    
    # ORM Query: SELECT * FROM records ORDER BY timestamp DESC
    records = Record.query.order_by(Record.timestamp.desc()).all()
    
    return render_template('records_list.html', records=records)

@main_bp.route('/about')
def about():
    """Renders the About page, using the endpoint 'main.about'."""
    return render_template('about.html')

@main_bp.route('/records/<int:id>')
def view_record(id): 
    """View single record using ORM."""
    
    record = Record.query.get_or_404(id)
    
    return render_template('record_detail.html', record=record)

# --- Create Route ---

@main_bp.route('/records/new', methods=['GET', 'POST'])
def create_record():
    """Create new record using ORM."""
    form = RecordForm()
    
    if form.validate_on_submit():
        record = Record(
            title=form.title.data,
            content=form.content.data
        )
        
        db.session.add(record)
        db.session.commit()
        
        flash('Record created successfully!', 'success')
        return redirect(url_for('main.list_records'))
    
    return render_template('form.html', form=form, action='Create')

# --- Update Route ---

@main_bp.route('/records/<int:id>/edit', methods=['GET', 'POST'])
def edit_record(id):
    """Edit existing record using ORM."""
    
    record = Record.query.get_or_404(id)
    form = RecordForm()
    
    if form.validate_on_submit():
        record.title = form.title.data
        record.content = form.content.data
        
        db.session.commit()
        
        flash('Record updated successfully!', 'success')
        return redirect(url_for('main.view_record', id=id))
    
    if not form.is_submitted():
        form.title.data = record.title
        form.content.data = record.content

    return render_template('form.html', form=form, action='Edit')

# --- Delete Route ---

@main_bp.route('/records/<int:id>/delete', methods=['POST'])
def delete_record(id):
    """Delete record using ORM (POST only for security)."""
    
    record = Record.query.get_or_404(id)
    
    db.session.delete(record)
    db.session.commit()

    flash('Record deleted successfully', 'success')
    return redirect(url_for('main.list_records'))