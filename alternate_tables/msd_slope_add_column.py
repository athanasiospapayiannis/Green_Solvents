import sqlite3
conn = sqlite3.connect('solventsdb.sqlite')
cur = conn.cursor()

cur.execute("""
ALTER TABLE validation_results
ADD COLUMN msd_slope REAL
""")

conn.commit()
conn.close()

print("msd_slope columb successfully added!")
