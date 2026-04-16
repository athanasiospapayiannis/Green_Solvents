import sqlite3
conn = sqlite3.connect('solventsdb.sqlite')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS validation_results(
    id INTEGER PRIMARY KEY,
    solvent_name TEXT,
    temperature_K REAL,
    pressure_atm  REAL,
    predicted_diffusion REAL,
    literature_diffusion REAL,
    absolute_error       REAL,
    relative_error_percent REAL,
    source_reference     TEXT,
    notes               TEXT
)
""")
conn.commit()
conn.close()
print("validation_results table ready!")
