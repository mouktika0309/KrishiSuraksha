# ============================================================
# KRISHISURAKSHA - RISK ENGINE
# ============================================================

def calculate_risk(
    roll,
    temperature,
    rpm,
    terrain_depth,
    obstacle_distance
):

    # ========================================================
    # INITIAL RISKS
    # ========================================================

    rollover = 0
    terrain = 0
    collision = 0
    machine = 0


    # ========================================================
    # ROLLOVER RISK
    # ========================================================

    if abs(roll) > 5:
        rollover += 20

    if abs(roll) > 10:
        rollover += 30

    if abs(roll) > 15:
        rollover += 40

    rollover = min(rollover, 100)


    # ========================================================
    # TERRAIN RISK
    # ========================================================

    if terrain_depth > 0.5:
        terrain += 20

    if terrain_depth > 1.0:
        terrain += 30

    if terrain_depth > 1.5:
        terrain += 40

    terrain = min(terrain, 100)


    # ========================================================
    # COLLISION RISK
    # ========================================================

    if obstacle_distance < 10:
        collision += 20

    if obstacle_distance < 5:
        collision += 30

    if obstacle_distance < 2:
        collision += 40

    collision = min(collision, 100)


    # ========================================================
    # MACHINE RISK
    # ========================================================

    if temperature > 80:
        machine += 20

    if temperature > 90:
        machine += 30

    if temperature > 100:
        machine += 40

    if rpm > 2500:
        machine += 20

    if rpm > 3000:
        machine += 20

    machine = min(machine, 100)


    # ========================================================
    # OVERALL RISK
    # ========================================================

    overall_risk = (
        rollover * 0.35
        + terrain * 0.20
        + collision * 0.30
        + machine * 0.15
    )

    overall_risk = int(
        min(overall_risk, 100)
    )


    # ========================================================
    # SAFETY SCORE
    # ========================================================

    safety_score = 100 - overall_risk

    safety_score = max(
        0,
        min(safety_score, 100)
    )


    # ========================================================
    # STATUS
    # ========================================================

    if safety_score >= 70:

        status = "SAFE"

    elif safety_score >= 40:

        status = "WARNING"

    else:

        status = "CRITICAL"


    # ========================================================
    # ALERTS
    # ========================================================

    alerts = []

    if rollover >= 50:
        alerts.append("High Rollover Risk")

    if terrain >= 50:
        alerts.append("Terrain Hazard Detected")

    if collision >= 50:
        alerts.append("Obstacle Ahead")

    if machine >= 50:
        alerts.append("Engine Health Warning")


    # ========================================================
    # RETURN RESULT
    # ========================================================

    return {
        "rollover": rollover,
        "terrain": terrain,
        "collision": collision,
        "machine": machine,
        "overall": overall_risk,
        "safety_score": safety_score,
        "status": status,
        "alerts": alerts
    }


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    result = calculate_risk(
        roll=8,
        temperature=85,
        rpm=2200,
        terrain_depth=0.8,
        obstacle_distance=6
    )

    print("Risk Engine Test")
    print(result)