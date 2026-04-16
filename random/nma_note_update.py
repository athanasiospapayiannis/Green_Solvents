import sqlite3
conn = sqlite3.connect('solventsdb.sqlite')
cur = conn.cursor()

cur.execute("""
UPDATE validation_results
SET notes = 'Higher error likely due to insufficient simulation length and incomplete MSD stabilization'
WHERE solvent_name = 'N-Methylaniline'
""")
conn.commit()
conn.close()
print("NMA updated successfully!")
