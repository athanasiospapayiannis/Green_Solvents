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
SELECT 
    s.name,
    d.diffusion_coefficient,
    a.activation_energy_kcal_mol,
    MAX(t.diffusion_coefficient) / MIN(t.diffusion_coefficient) AS thermal_ratio
FROM solvents s
JOIN green_diffusion_results_300K d
ON s.id = d.solvent_id
JOIN green_arrhenius_parameters a
ON s.id = a.solvent_id
JOIN green_temperature_series t
ON s.id = t.solvent_id
GROUP BY s.name, d.diffusion_coefficient, a.activation_energy_kcal_mol;
"""

df = pd.read_sql_query(query, conn)

# ranking
df["rank_diffusion"] = df["diffusion_coefficient"].rank(ascending=False)
df["rank_thermal"] = df["thermal_ratio"].rank(ascending=False)
df["rank_barrier"] = df["activation_energy_kcal_mol"].rank(ascending=True)

# consistency score
df["consistency_score"] = (
    df["rank_diffusion"] +
    df["rank_thermal"] +
    df["rank_barrier"]
) / 3

df = df.sort_values("consistency_score")

print(df[[
    "name",
    "rank_diffusion",
    "rank_thermal",
    "rank_barrier",
    "consistency_score"
]])

# plot
plt.figure(figsize=(8,5))
plt.barh(df["name"], df["consistency_score"])

plt.xlabel("Consistency Score (lower is better)")
plt.title("Multi-Criteria Solvent Ranking")
plt.gca().invert_yaxis()

plt.tight_layout()


plt.show()


conn.close()