import sqlite3
conn = sqlite3.connect('solventsdb.sqlite')
cur = conn.cursor()

query = """
SELECT code, name, viscosity_25C
FROM solvents
WHERE aromatic_ring_count = 1
ORDER BY viscosity_25C ASC
"""

cur.execute(query)
results = cur.fetchall()
print("=== Aromatic Solvents Sorted by Viscosity ===")
for code,name,viscosity in results:
    print(f"{code} | {name} | {viscosity:.2f} mPa·s")


conn.close()
