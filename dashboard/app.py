import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Wildfire Emergency Response Analytics",
    page_icon="🔥",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():

    project = Path(__file__).resolve().parent.parent

    file_path = (
        project
        / "data"
        / "processed"
        / "wildfire_analytics_2025.csv"
    )

    return pd.read_csv(file_path)


df = load_data()

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🔥 Wildfire Emergency Response Analytics")

st.markdown(
    """
    **NASA FIRMS 2025 Fire Detection Analysis**

    Analyze wildfire activity, fire intensity, geographic
    hotspots and emergency response priorities.
    """
)

st.divider()

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------

st.sidebar.header("🔎 Dashboard Filters")

# Fire intensity filter

intensity_options = [
    "Low",
    "Medium",
    "High",
    "Extreme"
]

available_intensities = [
    x for x in intensity_options
    if x in df["fire_intensity"].dropna().unique()
]

selected_intensity = st.sidebar.multiselect(
    "Fire Intensity",
    options=available_intensities,
    default=available_intensities
)

# Month filter

months = sorted(
    df["month"].dropna().unique()
)

selected_months = st.sidebar.multiselect(
    "Month",
    options=months,
    default=months
)

# Apply filters

filtered_df = df[
    df["fire_intensity"].isin(selected_intensity)
    &
    df["month"].isin(selected_months)
].copy()

if filtered_df.empty:

    st.warning(
        "No fire detections match the selected filters."
    )

    st.stop()

# --------------------------------------------------
# KPI CALCULATIONS
# --------------------------------------------------

total_fires = len(filtered_df)

high_extreme = filtered_df[
    filtered_df["fire_intensity"].isin(
        ["High", "Extreme"]
    )
]

high_extreme_count = len(high_extreme)

extreme_count = (
    filtered_df["fire_intensity"] == "Extreme"
).sum()

avg_frp = filtered_df["frp"].mean()

max_frp = filtered_df["frp"].max()

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

col1, col2, col3, col4, col5 = st.columns(5)

with col1:

    st.metric(
        "🔥 Fire Detections",
        f"{total_fires:,}"
    )

with col2:

    st.metric(
        "🟠 High / Extreme",
        f"{high_extreme_count:,}"
    )

with col3:

    st.metric(
        "🔴 Extreme Fires",
        f"{extreme_count:,}"
    )

with col4:

    st.metric(
        "📊 Average FRP",
        f"{avg_frp:.2f}"
    )

with col5:

    st.metric(
        "⚡ Maximum FRP",
        f"{max_frp:.2f}"
    )

st.divider()

# --------------------------------------------------
# FIRE INTENSITY DISTRIBUTION
# --------------------------------------------------

st.subheader("🔥 Fire Intensity Distribution")

intensity_counts = (
    filtered_df["fire_intensity"]
    .value_counts()
    .reindex(
        intensity_options,
        fill_value=0
    )
)

col1, col2 = st.columns(2)

with col1:

    st.bar_chart(
        intensity_counts
    )

with col2:

    intensity_table = (
        intensity_counts
        .reset_index()
    )

    intensity_table.columns = [
        "Fire Intensity",
        "Detections"
    ]

    st.dataframe(
        intensity_table,
        width="stretch",
        hide_index=True
    )

st.divider()

# --------------------------------------------------
# MONTHLY FIRE TREND
# --------------------------------------------------

st.subheader("📈 Monthly Wildfire Detection Trend")

monthly_fires = (
    filtered_df
    .groupby("month")
    .size()
    .reset_index(name="fire_count")
)

monthly_fires = monthly_fires.sort_values(
    "month"
)

st.line_chart(
    monthly_fires.set_index("month")
)

st.divider()

# --------------------------------------------------
# DAILY FIRE ACTIVITY
# --------------------------------------------------

st.subheader("📅 Daily Fire Activity")

daily_fires = (
    filtered_df
    .groupby("acq_date")
    .size()
    .reset_index(name="fire_count")
)

daily_fires = daily_fires.sort_values(
    "acq_date"
)

st.line_chart(
    daily_fires.set_index("acq_date")
)

st.divider()

# --------------------------------------------------
# GEOGRAPHIC HOTSPOTS
# --------------------------------------------------

st.subheader("🗺️ Wildfire Geographic Hotspots")

fig, ax = plt.subplots(
    figsize=(12, 5)
)

ax.scatter(
    filtered_df["longitude"],
    filtered_df["latitude"],
    s=5,
    alpha=0.4
)

ax.set_title(
    "Global Wildfire Detection Hotspots - 2025"
)

ax.set_xlabel("Longitude")

ax.set_ylabel("Latitude")

st.pyplot(fig)

st.divider()

# --------------------------------------------------
# TOP FIRE EVENTS
# --------------------------------------------------

st.subheader(
    "🚨 Top 10 Strongest Fire Events"
)

top_fires = (
    filtered_df[
        [
            "acq_date",
            "latitude",
            "longitude",
            "brightness",
            "frp",
            "fire_intensity"
        ]
    ]
    .sort_values(
        "frp",
        ascending=False
    )
    .head(10)
)

st.dataframe(
    top_fires,
    width="stretch",
    hide_index=True
)

st.divider()

# --------------------------------------------------
# RESPONSE PRIORITY
# --------------------------------------------------

st.subheader(
    "🚨 Emergency Response Priority"
)

priority_df = (
    filtered_df[
        filtered_df["fire_intensity"].isin(
            ["High", "Extreme"]
        )
    ]
    [
        [
            "acq_date",
            "latitude",
            "longitude",
            "frp",
            "fire_intensity"
        ]
    ]
    .sort_values(
        "frp",
        ascending=False
    )
    .head(20)
)

st.dataframe(
    priority_df,
    width="stretch",
    hide_index=True
)

st.divider()

# --------------------------------------------------
# EXECUTIVE INSIGHTS
# --------------------------------------------------

st.subheader("💡 Executive Insights")

severe_percentage = (
    high_extreme_count
    / total_fires
    * 100
)

extreme_percentage = (
    extreme_count
    / total_fires
    * 100
)

col1, col2 = st.columns(2)

with col1:

    st.info(
        f"""
        **Total detections:** {total_fires:,}

        **High / Extreme fires:** {severe_percentage:.1f}%

        **Extreme fires:** {extreme_percentage:.1f}%
        """
    )

with col2:

    st.warning(
        f"""
        **Average FRP:** {avg_frp:.2f}

        **Maximum FRP:** {max_frp:.2f}

        Emergency teams should prioritize
        locations with high FRP and Extreme intensity.
        """
    )

st.divider()

st.caption(
    "Wildfire Emergency Response Analytics | "
    "NASA FIRMS • Python • Pandas • Matplotlib • Streamlit"
)