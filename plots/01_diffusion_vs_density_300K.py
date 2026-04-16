from pathlib import Path
import sqlite3
import pandas as pd
import numpy as np
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
d.density_g_cm3
FROM green_diffusion_results_300K d
JOIN solvents s
ON d.solvent_id = s.id
ORDER BY d.diffusion_coefficient DESC;
"""

df = pd.read_sql_query(query, conn)

#====PLOT======
plt.figure(figsize=(8,6))
plt.scatter(df["density_g_cm3"], df["diffusion_coefficient"])

for _, row in df.iterrows():
    plt.text(
        row["density_g_cm3"],
        row["diffusion_coefficient"],
        row["name"],
        fontsize=8
    )
plt.xlabel("Density (g/cm³)")
plt.ylabel("Diffusion Coefficient (m²/s)")
plt.title("Diffusion at 300 K - Density of MD simulation")
plt.grid(True)
plt.tight_layout()

#SAVE FILE
plot_file = plot_path / "01_Diffusion_vs_Density_at_300K.png"
plt.savefig(plot_file, dpi = 300)
plt.show()
conn.close()