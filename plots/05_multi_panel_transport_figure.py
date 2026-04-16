from pathlib import Path
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# =========================
# PATHS
# =========================
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = PROJECT_ROOT / "database" / "solventsdb.sqlite"
PLOTS_PATH = PROJECT_ROOT / "plots"

# =========================
# DATABASE
# =========================
conn = sqlite3.connect(DB_PATH)

# =========================
# QUERY 1: ACTIVATION ENERGY
# =========================
query_energy = """
SELECT s.name,
       g.activation_energy_kcal_mol
FROM green_arrhenius_parameters g
JOIN solvents s
ON g.solvent_id = s.id
ORDER BY g.activation_energy_kcal_mol DESC;
"""

df_energy = pd.read_sql_query(query_energy, conn)

# =========================
# QUERY 2: DIFFUSION 300 K
# =========================
query_diff = """
SELECT s.name,
       d.diffusion_coefficient
FROM green_diffusion_results_300K d
JOIN solvents s
ON d.solvent_id = s.id
ORDER BY d.diffusion_coefficient DESC;
"""

df_diff = pd.read_sql_query(query_diff, conn)

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

group_colors = {
    "Aromatic ketone": "tab:red",
    "Lactam carbonyl": "tab:orange",
    "Cyclic ethers": "tab:blue",
    "Aromatic hydrocarbons": "tab:green"
}

df_energy["chemical_group"] = df_energy["name"].map(chemical_groups)
df_diff["chemical_group"] = df_diff["name"].map(chemical_groups)

energy_colors = df_energy["chemical_group"].map(group_colors)
diff_colors = df_diff["chemical_group"].map(group_colors)

# =========================
# MULTI PANEL FIGURE
# =========================
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# LEFT PANEL
axes[0].barh(
    df_energy["name"],
    df_energy["activation_energy_kcal_mol"],
    color=energy_colors
)
axes[0].set_title("Activation Energy")
axes[0].set_xlabel("kcal/mol")
axes[0].invert_yaxis()
axes[0].grid(axis="x")

# RIGHT PANEL
axes[1].barh(
    df_diff["name"],
    df_diff["diffusion_coefficient"],
    color=diff_colors
)
axes[1].set_title("300 K Diffusion")
axes[1].set_xlabel("m²/s")
axes[1].invert_yaxis()
axes[1].grid(axis="x")

# =========================
# LEGEND
# =========================
legend_elements = [
    Patch(facecolor=color, label=group)
    for group, color in group_colors.items()
]

fig.legend(
    handles=legend_elements,
    title="Chemical Family",
    loc="lower center",
    ncol=4
)

plt.tight_layout(rect=[0, 0.08, 1, 1])

# =========================
# SAVE
# =========================
plot_file = PLOTS_PATH / "09_multi_panel_transport_figure.png"
plt.savefig(plot_file, dpi=300)

plt.show()
conn.close()