# app/model.py (Corrected)
from app import db
from datetime import datetime

class Record(db.Model):
    __tablename__ = 'records' 

    id = db.Column(db.Integer, primary_key=True)
    
    # FIX: Change 'data' to 'title' and add 'content'
    title = db.Column(db.String(140), nullable=False)
    content = db.Column(db.Text)
    
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        # Update representation to use title
        return f'<Record {self.id}: {self.title}>'