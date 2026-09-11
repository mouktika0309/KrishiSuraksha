# ============================================================
# KRISHISURAKSHA - SENSOR MODULE
# ============================================================
#
# This file will eventually read:
#
# MPU6050
# ADXL345
# MLX90614
# DS18B20
# DHT11
#
# Currently it provides simulated sensor values so that
# software development can continue before the Raspberry Pi
# sensor testing is complete.
# ============================================================

import random


# ============================================================
# SIMULATED SENSOR DATA
# ============================================================

def get_sensor_data():

    return {

        # MPU6050 / ADXL345
        "roll": round(
            random.uniform(0, 12),
            2
        ),

        "pitch": round(
            random.uniform(0, 8),
            2
        ),

        # Temperature sensor
        "temperature": round(
            random.uniform(50, 90),
            1
        ),

        # RPM
        #
        # Currently simulated because an RPM sensor has
        # not yet been integrated.
        #
        "rpm": random.randint(
            1000,
            2500
        )
    }


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    print("Sensor Module Test")

    data = get_sensor_data()

    print(data)