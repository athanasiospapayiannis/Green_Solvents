from pathlib import Path
import sqlite3

db_path = Path(__file__).resolve().parents[1] / "database" / "solventsdb.sqlite"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

green_simulation_metadata = [
(
    1,        #production_simulation_id
    1,        #solvent_id from solvents table
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
    "Aromatic green solvent production simulation at 300 K. Low-viscosity aromatic hydrocarbon reference within the thesis solvent set. Exact stabilized box dimensions, molecule count, thermostat identity, and full input/output files remain archived in the university laboratory workstation and are recoverable during metadata reconciliation."
),
(
    2,
    2,
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
    "Aromatic green solvent production simulation at 300 K. Symmetrically substituted aromatic hydrocarbon reference used to evaluate the effect of increased alkyl substitution on translational mobility. Exact stabilized box dimensions, molecule count, thermostat identity, and full input/output files remain archived in the university laboratory workstation and are recoverable during metadata reconciliation."
),
(
    3,
    3,
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
    "Aromatic green solvent production simulation at 300 K. Polar aromatic ketone reference used to evaluate the effect of carbonyl-driven dipolar interactions on translational mobility relative to non-polar aromatic hydrocarbons. Exact stabilized box dimensions, molecule count, thermostat identity, and full input/output files remain archived in the university laboratory workstation and are recoverable during metadata reconciliation."
),
(
    4,
    4,
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
    "Bio-based non-aromatic green solvent production simulation at 300 K. Cyclic ether reference used to evaluate the effect of heterocyclic oxygen incorporation and reduced aromaticity on translational mobility. Exact stabilized box dimensions, molecule count, thermostat identity, and full input/output files remain archived in the university laboratory workstation and are recoverable during metadata reconciliation."
),
(
    5,
    5,
    600,
    300,
    "NAMD",
    "AMBER",
    "NPT",
    1,
    150000,
    5000000,
    "OFF during diffusion",
    None,
    "Molecular COM MSD",
    "Einstein relation from COM displacement",
    "Polar aprotic non-aromatic green solvent production simulation at 300 K. Cyclic lactam reference used to evaluate the effect of strong dipolar carbonyl interactions on translational mobility. Extended production run to 5,000,000 steps was applied for improved MSD stabilization and diffusion convergence. Exact stabilized box dimensions, molecule count, thermostat identity, and full input/output files remain archived in the university laboratory workstation and are recoverable during metadata reconciliation."
),
(
    6,
    6,
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
    "Hydrophobic non-aromatic green solvent production simulation at 300 K. Cyclic ether benchmark used to evaluate the effect of ether oxygen placement, ring topology, and molecular flexibility on translational mobility. Exact stabilized box dimensions, molecule count, thermostat identity, and full input/output files remain archived in the university laboratory workstation and are recoverable during metadata reconciliation."
    )
]
cur.executemany("""
INSERT INTO green_simulation_metadata(
    production_simulation_id,
    solvent_id,
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
VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",green_simulation_metadata)
conn.commit()
conn.close()
print(f"{len(green_simulation_metadata)} green simulation rows inserted successfully!")
