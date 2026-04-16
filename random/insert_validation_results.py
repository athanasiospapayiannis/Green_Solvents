import sqlite3
conn = sqlite3.connect('solventsdb.sqlite')
cur = conn.cursor()

validation_results = [
(
    1,
    "Ethanol",
    300,
    None,
    3.160e-9,   #msd_slope A
    0.526e-9,   #Dcalc
    0.413e-9,   #Dref
    abs(0.526e-9 - 0.413e-9),
    abs((0.526e-9 - 0.413e-9) / 0.413e-9) * 100,
    "Thesis Table I",
    "Validation benchmark solvent",
    "m²/s"
),
(
    2,
    "Acetone",
    300,
    None,
    8.934e-9,   #msd_slope A
    1.489e-9,   #Dcalc
    1.321e-9,   #Dref
    abs(1.489e-9 - 1.321e-9),
    abs((1.489e-9 - 1.321e-9) / 1.321e-9) * 100,
    "Thesis Table I",
    "Validation benchmark solvent",
    "m²/s"
),
(
    3,
    "Acetic Acid",
    300,
    None,
    1.290e-9,   #msd_slope A
    0.215e-9,   #Dcalc
    0.283e-9,   #Dref
    abs(0.215e-9 - 0.283e-9),
    abs((0.215e-9 - 0.283e-9) / 0.283e-9) * 100,
    "Thesis Table I",
    "Validation benchmark solvent",
    "m²/s"
),
(
    4,
    "N-Methylaniline",
    300,
    None,
    1.270e-9,   #msd_slope A
    0.211e-9,   #Dcalc
    0.143e-9,   #Dref
    abs(0.211e-9 - 0.143e-9),
    abs((0.211e-9 - 0.143e-9) / 0.143e-9) * 100,
    "Thesis Table I",
    "Validation benchmark solvent",
    "m²/s"
),
(
    5,
    "Pyridine",
    300,
    None,
    3.640e-9,   #msd_slope A
    0.606e-9,   #Dcalc
    0.548e-9,   #Dref
    abs(0.606e-9 - 0.548e-9),
    abs((0.606e-9 - 0.548e-9) / 0.548e-9) * 100,
    "Thesis Table I",
    "Validation benchmark solvent",
    "m²/s"
    )
]

cur.executemany("""
INSERT INTO validation_results (
    id,
    solvent_name,
    temperature_K,
    pressure_atm,
    msd_slope,
    predicted_diffusion,
    literature_diffusion,
    absolute_error,
    relative_error_percent,
    source_reference,
    notes,
    diffusion_unit
)
VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
""", validation_results)
conn.commit()
conn.close()
print(f"{len(validation_results)} validation rows inserted successfully!")
