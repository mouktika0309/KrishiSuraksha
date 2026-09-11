# ============================================================
# KRISHISURAKSHA - DASHBOARD
# ============================================================

import streamlit as st
import pandas as pd
import random

from risk_engine import calculate_risk
from data_source import (
    get_demo_data,
    get_raspberry_pi_data
)


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="KrishiSuraksha",
    page_icon="🚜",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("🚜 KRISHISURAKSHA")

st.markdown(
    "### Smart Tractor Safety & Monitoring System"
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("⚙️ Control Panel")

mode = st.sidebar.radio(
    "Data Source",
    [
        "DEMO MODE",
        "LIVE HARDWARE"
    ]
)


# ============================================================
# DATA
# ============================================================

if mode == "DEMO MODE":

    scenario = st.sidebar.selectbox(
        "Select Demo Scenario",
        [
            "SAFE",
            "WARNING",
            "CRITICAL"
        ]
    )

    data = get_demo_data(
        scenario
    )

else:

    data = get_raspberry_pi_data()


# ============================================================
# SENSOR DATA
# ============================================================

sensor_data = {

    "roll": data["roll"],

    "pitch": data["pitch"],

    "temperature": data["temperature"],

    "rpm": data["rpm"]
}


# ============================================================
# VISION DATA
# ============================================================

vision_data = {

    "obstacle_distance":
        data["obstacle_distance"],

    "terrain_depth":
        data["terrain_depth"]
}


# ============================================================
# RISK ENGINE
# ============================================================

result = calculate_risk(

    roll=sensor_data["roll"],

    temperature=sensor_data["temperature"],

    rpm=sensor_data["rpm"],

    terrain_depth=
        vision_data["terrain_depth"],

    obstacle_distance=
        vision_data["obstacle_distance"]
)


# ============================================================
# DATA SOURCE STATUS
# ============================================================

if mode == "DEMO MODE":

    st.info(
        "🧪 Demo Mode — Simulated Data"
    )

else:

    st.info(
        "📡 Live Hardware Mode — Raspberry Pi"
    )


# ============================================================
# SAFETY SCORE
# ============================================================

st.markdown("---")

st.subheader(
    "🛡️ Overall Safety Score"
)

safety_score = result["safety_score"]

st.progress(
    safety_score / 100
)


col1, col2 = st.columns(2)


with col1:

    st.metric(
        "Safety Score",
        f"{safety_score}/100"
    )


with col2:

    if result["status"] == "SAFE":

        st.success(
            "🟢 SAFE"
        )

    elif result["status"] == "WARNING":

        st.warning(
            "🟡 WARNING"
        )

    else:

        st.error(
            "🔴 CRITICAL"
        )


# ============================================================
# RISK BREAKDOWN
# ============================================================

st.markdown("---")

st.subheader(
    "⚠️ Risk Breakdown"
)


c1, c2, c3, c4 = st.columns(4)


with c1:

    st.metric(
        "Rollover Risk",
        f"{result['rollover']}/100"
    )


with c2:

    st.metric(
        "Terrain Risk",
        f"{result['terrain']}/100"
    )


with c3:

    st.metric(
        "Collision Risk",
        f"{result['collision']}/100"
    )


with c4:

    st.metric(
        "Machine Risk",
        f"{result['machine']}/100"
    )


# ============================================================
# VEHICLE HEALTH
# ============================================================

st.markdown("---")

st.subheader(
    "🚜 Vehicle Health"
)


c1, c2, c3 = st.columns(3)


with c1:

    st.metric(
        "Engine Temperature",
        f"{sensor_data['temperature']} °C"
    )


with c2:

    st.metric(
        "RPM",
        sensor_data["rpm"]
    )


with c3:

    vehicle_health = (
        100 - result["machine"]
    )

    st.metric(
        "Vehicle Health",
        f"{vehicle_health}%"
    )


# ============================================================
# LIVE SENSOR VALUES
# ============================================================

st.markdown("---")

st.subheader(
    "📡 Live Sensor Values"
)


s1, s2, s3, s4 = st.columns(4)


with s1:

    st.metric(
        "Roll Angle",
        f"{sensor_data['roll']}°"
    )


with s2:

    st.metric(
        "Pitch Angle",
        f"{sensor_data['pitch']}°"
    )


with s3:

    st.metric(
        "Obstacle Distance",
        f"{vision_data['obstacle_distance']} m"
    )


with s4:

    st.metric(
        "Terrain Depth",
        f"{vision_data['terrain_depth']} m"
    )


# ============================================================
# ALERTS
# ============================================================

st.markdown("---")

st.subheader(
    "🚨 Active Alerts"
)


if len(result["alerts"]) == 0:

    st.success(
        "✅ No active hazards detected."
    )

else:

    for alert in result["alerts"]:

        st.warning(
            f"⚠️ {alert}"
        )


# ============================================================
# RECOMMENDED ACTIONS
# ============================================================

st.markdown("---")

st.subheader(
    "💡 Recommended Actions"
)


recommendation_found = False


if result["rollover"] >= 50:

    st.warning(
        "🚜 Reduce speed and avoid side slopes."
    )

    recommendation_found = True


if result["terrain"] >= 50:

    st.warning(
        "⛰️ Dangerous terrain detected ahead."
    )

    recommendation_found = True


if result["collision"] >= 50:

    st.warning(
        "🚨 Obstacle nearby. Stop immediately."
    )

    recommendation_found = True


if result["machine"] >= 50:

    st.warning(
        "🔧 Engine requires inspection."
    )

    recommendation_found = True


if not recommendation_found:

    st.success(
        "✅ Continue operation normally."
    )


# ============================================================
# RISK TREND
# ============================================================

st.markdown("---")

st.subheader(
    "📈 Risk Trend"
)


risk_history = []


for _ in range(20):

    value = (
        result["overall"]
        + random.randint(-10, 10)
    )

    value = max(
        0,
        min(
            100,
            value
        )
    )

    risk_history.append(
        value
    )


df = pd.DataFrame(
    {
        "Risk Score": risk_history
    }
)


st.line_chart(df)


# ============================================================
# HAZARD LOG
# ============================================================

st.markdown("---")

st.subheader(
    "📋 Hazard Log"
)


logs = [

    "12:01 - Terrain anomaly detected",

    "12:02 - Roll angle increased",

    "12:03 - Obstacle detected",

    "12:04 - Engine temperature rising"
]


for log in logs:

    st.write(log)


# ============================================================
# CAMERA FEED
# ============================================================

st.markdown("---")

st.subheader(
    "📷 IR Camera / Vision"
)


st.info(
    "📷 IR Camera Feed\n\n"
    "OpenCV camera integration will be connected "
    "after the Raspberry Pi camera test."
)


# ============================================================
# DEBUG DATA
# ============================================================

st.markdown("---")

with st.expander(
    "🔧 Debug Data"
):

    st.json(
        {
            "data_source": mode,

            "sensor_data":
                sensor_data,

            "vision_data":
                vision_data,

            "risk_result":
                result
        }
    )