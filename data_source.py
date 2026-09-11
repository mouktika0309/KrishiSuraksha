# ============================================================
# KRISHISURAKSHA - DATA SOURCE
# ============================================================

import random


# ============================================================
# DEMO DATA
# ============================================================

def get_demo_data(scenario):

    if scenario == "SAFE":

        return {
            "roll": 2,
            "pitch": 1,
            "temperature": 60,
            "rpm": 1200,
            "obstacle_distance": 15,
            "terrain_depth": 0.2
        }


    elif scenario == "WARNING":

        return {
            "roll": 8,
            "pitch": 3,
            "temperature": 85,
            "rpm": 2200,
            "obstacle_distance": 6,
            "terrain_depth": 0.8
        }


    elif scenario == "CRITICAL":

        return {
            "roll": 16,
            "pitch": 7,
            "temperature": 105,
            "rpm": 2900,
            "obstacle_distance": 2,
            "terrain_depth": 1.6
        }


    else:

        return {
            "roll": 0,
            "pitch": 0,
            "temperature": 25,
            "rpm": 0,
            "obstacle_distance": 20,
            "terrain_depth": 0
        }


# ============================================================
# SIMULATED LIVE DATA
# ============================================================

def get_simulated_live_data():

    return {

        "roll": round(
            random.uniform(0, 12),
            2
        ),

        "pitch": round(
            random.uniform(0, 8),
            2
        ),

        "temperature": round(
            random.uniform(50, 90),
            1
        ),

        "rpm": random.randint(
            1000,
            2500
        ),

        "obstacle_distance": round(
            random.uniform(5, 20),
            2
        ),

        "terrain_depth": round(
            random.uniform(0.1, 1.0),
            2
        )
    }


# ============================================================
# RASPBERRY PI DATA
# ============================================================

def get_raspberry_pi_data():

    # --------------------------------------------------------
    # TEMPORARY
    #
    # Raspberry Pi connection will be added later.
    # --------------------------------------------------------

    return get_simulated_live_data()