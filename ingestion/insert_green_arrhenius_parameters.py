import sqlite3
from pathlib import Path

db_path = Path(__file__).resolve().parents[1]/"database" / "solventsdb.sqlite"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

green_arrhenius_parameters = [
(
    1,        #fit_id
    1,        #solvent_id -> MXY
    -1265.708, #arrhenius_slope_K
    -16.820,    #  b -> ln_pre_exponential_factor
    0.0112,      #activation_energy_kcal_mol
    "MXY Arrhenius fit from lnD vs 1/T temperature series."
),
(
    2,
    2,
    -1287.389,
    -17.096,
    0.0114,
    "MS Arrhenius fit from lnD vs 1/T temperature series."
),
(
    3,
    3,
    -1725.023,
    -16.455,
    0.0172,
    "AP Arrhenius fit from lnD vs 1/T temperature series."
),
(
    4,
    4,
    -1082.102,
    -17.553,
    0.0102,
    "2-MeTHF Arrhenius fit from lnD vs 1/T temperature series."
),
(
    5,
    5,
    -1414.756,
    -17.273,
    0.0134,
    "NMP Arrhenius fit from lnD vs 1/T temperature series."
),
(
    6,
    6,
    -1219.666,
    -17.255,
    0.0124,
    "CPME Arrhenius fit from lnD vs 1/T temperature series."
    )
]
cur.executemany("""
INSERT INTO green_arrhenius_parameters(
    fit_id,
    solvent_id,
    arrhenius_slope_K,
    ln_pre_exponential_factor,
    activation_energy_kcal_mol,
    notes
)
VALUES(?,?,?,?,?,?)""", green_arrhenius_parameters)

conn.commit()
conn.close()
print("Your data has loaded successfully!")
