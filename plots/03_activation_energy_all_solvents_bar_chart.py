from pathlib import Path
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
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
activation_energy_kcal_mol
FROM green_arrhenius_parameters g 
JOIN solvents s
ON g.solvent_id = s.id
ORDER BY g.activation_energy_kcal_mol DESC;
"""

df = pd.read_sql_query(query, conn)
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

group_colors = {
    "Aromatic ketone": "tab:red",
    "Lactam carbonyl": "tab:orange",
    "Cyclic ethers": "tab:blue",
    "Aromatic hydrocarbons": "tab:green"
}

df["chemical_group"] = df["name"].map(chemical_groups)
bar_colors = df["chemical_group"].map(group_colors)

# =========================
# HORIZONTAL BAR CHART
# =========================
plt.figure(figsize=(10, 6))

plt.barh(
    df["name"],
    df["activation_energy_kcal_mol"],
    color=bar_colors
)

plt.xlabel("Activation Energy (kcal/mol)")
plt.ylabel("Solvent")
plt.title("Diffusion Activation Energy by Chemical Family")
plt.grid(axis="x")
plt.gca().invert_yaxis()

# =========================
# LEGEND
# =========================
legend_elements = [
    Patch(facecolor=color, label=group)
    for group, color in group_colors.items()
]

plt.legend(handles=legend_elements, title="Chemical Family")
plt.tight_layout()

# =========================
# SAVE FIGURE
# =========================
plot_file = plot_path / "03_activation_energy_by_chemical_family.png"
plt.savefig(plot_file, dpi=300)

plt.show()
conn.close()