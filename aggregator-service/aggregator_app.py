import pandas as pd
import mysql.connector
import psycopg2
from dotenv import load_dotenv
import os

# --- MySQL Config for fetching data ---
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PWD = os.getenv("MYSQL_PWD")
MYSQL_DB = os.getenv("MYSQL_DB")
PORT = os.getenv("PORT")

MYSQL_CONFIG = {
    "host": MYSQL_HOST,
    "user": MYSQL_USER,
    "password": MYSQL_PWD,
    "database": MYSQL_DB,
    "port": PORT
}

# --- Redshift Config ---
REDSHIFT_HOST=os.getenv("REDSHIFT_HOST")
REDSHIFT_PORT=os.getenv("REDSHIFT_PORT")
REDSHIFT_DBNAME=os.getenv("REDSHIFT_DBNAME")
REDSHIFT_USERNAME=os.getenv("REDSHIFT_USERNAME")
REDSHIFT_PWD=os.getenv("REDSHIFT_PWD")

REDSHIFT_CONFIG = {
    "host": REDSHIFT_HOST,
    "port": REDSHIFT_PORT,
    "dbname": REDSHIFT_DBNAME,
    "user": REDSHIFT_USERNAME,
    "password": REDSHIFT_PWD
}

# ------------------ FETCHING AGGREGATIONS ------------------
def fetch_dataframe(query):
    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except mysql.connector.Error as err:
        print(f"[MySQL ERROR] {err}")
        return pd.DataFrame()

def get_team_sales():
    return fetch_dataframe("""
        SELECT a.team, SUM(s.amount) AS total_sales
        FROM agents a
        JOIN sales s ON a.agent_code = s.agent_code
        GROUP BY a.team
        ORDER BY total_sales DESC
    """)

def get_product_target_achievement():
    return fetch_dataframe("""
        SELECT p.product_name, p.target_amount, 
               COALESCE(SUM(s.amount), 0) AS total_sales,
               CASE 
                   WHEN COALESCE(SUM(s.amount), 0) >= p.target_amount 
                   THEN 'Achieved' ELSE 'Not Achieved' 
               END AS status
        FROM products p
        LEFT JOIN sales s ON p.product_id = s.product_id
        GROUP BY p.product_id
        ORDER BY total_sales DESC
    """)

def get_branch_sales():
    return fetch_dataframe("""
        SELECT branch, SUM(amount) AS total_sales
        FROM sales
        GROUP BY branch
        ORDER BY total_sales DESC
    """)

# ------------------ INSERT TO REDSHIFT (UPSERT) ------------------

def connect_redshift():
    return psycopg2.connect(**REDSHIFT_CONFIG)

def upsert_team_sales(df):
    conn = connect_redshift()
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            DELETE FROM team_sales_metrics WHERE team = %s;
        """, (row['team'],))
        cursor.execute("""
            INSERT INTO team_sales_metrics (team, total_sales)
            VALUES (%s, %s);
        """, (row['team'], row['total_sales']))
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Upserted team_sales_metrics")

def upsert_product_target_metrics(df):
    conn = connect_redshift()
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            DELETE FROM product_target_metrics WHERE product_name = %s;
        """, (row['product_name'],))
        cursor.execute("""
            INSERT INTO product_target_metrics (product_name, target_amount, total_sales, status)
            VALUES (%s, %s, %s, %s);
        """, (row['product_name'], row['target_amount'], row['total_sales'], row['status']))
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Upserted product_target_metrics")

def upsert_branch_sales(df):
    conn = connect_redshift()
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            DELETE FROM branch_sales_metrics WHERE branch = %s;
        """, (row['branch'],))
        cursor.execute("""
            INSERT INTO branch_sales_metrics (branch, total_sales)
            VALUES (%s, %s);
        """, (row['branch'], row['total_sales']))
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Upserted branch_sales_metrics")

# ------------------ MAIN ------------------
if __name__ == "__main__":
    df1 = get_team_sales()
    upsert_team_sales(df1)

    df2 = get_product_target_achievement()
    upsert_product_target_metrics(df2)

    df3 = get_branch_sales()
    upsert_branch_sales(df3)

    # print('df1')
    # print(df1.info())y

    # print('df2')
    # print(df2.info())

    # print('df1')
    # print(df2.info())

    
