import sqlite3
conn = sqlite3.connect('../database/solventsdb.sqlite')
cur = conn.cursor()

validation_simulation_metadata = [
(
    1,
    "Ethanol",
    600,
    300,
    "NAMD",
    "AMBER",
    "NPT",
    1,
    100000,
    100000,
    "OFF during diffusion",
    None,
    "Molecular COM MSD",
    "Einstein relation from COM displacement",
    "Benchmark validation solvent. Exact stabilized box length, molecule count, thermostat identity, and full input/output files remain archived in the university laboratory workstation and are recoverable during metadata reconciliation."
),
(
    2,
    "Acetone",
    600,
    300,
    "NAMD",
    "AMBER",
    "NPT",
    1,
    150000,
    4000000,
    "OFF during diffusion",
    None,
    "Molecular COM MSD",
    "Einstein relation from COM displacement",
    "High-mobility benchmark validation solvent with strong agreement to literature diffusion values. Exact stabilized box length, molecule count, thermostat identity, and full input/output files remain archived in the university laboratory workstation and are recoverable during metadata reconciliation."
),
(
    3,
    "Acetic Acid",
    600,
    300,
    "NAMD",
    "AMBER",
    "NPT",
    1,
    100000,
    100000,
    "OFF during diffusion",
    None,
    "Molecular COM MSD",
    "Einstein relation from COM displacement",
    "Polar benchmark validation solvent. Exact stabilized box length, molecule count, thermostat identity, and full input/output files remain archived in the university laboratory workstation and are recoverable during metadata reconciliation."
),
(
    4,
    "N-Methylaniline",
    600,
    300,
    "NAMD",
    "AMBER",
    "NPT",
    1,
    150000,
    150000,
    "OFF during diffusion",
    None,
    "Molecular COM MSD",
    "Einstein relation from COM displacement",
    "Aromatic amine benchmark validation solvent. MSD convergence was less stable and may benefit from extended production sampling. Exact stabilized box length, molecule count, thermostat identity, and full input/output files remain archived in the university laboratory workstation and are recoverable during metadata reconciliation."
),
(
    5,
    "Pyridine",
    600,
    300,
    "NAMD",
    "AMBER",
    "NPT",
    1,
    150000,
    150000,
    "OFF during diffusion",
    None,
    "Molecular COM MSD",
    "Einstein relation from COM displacement",
    "Heteroaromatic benchmark validation solvent. Exact stabilized box length, molecule count, thermostat identity, and full input/output files remain archived in the university laboratory workstation and are recoverable during metadata reconciliation."
    )
]
cur.executemany("""
INSERT INTO validated_simulation_metadata(
    validation_simulation_id,
    solvent_name,
    initial_temperature_K,
    temperature_K,
    software,
    force_field,
    ensemble,
    timestep_fs,
    equilibration_steps,
    production_steps,
    barostat_status,
    box_length_A,
    observable_type,
    diffusion_definition,
    notes
)
VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",validation_simulation_metadata)
conn.commit()
conn.close()
print(f"{len(validation_simulation_metadata)} validation rows inserted successfully!")
