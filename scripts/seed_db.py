import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sqlite3
import pandas as pd
from app.utils.config import SQLITE_DB_PATH

def create_tables(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS universities (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            university_name     TEXT NOT NULL,
            country             TEXT,
            city_state          TEXT,
            program             TEXT,
            qs_ranking_2026     INTEGER,
            tuition_usd_per_year        INTEGER,
            living_cost_usd_per_year    INTEGER,
            fall_2026_deadline  TEXT,
            spring_2026_deadline TEXT,
            min_gpa_4           REAL,
            gre_required        TEXT,
            min_gre_score       INTEGER,
            min_ielts           REAL,
            min_toefl           INTEGER,
            acceptance_rate     REAL,
            employability_score INTEGER,
            notes               TEXT
        )
    """)
    print("✅ Tables created")

def seed_unis(conn):

    csv_path = "./data/structured/universities.csv"

    if not os.path.exists(csv_path):
        print("CSV not found!")
        return
    
    df = pd.read_csv(csv_path)
    df.to_sql("universities", conn, if_exists="replace", index=False)
    print(f"Seeded {len(df)} universities into DB")

def verify(conn):
    cursor = conn.execute("SELECT COUNT(*) FROM universities")
    count = cursor.fetchone()[0]
    print(f"✅ Verification — total rows in DB: {count}")

    # Print first 3 rows as a sanity check
    cursor = conn.execute("SELECT university_name, country, qs_ranking_2026 FROM universities LIMIT 3")
    rows = cursor.fetchall()
    for row in rows:
        print(f"   {row[0]} | {row[1]} | Rank #{row[2]}")

def seed():
    os.makedirs(os.path.dirname(SQLITE_DB_PATH), exist_ok=True)

    conn = sqlite3.connect(SQLITE_DB_PATH)
    print(f"📂 Connected to DB at {SQLITE_DB_PATH}")

    create_tables(conn)
    seed_unis(conn)

    verify(conn)

    conn.commit()
    conn.close()
    print("✅ Done!")


if __name__ == "__main__":
    seed()
