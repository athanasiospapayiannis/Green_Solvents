import sqlite3
conn = sqlite3.connect('solventsdb.sqlite')
cur = conn.cursor()

solvents = [
    (
        1, "MXY", "m-Xylene", "C8H10",
        106.16, 0.8599, 0.58, 1, 1,
        "Aromatic non polar benchmark solvent"
    ),
    (
        2, "MS", "Mesitylene", "C9H12",
        120.19, 0.864, 1.04, 1, 1,
        "Aromatic solvent with high steric bulk"
    ),
    (
        3, "AP", "Acetophenone", "C8H8O",
        120.15, 1.03, 1.20, 1, 1,
        "Polar aromatic ketone solvent"
    ),
    (
        4, "2-MeTHF", "2-Methyltetrahydrofuran", "C5H10O",
        86.13, 0.860, 4.00, 0, 1,
        "Bio-based cyclic ether solvent"
    ),
    (   5, "NMP", "N-Methyl-2-Pyrrolidone", "C5H9ON",
        99.13, 1.028, 1.65, 0, 1,
        "Polar aprotic cyclic lactam solvent"
    ),
    (   6, "CPME", "Cyclopentyl-Methyl-Ether", "C6H12O",
        100.16, 0.860, 0.57, 0, 1,
        "Green hydrophobic cyclic ether solvent"
    )
]

cur.executemany("""
INSERT INTO solvents (
    id, code, name, formula,
    molar_mass, density_25C, viscosity_25C,
    aromatic_ring_count, halogen_free, notes
)
VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", solvents)

conn.commit()
conn.close()

print("6 green solvents inserted successfully")
