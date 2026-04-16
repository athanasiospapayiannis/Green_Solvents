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
d.diffusion_coefficient
FROM green_diffusion_results_300K d 
JOIN solvents s
ON d.solvent_id = s.id
ORDER BY d.diffusion_coefficient DESC;
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
    df["diffusion_coefficient"],
    color=bar_colors
)

plt.xlabel("Diffusion Coefficient (m²/s)")
plt.ylabel("Solvent")
plt.title("Diffusion Coefficient at 300 K by Chemical Family")
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
plot_file = plot_path / "04_diffusion_coefficient_300K_.png"
plt.savefig(plot_file, dpi=300)

plt.show()
conn.close()