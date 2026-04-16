from pathlib import Path
import sqlite3
db_path = Path(__file__).resolve().parents[1] / "database" / "solventsdb.sqlite"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

green_results_300K = [
(
    1,    #result_id
    1,    #solvent_id
    300,  #temperature_K
    5.0730e-9, #msd_slope
    0.8455e-9, #diffusion_coefficient
    "m²/s",
    "300 K self-diffusion result from molecular COM MSD for m-Xylene baseline simulation."
),
(
    2,    #result_id
    2,    #solvent_id
    300,  #temperature_K
    3.090e-9, #msd_slope
    0.5150e-9, #diffusion_coefficient
    "m²/s",
    "300 K self-diffusion result from molecular COM MSD for symmetrically substituted aromatic hydrocarbon comparison solvent."
),
(
    3,    #result_id
    3,    #solvent_id
    300,  #temperature_K
    1.428e-9, #msd_slope
    0.238e-9, #diffusion_coefficient
    "m²/s",
    "300 K self-diffusion result from molecular COM MSD for polar aromatic ketone comparison solvent."
),
(
    4,    #result_id
    4,    #solvent_id
    300,  #temperature_K
    4.470e-9, #msd_slope
    0.745e-9, #diffusion_coefficient
    "m²/s",
    "300 K self-diffusion result from molecular COM MSD for bio-based cyclic ether comparison solvent."
),
(
    5,    #result_id
    5,    #solvent_id
    300,  #temperature_K
    1.551e-9, #msd_slope
    0.258e-9, #diffusion_coefficient
    "m²/s",
    "300 K self-diffusion result from molecular COM MSD for polar aprotic cyclic lactam solvent with extended 5,000,000-step production sampling."
),
(
    6,    #result_id
    6,    #solvent_id
    300,  #temperature_K
    4.168e-9, #msd_slope
    0.694e-9, #diffusion_coefficient
    "m²/s",
    "300 K self-diffusion result from molecular COM MSD for hydrophobic cyclic ether comparison solvent."
    )
]
cur.executemany("""
INSERT INTO green_diffusion_results_300K(
    result_id,
    solvent_id,
    temperature_K,
    msd_slope,
    diffusion_coefficient,
    diffusion_unit,
    notes
)
VALUES(?,?,?,?,?,?,?)""",green_results_300K)
conn.commit()
conn.close()
print("Diffusion results at 300K has loaded successfully!")
