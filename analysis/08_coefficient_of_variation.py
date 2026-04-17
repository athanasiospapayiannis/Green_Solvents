from pathlib import Path
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

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

# mapping families
chemical_groups = {
    "Acetophenone": "Aromatic ketone",
    "N-Methyl-2-Pyrrolidone": "Lactam carbonyl",
    "2-Methyltetrahydrofuran": "Cyclic ethers",
    "Cyclopentyl-Methyl-Ether": "Cyclic ethers",
    "m-Xylene": "Aromatic hydrocarbons",
    "Mesitylene": "Aromatic hydrocarbons"
}

df["family"] = df["name"].map(chemical_groups)

# compute CV
summary = (
    df.groupby("family")
      .agg(
          mean_diffusion=("diffusion_coefficient", "mean"),
          std_diffusion=("diffusion_coefficient", "std")
      )
)

summary["cv_diffusion"] = summary["std_diffusion"] / summary["mean_diffusion"]

print(summary.sort_values("cv_diffusion", ascending=False))



summary_sorted = summary.sort_values("cv_diffusion", ascending=True)

plt.figure(figsize=(8,5))
plt.barh(summary_sorted.index, summary_sorted["cv_diffusion"])

plt.xlabel("Coefficient of Variation (Diffusion)")
plt.title("Family Transport Heterogeneity (CV)")
plt.tight_layout()
plt.show()


conn.close()