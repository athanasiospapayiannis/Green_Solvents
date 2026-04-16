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

#connections
conn = sqlite3.connect(db_path)
cur = conn.cursor()

query = """
SELECT s.name,
d.diffusion_coefficient,
d.density_g_cm3
FROM green_diffusion_results_300K d
JOIN solvents s
ON d.solvent_id = s.id
ORDER BY d.diffusion_coefficient DESC;
"""

#LOAD DATAFRAME
df = pd.read_sql_query(query,conn)

#Engineering Features
df["Relative to top"] = (
    df["diffusion_coefficient"] / df["diffusion_coefficient"].max()
)

df["Relative to bottom"] = (
   df["diffusion_coefficient"] / df["diffusion_coefficient"].min()
)

df["ln_diffusion"] = np.log(df["diffusion_coefficient"])

#PREVIEW
print(df)
conn.close()