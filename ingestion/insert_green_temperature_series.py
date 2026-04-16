import sqlite3
import math
from pathlib import Path

db_path = Path(__file__).resolve().parents[1] / "database" / "solventsdb.sqlite"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

green_temperature_series = [
(
    1,   #series_id
    1,   #solvent_id --- MXY----
    275, #temperature_K
    2.815e-9,   #msd_slope
    0.469e-9,   #diffusion_coefficient
    1 / 275,    # 1 / T
    math.log(0.469e-9),   #lnD
    "m²/s",
    "MXY temperature-dependent diffusion point from molecular COM MSD."
),
(
    2,   #series_id
    1,   #solvent_id --- MXY----
    300, #temperature_K
    4.977e-9,   #msd_slope
    0.845e-9,   #diffusion_coefficient
    1 / 300,    # 1 / T
    math.log(0.845e-9),   #lnD
    "m²/s",
    "MXY temperature-dependent diffusion point from molecular COM MSD."
),
(
    3,   #series_id
    1,   #solvent_id --- MXY----
    325, #temperature_K
    5.883e-9,   #msd_slope
    0.980e-9,   #diffusion_coefficient
    1 / 325,    # 1 / T
    math.log(0.980e-9),   #lnD
    "m²/s",
    "MXY temperature-dependent diffusion point from molecular COM MSD."
),
(
    4,   #series_id
    1,   #solvent_id --- MXY----
    350, #temperature_K
    7.836e-9,   #msd_slope
    1.306e-9,   #diffusion_coefficient
    1 / 350,    # 1 / T
    math.log(1.306e-9),   #lnD
    "m²/s",
    "MXY temperature-dependent diffusion point from molecular COM MSD."
),
(
    5,   #series_id
    1,   #solvent_id --- MXY----
    375, #temperature_K
    10.435e-9,   #msd_slope
    1.739e-9,   #diffusion_coefficient
    1 / 375,    # 1 / T
    math.log(1.739e-9),   #lnD
    "m²/s",
    "MXY temperature-dependent diffusion point from molecular COM MSD."
),
(
    6,   #series_id
    1,   #solvent_id --- MXY----
    400, #temperature_K
    12.463e-9,   #msd_slope
    2.077e-9,   #diffusion_coefficient
    1 / 400,    # 1 / T
    math.log(2.077e-9),   #lnD
    "m²/s",
    "MXY temperature-dependent diffusion point from molecular COM MSD."
),
(
    7,   #series_id
    2,   #solvent_id --- MS----
    300, #temperature_K
    3.173e-9,   #msd_slope
    0.528e-9,   #diffusion_coefficient
    1 / 300,    # 1 / T
    math.log(0.528e-9),   #lnD
    "m²/s",
    "MS temperature-dependent diffusion point from molecular COM MSD."
),
(
    8,   #series_id
    2,   #solvent_id --- MS----
    325, #temperature_K
    4.902e-9,   #msd_slope
    0.817e-9,   #diffusion_coefficient
    1 / 325,    # 1 / T
    math.log(0.817e-9),   #lnD
    "m²/s",
    "MS temperature-dependent diffusion point from molecular COM MSD."
),
(
    9,   #series_id
    2,   #solvent_id --- MS----
    350, #temperature_K
    5.783e-9,   #msd_slope
    0.963e-9,   #diffusion_coefficient
    1 / 350,    # 1 / T
    math.log(0.963e-9),   #lnD
    "m²/s",
    "MS temperature-dependent diffusion point from molecular COM MSD."
),
(
    10,   #series_id
    2,   #solvent_id --- MS----
    375, #temperature_K
    8.004e-9,   #msd_slope
    1.334e-9,   #diffusion_coefficient
    1 / 375,    # 1 / T
    math.log(1.334e-9),   #lnD
    "m²/s",
    "MS temperature-dependent diffusion point from molecular COM MSD."
),
(
    11,   #series_id
    2,   #solvent_id --- MS----
    400, #temperature_K
    9.922e-9,   #msd_slope
    1.653e-9,   #diffusion_coefficient
    1 / 400,    # 1 / T
    math.log(1.653e-9),   #lnD
    "m²/s",
    "MS temperature-dependent diffusion point from molecular COM MSD."
),
(
    12,   #series_id
    2,   #solvent_id --- MS----
    425, #temperature_K
    10.971e-9,   #msd_slope
    1.828e-9,   #diffusion_coefficient
    1 / 425,    # 1 / T
    math.log(1.828e-9),   #lnD
    "m²/s",
    "MS temperature-dependent diffusion point from molecular COM MSD."
),
(
    13,   #series_id
    3,   #solvent_id --- AP----
    300, #temperature_K
    1.546e-9,   #msd_slope
    0.257e-9,   #diffusion_coefficient
    1 / 300,    # 1 / T
    math.log(0.257e-9),   #lnD
    "m²/s",
    "AP temperature-dependent diffusion point from molecular COM MSD."
),
(
    14,   #series_id
    3,   #solvent_id --- AP----
    325, #temperature_K
    2.002e-9,   #msd_slope
    0.333e-9,   #diffusion_coefficient
    1 / 325,    # 1 / T
    math.log(0.333e-9),   #lnD
    "m²/s",
    "AP temperature-dependent diffusion point from molecular COM MSD."
),
(
    15,   #series_id
    3,   #solvent_id --- AP----
    350, #temperature_K
    3.696e-9,   #msd_slope
    0.616e-9,   #diffusion_coefficient
    1 / 350,    # 1 / T
    math.log(0.616e-9),   #lnD
    "m²/s",
    "AP temperature-dependent diffusion point from molecular COM MSD."
),
(
    16,   #series_id
    3,   #solvent_id --- AP----
    375, #temperature_K
    5.072e-9,   #msd_slope
    0.845e-9,   #diffusion_coefficient
    1 / 375,    # 1 / T
    math.log(0.845e-9),   #lnD
    "m²/s",
    "AP temperature-dependent diffusion point from molecular COM MSD."
),
(
    17,   #series_id
    3,   #solvent_id --- AP----
    400, #temperature_K
    6.070e-9,   #msd_slope
    1.011e-9,   #diffusion_coefficient
    1 / 400,    # 1 / T
    math.log(1.011e-9),   #lnD
    "m²/s",
    "AP temperature-dependent diffusion point from molecular COM MSD."
),
(
    18,   #series_id
    3,   #solvent_id --- AP----
    425, #temperature_K
    7.625e-9,   #msd_slope
    1.270e-9,   #diffusion_coefficient
    1 / 425,    # 1 / T
    math.log(1.270e-9),   #lnD
    "m²/s",
    "AP temperature-dependent diffusion point from molecular COM MSD."
),
(
    19,   #series_id
    4,   #solvent_id --- 2-MeTHF----
    200, #temperature_K
    0.604e-9,   #msd_slope
    0.100e-9,   #diffusion_coefficient
    1 / 200,    # 1 / T
    math.log(0.100e-9),   #lnD
    "m²/s",
    "2-MeTHF temperature-dependent diffusion point from molecular COM MSD."
),
(
    20,   #series_id
    4,   #solvent_id --- 2-MeTHF----
    225, #temperature_K
    1.182e-9,   #msd_slope
    0.197e-9,   #diffusion_coefficient
    1 / 225,    # 1 / T
    math.log(0.197e-9),   #lnD
    "m²/s",
    "2-MeTHF temperature-dependent diffusion point from molecular COM MSD."
),
(
    21,   #series_id
    4,   #solvent_id --- 2-MeTHF----
    250, #temperature_K
    2.184e-9,   #msd_slope
    0.364e-9,   #diffusion_coefficient
    1 / 250,    # 1 / T
    math.log(0.364e-9),   #lnD
    "m²/s",
    "2-MeTHF temperature-dependent diffusion point from molecular COM MSD."
),
(
    22,   #series_id
    4,   #solvent_id --- 2-MeTHF----
    275, #temperature_K
    2.732e-9,   #msd_slope
    0.455e-9,   #diffusion_coefficient
    1 / 275,    # 1 / T
    math.log(0.455e-9),   #lnD
    "m²/s",
    "2-MeTHF temperature-dependent diffusion point from molecular COM MSD."
),
(
    23,   #series_id
    4,   #solvent_id --- 2-MeTHF----
    300, #temperature_K
    4.615e-9,   #msd_slope
    0.769e-9,   #diffusion_coefficient
    1 / 300,    # 1 / T
    math.log(0.769e-9),   #lnD
    "m²/s",
    "2-MeTHF temperature-dependent diffusion point from molecular COM MSD."
),
(
    24,   #series_id
    4,   #solvent_id --- 2-MeTHF----
    325, #temperature_K
    4.829e-9,   #msd_slope
    0.804e-9,   #diffusion_coefficient
    1 / 325,    # 1 / T
    math.log(0.804e-9),   #lnD
    "m²/s",
    "2-MeTHF temperature-dependent diffusion point from molecular COM MSD."
),
(
    25,   #series_id
    5,   #solvent_id --- NMP----
    300, #temperature_K
    1.551e-9,   #msd_slope
    0.258e-9,   #diffusion_coefficient
    1 / 300,    # 1 / T
    math.log(0.258e-9),   #lnD
    "m²/s",
    "NMP temperature-dependent diffusion point from molecular COM MSD."
),
(
    26,   #series_id
    5,   #solvent_id --- NMP----
    325, #temperature_K
    2.683e-9,   #msd_slope
    0.447e-9,   #diffusion_coefficient
    1 / 325,    # 1 / T
    math.log(0.447e-9),   #lnD
    "m²/s",
    "NMP temperature-dependent diffusion point from molecular COM MSD."
),
(
    27,   #series_id
    5,   #solvent_id --- NMP----
    350, #temperature_K
    3.673e-9,   #msd_slope
    0.612e-9,   #diffusion_coefficient
    1 / 350,    # 1 / T
    math.log(0.612e-9),   #lnD
    "m²/s",
    "NMP temperature-dependent diffusion point from molecular COM MSD."
),
(
    28,   #series_id
    5,   #solvent_id --- NMP----
    375, #temperature_K
    4.210e-9,   #msd_slope
    0.701e-9,   #diffusion_coefficient
    1 / 375,    # 1 / T
    math.log(0.701e-9),   #lnD
    "m²/s",
    "NMP temperature-dependent diffusion point from molecular COM MSD."
),
(
    29,   #series_id
    5,   #solvent_id --- NMP----
    400, #temperature_K
    4.914e-9,   #msd_slope
    0.819e-9,   #diffusion_coefficient
    1 / 400,    # 1 / T
    math.log(0.819e-9),   #lnD
    "m²/s",
    "NMP temperature-dependent diffusion point from molecular COM MSD."
),
(
    30,   #series_id
    5,   #solvent_id --- NMP----
    425, #temperature_K
    6.857e-9,   #msd_slope
    1.142e-9,   #diffusion_coefficient
    1 / 425,    # 1 / T
    math.log(1.142e-9),   #lnD
    "m²/s",
    "NMP temperature-dependent diffusion point from molecular COM MSD."
),
(
    31,   #series_id
    6,   #solvent_id --- CPME----
    250, #temperature_K
    1.414e-9,   #msd_slope
    0.235e-9,   #diffusion_coefficient
    1 / 250,    # 1 / T
    math.log(0.235e-9),   #lnD
    "m²/s",
    "CPME temperature-dependent diffusion point from molecular COM MSD."
),
(
    32,   #series_id
    6,   #solvent_id --- CPME----
    275, #temperature_K
    2.330e-9,   #msd_slope
    0.388e-9,   #diffusion_coefficient
    1 / 275,    # 1 / T
    math.log(0.388e-9),   #lnD
    "m²/s",
    "CPME temperature-dependent diffusion point from molecular COM MSD."
),
(
    33,   #series_id
    6,   #solvent_id --- CPME----
    300, #temperature_K
    3.806e-9,   #msd_slope
    0.634e-9,   #diffusion_coefficient
    1 / 300,    # 1 / T
    math.log(0.634e-9),   #lnD
    "m²/s",
    "CPME temperature-dependent diffusion point from molecular COM MSD."
),
(
    34,   #series_id
    6,   #solvent_id --- CPME----
    325, #temperature_K
    4.773e-9,   #msd_slope
    0.795e-9,   #diffusion_coefficient
    1 / 325,    # 1 / T
    math.log(0.795e-9),   #lnD
    "m²/s",
    "CPME temperature-dependent diffusion point from molecular COM MSD."
),
(
    35,   #series_id
    6,   #solvent_id --- CPME----
    350, #temperature_K
    6.810e-9,   #msd_slope
    1.135e-9,   #diffusion_coefficient
    1 / 350,    # 1 / T
    math.log(1.135e-9),   #lnD
    "m²/s",
    "CPME temperature-dependent diffusion point from molecular COM MSD."
),
(
    36,   #series_id
    6,   #solvent_id --- CPME----
    375, #temperature_K
    7.445e-9,   #msd_slope
    1.240e-9,   #diffusion_coefficient
    1 / 375,    # 1 / T
    math.log(1.240e-9),   #lnD
    "m²/s",
    "CPME temperature-dependent diffusion point from molecular COM MSD."
    )
]
cur.executemany("""
INSERT INTO green_temperature_series(
    series_id,
    solvent_id,
    temperature_K,
    msd_slope,
    diffusion_coefficient,
    inverse_temperature,
    ln_diffusion,
    diffusion_unit,
    notes
)
VALUES(?,?,?,?,?,?,?,?,?)""",green_temperature_series)
conn.commit()
conn.close()
print("Data has loaded successfully!")
