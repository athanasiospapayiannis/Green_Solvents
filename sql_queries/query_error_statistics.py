import sqlite3
conn = sqlite3.connect('../database/solventsdb.sqlite')
cur = conn.cursor()

#average error
cur.execute("""
SELECT AVG(relative_error_percent)
FROM validation_results
""")
avg_error = cur.fetchone()[0]

#best solvent
cur.execute("""
SELECT solvent_name, relative_error_percent
FROM validation_results
ORDER BY relative_error_percent ASC
LIMIT 1
""")
best_solvent = cur.fetchone()

#worst solvent
cur.execute("""
SELECT solvent_name, relative_error_percent
FROM validation_results
ORDER BY relative_error_percent DESC
LIMIT 1
""")
worst_solvent = cur.fetchone()

#Total count
cur.execute("""
SELECT COUNT(*)
FROM validation_results
""")
total_solvents = cur.fetchone()[0]

print("=== Validation Error Statistics ===")
print(f"Average error: {avg_error:.2f}%")
print(f"Best agreement: {best_solvent[0]} ({best_solvent[1]:.2f}%)")
print(f"Worst agreement: {worst_solvent[0]} ({worst_solvent[1]:.2f}%)")
print(f"Validation solvents: {total_solvents}")
conn.close()
