from flask import Flask, request
import psycopg2
import random
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Database connection pool (reusable connections)
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST', 'postgres'),
        port=int(os.getenv('POSTGRES_PORT', 5432)),
        dbname=os.getenv('POSTGRES_DB', 'quotesdb'),
        user=os.getenv('POSTGRES_USER', 'admin'),
        password=os.getenv('POSTGRES_PASSWORD', 'secret')
    )
    return conn


@app.route('/')
def index():
    """Home page"""
    return '<h1>Quote Generator API</h1><p>Visit /quote or /quote/<id></p>'


@app.route('/quote', methods=['GET'])
def get_random_quote():
    """Return a pseudo-random quote from the database"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Select all quotes and pick randomly in Python
        cursor.execute('SELECT id, text FROM quotes')
        rows = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        if not rows:
            return {'error': 'No quotes found in database'}, 404
        
        # Random selection
        quotedata = random.choice(rows)
        
        return {
            'id': quotedata[0],
            'text': quotedata[1]
        }, 200
        
    except Exception as e:
        return {'error': str(e)}, 500


@app.route('/quote/<int:id>', methods=['GET'])
def get_quote_by_id(id):
    """Return specific quote by ID"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, text FROM quotes WHERE id = %s', (id,))
        row = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if not row:
            return {'error': 'Quote not found'}, 404
        
        return {
            'id': row[0],
            'text': row[1]
        }, 200
        
    except Exception as e:
        return {'error': str(e)}, 500


@app.route('/quotes/list', methods=['GET'])
def list_all_quotes():
    """List all quotes in the database"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, text FROM quotes ORDER BY id ASC')
        rows = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return {
            'count': len(rows),
            'quotes': [{'id': r[0], 'text': r[1]} for r in rows]
        }, 200
        
    except Exception as e:
        return {'error': str(e)}, 500
    
@app.route('/quote/<int:id>', methods=['PATCH'])
def update_quote(id):
    """Update specific quote by ID"""
    try:
        payload = request.get_json(silent=True)
        if not payload or 'text' not in payload:
            return {'error': 'Missing text field in request body'}, 400

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('UPDATE quotes SET text = %s WHERE id = %s', (payload['text'], id))
        conn.commit()

        if cursor.rowcount == 0:
            cursor.close()
            conn.close()
            return {'error': f'Quote ID {id} not found'}, 404

        cursor.close()
        conn.close()

        return {'message': 'Quote updated successfully'}, 200

    except Exception as e:
        return {'error': str(e)}, 500
    


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for monitoring"""
    try:
        conn = get_db_connection()
        conn.close()
        return {'status': 'healthy', 'database': 'connected'}
    except Exception as e:
        return {'status': 'unhealthy', 'database': str(e)}, 503


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=True)