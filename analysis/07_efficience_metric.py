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
d.diffusion_coefficient,
a.activation_energy_kcal_mol,
d.diffusion_coefficient / a.activation_energy_kcal_mol AS efficiency_metric
FROM solvents s
JOIN green_diffusion_results_300K d
ON s.id = d.solvent_id
JOIN green_arrhenius_parameters a
ON s.id = a.solvent_id
ORDER BY efficiency_metric DESC;
"""
df = pd.read_sql_query(query, conn)
print(df)


plt.figure(figsize=(10,6))
plt.barh(df["name"], df["efficiency_metric"])

plt.xlabel("Efficiency (D / Ea )")
plt.title("Diffusion per Activation Energy")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
conn.close()