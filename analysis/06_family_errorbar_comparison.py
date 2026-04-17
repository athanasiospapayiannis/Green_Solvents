from pathlib import Path
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#paths
project_root = Path(__file__).resolve().parents[1]
db_path = project_root / "database" / "solventsdb.sqlite"
sql_path = project_root / "sql_queries"
analysis_path = project_root / "analysis"
plot_path = project_root / "plots"

conn = sqlite3.connect(db_path)
cur = conn.cursor()

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

chemical_groups = {
    "Acetophenone": "Aromatic ketone",
    "N-Methyl-2-Pyrrolidone": "Lactam carbonyl",
    "2-Methyltetrahydrofuran": "Cyclic ethers",
    "Cyclopentyl-Methyl-Ether": "Cyclic ethers",
    "m-Xylene": "Aromatic hydrocarbons",
    "Mesitylene": "Aromatic hydrocarbons"
}

df["chemical_family"] = df["name"].map(chemical_groups)

summary = (
    df.groupby("chemical_family")
      .agg(
          mean_activation_energy=("activation_energy_kcal_mol", "mean"),
          std_activation_energy=("activation_energy_kcal_mol", "std"),
          mean_diffusion=("diffusion_coefficient", "mean"),
          std_diffusion=("diffusion_coefficient", "std")
      )
      .fillna(0)
)

# =========================
# MULTI PANEL ERRORBAR
# =========================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

families = summary.index

# LEFT PANEL
axes[0].bar(
    families,
    summary["mean_activation_energy"],
    yerr=summary["std_activation_energy"],
    capsize=5
)
axes[0].set_title("Mean Activation Energy")
axes[0].set_ylabel("kcal/mol")
axes[0].tick_params(axis="x", rotation=45)

# RIGHT PANEL
axes[1].bar(
    families,
    summary["mean_diffusion"],
    yerr=summary["std_diffusion"],
    capsize=5
)
axes[1].set_title("Mean 300 K Diffusion")
axes[1].set_ylabel("m²/s")
axes[1].tick_params(axis="x", rotation=45)

plt.tight_layout()

plot_file = plot_path / "11_family_errorbar_comparison.png"
plt.savefig(plot_file, dpi=300)

plt.show()
conn.close()