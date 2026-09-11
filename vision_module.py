# ============================================================
# KRISHISURAKSHA - VISION MODULE
# ============================================================
#
# This module is responsible for:
#
# 1. Camera handling
# 2. OpenCV image processing
# 3. Future obstacle detection
# 4. Future stereo/depth processing
#
# IMPORTANT:
#
# Your OV5647 is a Raspberry Pi camera.
# We will connect the actual Pi camera after the hardware
# camera test is completed.
#
# ============================================================

import cv2


# ============================================================
# OPENCV TEST
# ============================================================

def test_opencv():

    print("OpenCV version:", cv2.__version__)

    return True


# ============================================================
# PROCESS IMAGE
# ============================================================

def process_frame(frame):

    """
    Basic OpenCV processing.

    Currently this function:
    - receives a camera frame
    - converts it to grayscale
    - returns the processed frame

    Later we can add:
    - obstacle detection
    - stereo depth
    - terrain detection
    """

    if frame is None:

        return None

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    return gray


# ============================================================
# VISION DATA
# ============================================================

def get_vision_data():

    """
    Temporary vision data.

    These values are placeholders until the actual
    camera and OpenCV processing are integrated.
    """

    return {
        "obstacle_distance": 15,
        "terrain_depth": 0.2
    }


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    print("Vision Module Test")

    test_opencv()

    data = get_vision_data()

    print(data)