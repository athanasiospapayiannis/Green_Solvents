import sqlite3
from pathlib import Path

db_path = Path(__file__).resolve().parents[1] / "solventsdb.sqlite"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("""
DROP TABLE IF EXISTS green_arrhenius_parameters
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS green_arrhenius_parameters(
    fit_id     INTEGER PRIMARY KEY,
    solvent_id INTEGER NOT NULL,
    arrhenius_slope_K REAL NOT NULL,
    ln_pre_exponential_factor REAL NOT NULL,
    activation_energy_kcal_mol REAL NOT NULL,
    notes                  TEXT,
    FOREIGN KEY(solvent_id) REFERENCES solvents(solvent_id)
)
""")
conn.commit()
conn.close()
print("Green Arrhenius Parameters table has created successfully!")
