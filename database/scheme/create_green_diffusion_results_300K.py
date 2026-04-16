from pathlib import Path
import sqlite3
db_path = Path(__file__).resolve().parents[1] / 'solventsdb.sqlite'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS green_diffusion_results_300K(
    result_id      INTEGER PRIMARY KEY,
    solvent_id     INTEGER NOT NULL,
    temperature_K  REAL NOT NULL,
    msd_slope      REAL NOT NULL,
    diffusion_coefficient    REAL NOT NULL,
    diffusion_unit           TEXT NOT NULL,
    notes                     TEXT,
    FOREIGN KEY(solvent_id) REFERENCES solvents (solvent_id)
)
""")

conn.commit()
conn.close()

print("green_diffusion_results_300K table has created successfully!")
