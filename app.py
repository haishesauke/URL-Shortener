# Import required libraries
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from hashids import Hashids
import secrets

# Initialize Flask application
app = Flask(__name__)

# Configure application
# Set secret key for session security
app.config['SECRET_KEY'] = secrets.token_hex(16)
# Configure SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
# Disable SQLAlchemy modification tracking (improves performance)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database with Flask app
db = SQLAlchemy(app)
# Initialize Hashids for URL encoding (minimum length of 6 characters)
hashids = Hashids(min_length=6)

# Define URL database model
class URL(db.Model):
    """
    Database model for storing URLs
    Attributes:
        id: Primary key for the URL entry
        original_url: The original URL to be shortened
    """
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), nullable=False)
    
# Route for home page
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handle both GET and POST requests for the main page
    GET: Display the URL submission form
    POST: Process the submitted URL and create a shortened version
    """
    if request.method == 'POST':
        # Get the URL from the form submission
        original_url = request.form['url']
        # Create new URL database entry
        new_url = URL(original_url=original_url)
        db.session.add(new_url)
        db.session.commit()

        # Generate shortened URL
        short_id = hashids.encode(new_url.id)
        short_url = request.host_url + short_id
        return render_template('index.html', short_url=short_url)
    return render_template('index.html')

# Route for URL redirection
@app.route('/<short_id>')
def redirect_to_url(short_id):
    """
    Handle redirection from shortened URL to original URL
    Args:
        short_id: The encoded ID from the shortened URL
    Returns:
        Redirect to original URL or 404 error if URL not found
    """
    # Decode the short ID
    decoded = hashids.decode(short_id)
    if decoded:
        url_id = decoded[0]
        # Look up the original URL in the database
        url_entry = URL.query.get(url_id)
        if url_entry:
            return redirect(url_entry.original_url)
    return 'URL not found', 404

# Application entry point
if __name__ == '__main__':
    # Create database tables when running directly
    with app.app_context():
        db.create_all()
    # Run the application in debug mode
    app.run(debug=True)
else:
    # Create database tables when running with flask command
    with app.app_context():
        db.create_all()
    


        

