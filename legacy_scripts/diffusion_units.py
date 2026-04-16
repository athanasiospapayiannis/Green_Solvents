import sqlite3
conn = sqlite3.connect('solventsdb.sqlite')
cur = conn.cursor()

cur.execute("""
ALTER TABLE validation_results
ADD COLUMN diffusion_unit TEXT
""")
conn.commit()
conn.close()
print("diffusion_unit column added!")
