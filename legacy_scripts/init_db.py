import sqlite3
conn = sqlite3.connect('solventsdb.sqlite')
cur = conn.cursor()

#SOLVENTS TABLE
cur.executescript('''
CREATE TABLE IF NOT EXISTS solvents (
    id  INTEGER PRIMARY KEY,
    code TEXT UNIQUE,
    name TEXT,
    formula TEXT,
    molar_mass REAL,
    density_25C REAL,
    viscosity_25C REAL,
    aromatic_ring_count INTEGER,
    halogen_free INTEGER,
    notes TEXT
)
''')

#SIMULATION TABLE
cur.executescript('''
CREATE TABLE IF NOT EXISTS simulations(
    id INTEGER PRIMARY KEY,
    solvent_id INTEGER,
    temperature_K REAL,
    pressure_atm REAL,
    ensemble TEXT,
    force_field TEXT,
    timestep_fs REAL,
    total_steps INTEGER,
    box_x       REAL,
    box_y       REAL,
    box_z       REAL,
    FOREIGN KEY(solvent_id) REFERENCES solvents(id)
)
''')

#DIFFUSION RESULTS TABLE
cur.executescript('''
CREATE TABLE IF NOT EXISTS diffusion_results (
    id  INTEGER PRIMARY KEY,
    simulation_id INTEGER,
    msd_slope   REAL,
    diffusion_coefficient  REAL,
    activation_energy      REAL,
    pre_exponential_factor REAL,
    FOREIGN KEY (simulation_id) REFERENCES simulations(id)
)
''')
conn.commit()
conn.close()
print("Database initialized successfully.")
