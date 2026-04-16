import sqlite3
conn = sqlite3.connect('solventsdb.sqlite')
cur = conn.cursor()

query = """
SELECT solvent_name, relative_error_percent
FROM validation_results
ORDER BY relative_error_percent ASC
"""
cur.execute(query)
results = cur.fetchall()

print("=== Validation Accuracy Ranking ===")
for solvent, error in results:
    print(f"{solvent:20} | error = {error:.2f}%")
conn.close()
