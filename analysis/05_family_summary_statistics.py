from pathlib import Path
import sqlite3
import pandas as pd

# =========================
# PATHS
# =========================
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = PROJECT_ROOT / "database" / "solventsdb.sqlite"

# =========================
# DATABASE
# =========================
conn = sqlite3.connect(DB_PATH)

query = """
SELECT s.name,
       g.activation_energy_kcal_mol,
       d.diffusion_coefficient
FROM solvents s
JOIN green_arrhenius_parameters g
ON s.id = g.solvent_id
JOIN green_diffusion_results_300K d
ON s.id = d.solvent_id;
"""

df = pd.read_sql_query(query, conn)

# =========================
# CHEMICAL GROUPS
# =========================
chemical_groups = {
    "Acetophenone": "Aromatic ketone",
    "N-Methyl-2-Pyrrolidone": "Lactam carbonyl",
    "2-Methyltetrahydrofuran": "Cyclic ethers",
    "Cyclopentyl-Methyl-Ether": "Cyclic ethers",
    "m-Xylene": "Aromatic hydrocarbons",
    "Mesitylene": "Aromatic hydrocarbons"
}

df["chemical_family"] = df["name"].map(chemical_groups)

# =========================
# FAMILY SUMMARY
# =========================
summary = (
    df.groupby("chemical_family")
      .agg(
          mean_activation_energy=("activation_energy_kcal_mol", "mean"),
          std_activation_energy=("activation_energy_kcal_mol", "std"),
          mean_diffusion=("diffusion_coefficient", "mean"),
          std_diffusion=("diffusion_coefficient", "std")
      )
      .sort_values("mean_activation_energy")
)

print(summary)

conn.close()