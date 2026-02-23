from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Path to our SQLite database
DB_PATH = r'C:\Users\mohan\OneDrive\Documents\Anti Gravity Projects\n8n DA POC\retail_warehouse.db'

@app.route('/query', methods=['GET', 'POST'])
def query_db():
    # Try to get SQL from: 1. JSON body, 2. Form data, 3. URL Query params
    sql = None
    
    if request.is_json:
        sql = request.json.get('sql')
    elif request.form:
        sql = request.form.get('sql')
    
    if not sql:
        sql = request.args.get('sql')

    if not sql:
        return jsonify({"error": "No SQL query provided. Use field 'sql'."}), 400
    
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute(sql)
        rows = cursor.fetchall()
        
        # Convert rows to list of dicts for n8n
        result = [dict(row) for row in rows]
        
        conn.close()
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print(f"🚀 Sentinel Data Bridge running on http://localhost:5000")
    print(f"📊 Connected to: {DB_PATH}")
    app.run(host='0.0.0.0', port=5000)
