import sqlite3

def save_to_db(df, db_path="../data/nbp.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql("rates", conn, if_exists="replace", index=False)
    conn.close()