from pathlib import Path
import sqlite3
import pandas as pd
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
a.activation_energy_kcal_mol,
MAX(t.diffusion_coefficient) / MIN(t.diffusion_coefficient) AS thermal_acceleration_ratio
FROM green_arrhenius_parameters a
JOIN green_temperature_series t
ON a.solvent_id = t.solvent_id
JOIN solvents s
ON a.solvent_id = s.id
GROUP BY s.name, a.activation_energy_kcal_mol
ORDER BY thermal_acceleration_ratio DESC;
"""

df = pd.read_sql_query(query, conn)

#Correlation
corr = df["activation_energy_kcal_mol"].corr(df["thermal_acceleration_ratio"])

print(df)
print("\nCorrelation between Energy Barrier - Thermal Acceleration: ")
print(corr)

