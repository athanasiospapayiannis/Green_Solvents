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

#====PLOT======
plt.figure(figsize=(8,6))
plt.scatter(df["activation_energy_kcal_mol"], df["thermal_acceleration_ratio"])

for _, row in df.iterrows():
    plt.text(
        row["activation_energy_kcal_mol"],
        row["thermal_acceleration_ratio"],
        row["name"],
        fontsize=8
    )
plt.xlabel("Activation Energy (kcal/mol)")
plt.ylabel("Thermal Acceleration Ratio")
plt.title("Energy Barrier - Thermal Acceleration Ratio")
plt.grid(True)
plt.tight_layout()

#SAVE FILE
raw_plot_file = plot_path / "02_barrier_vs_thermal_response.png"
plt.savefig(raw_plot_file, dpi = 300)


#====LINEAR FIT
x = df["activation_energy_kcal_mol"]
y = df["thermal_acceleration_ratio"]

m , b = np.polyfit(x,y,1)
x_fit = np.linspace(x.min(), x.max(), 100)
y_fit = m * x_fit + b
plt.plot(x_fit, y_fit, linestyle="--")

fit_plot_file = plot_path / "02_barrier_vs_thermal_response_with_fit.png"
plt.savefig(fit_plot_file, dpi = 300)
plt.show()
conn.close()