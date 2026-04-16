import sqlite3
conn = sqlite3.connect('../database/solventsdb.sqlite')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS validated_simulation_metadata(
    validation_simulation_id       INTEGER PRIMARY KEY,
    solvent_name                   TEXT NOT NULL,
    initial_temperature_K          REAL NOT NULL,
    temperature_K                  REAL NOT NULL,
    software                       TEXT NOT NULL,
    force_field                    TEXT NOT NULL,
    ensemble                       TEXT NOT NULL,
    timestep_fs                    REAL NOT NULL,
    equilibration_steps            INTEGER NOT NULL,
    production_steps               INTEGER NOT NULL,
    barostat_status                TEXT NOT NULL,
    box_length_A                   REAL,
    observable_type                TEXT NOT NULL,
    diffusion_definition           TEXT NOT NULL,
    notes                          TEXT
)
""")

conn.commit()
conn.close()
print("Validated simulation metadata table created successfully!")
