import sqlite3
conn = sqlite3.connect("../solventsdb.sqlite")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS green_simulation_metadata (
    production_simulation_id INTEGER PRIMARY KEY,
    solvent_id INTEGER NOT NULL,
    initial_temperature_K REAL NOT NULL,
    temperature_K REAL NOT NULL,
    software TEXT NOT NULL,
    force_field TEXT NOT NULL,
    ensemble TEXT NOT NULL,
    timestep_fs REAL NOT NULL,
    equilibration_steps INTEGER NOT NULL,
    production_steps INTEGER NOT NULL,
    barostat_status TEXT NOT NULL,
    box_length_A     REAL,
    observable_type TEXT NOT NULL,
    diffusion_definition TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY(solvent_id) REFERENCES solvents(solvent_id)
)
""")

conn.commit()
conn.close()

print("green_simulation_metadata table created successfully!")
