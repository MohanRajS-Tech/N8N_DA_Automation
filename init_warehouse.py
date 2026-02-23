import pandas as pd
import sqlite3
import os

# ELI5: This script is our "Migration Agent". 
# It takes the heavy Excel file and puts it into a fast, tidy SQLite filing cabinet.

def init_warehouse(excel_path, db_path):
    print(f"🚀 Initializing Warehouse: Connecting to {db_path}...")
    
    # 1. Connect to SQLite (This creates the file if it doesn't exist)
    conn = sqlite3.connect(db_path)
    
    # 2. Read the Excel File
    print(f"📂 Reading {excel_path}... (This is the last time you'll have to wait for Excel!)")
    df = pd.read_excel(excel_path)
    
    # 3. Clean names (SQL doesn't like spaces in column names)
    print("🪄 Tidying up column names for SQL...")
    df.columns = [c.replace(' ', '_') for c in df.columns]
    
    # 4. Burn the Data into the Warehouse
    print("🔥 Loading 541,000 rows into SQLite... Hang tight!")
    df.to_sql('transactions', conn, if_exists='replace', index=False)
    
    # 5. Create an "Index" (ELI5: This is like the 'A-Z' tabs in a cabinet that make searching instant)
    print("⚡ Creating indexes for high-speed searching...")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_customer ON transactions(CustomerID)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_invoice ON transactions(InvoiceNo)")
    
    # 6. Verification (The "Showroom" check)
    count = pd.read_sql("SELECT COUNT(*) FROM transactions", conn).iloc[0,0]
    print(f"\n✅ SUCCESS! Warehouse is ready.")
    print(f"📊 Total Records Stored: {count}")
    
    conn.close()

if __name__ == "__main__":
    EXCEL_FILE = "Online Retail.xlsx"
    DB_FILE = "retail_warehouse.db"
    
    if os.path.exists(EXCEL_FILE):
        init_warehouse(EXCEL_FILE, DB_FILE)
    else:
        print(f"❌ Error: {EXCEL_FILE} not found!")
