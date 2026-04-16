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
MAX(g.diffusion_coefficient) / MIN(diffusion_coefficient) AS thermal_acceleration_ratio
FROM green_temperature_series g
JOIN solvents s
ON g.solvent_id = s.id
GROUP BY s.name
ORDER BY thermal_acceleration_ratio DESC;
"""

df = pd.read_sql_query(query,conn)

df["ln_ratio"] = np.log(df["thermal_acceleration_ratio"])
print(df)
conn.close()