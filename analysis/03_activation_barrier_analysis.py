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
g.activation_energy_kcal_mol,
ABS(g.arrhenius_slope_K) AS abs_arrhenius_slope
FROM green_arrhenius_parameters g
JOIN solvents s
ON g.solvent_id = s.id
ORDER BY g.activation_energy_kcal_mol DESC;
"""
df = pd.read_sql_query(query, conn)

df["relative barrier"] = (
    df["activation_energy_kcal_mol"] / df["activation_energy_kcal_mol"].max()
)
print(df)