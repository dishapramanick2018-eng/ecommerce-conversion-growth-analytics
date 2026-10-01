
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="E-commerce Conversion Diagnostic",
    page_icon="🛍️",
    layout="wide"
)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("streamlit_session_data.csv")
    df["session_start"] = pd.to_datetime(df["session_start"])
    return df


df = load_data()


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("E-commerce Conversion & Growth Diagnostic")

st.caption(
    "Interactive product and funnel analytics case study | "
    "Session-level conversion analysis"
)

st.markdown(
    """
    This application investigates how customers progress from
    **Product View → Add to Cart → Checkout → Purchase**.

    Use the filters to identify where conversion changes,
    which customer segments are affected, and where deeper
    investigation may be required.
    """
)


# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------

st.sidebar.header("Analysis Filters")

min_date = df["session_start"].min().date()
max_date = df["session_start"].max().date()

date_range = st.sidebar.date_input(
    "Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

selected_devices = st.sidebar.multiselect(
    "Device",
    sorted(df["device"].dropna().unique()),
    default=sorted(df["device"].dropna().unique())
)

selected_channels = st.sidebar.multiselect(
    "Acquisition Channel",
    sorted(df["acquisition_channel"].dropna().unique()),
    default=sorted(df["acquisition_channel"].dropna().unique())
)

selected_categories = st.sidebar.multiselect(
    "Category",
    sorted(df["category"].dropna().unique()),
    default=sorted(df["category"].dropna().unique())
)

selected_customer_types = st.sidebar.multiselect(
    "Customer Type",
    sorted(df["customer_type"].dropna().unique()),
    default=sorted(df["customer_type"].dropna().unique())
)


# --------------------------------------------------
# APPLY FILTERS
# --------------------------------------------------

filtered_df = df.copy()

if len(date_range) == 2:

    start_date = pd.Timestamp(date_range[0])
    end_date = pd.Timestamp(date_range[1]) + pd.Timedelta(days=1)

    filtered_df = filtered_df[
        (filtered_df["session_start"] >= start_date)
        & (filtered_df["session_start"] < end_date)
    ]


filtered_df = filtered_df[
    filtered_df["device"].isin(selected_devices)
    & filtered_df["acquisition_channel"].isin(selected_channels)
    & filtered_df["category"].isin(selected_categories)
    & filtered_df["customer_type"].isin(selected_customer_types)
]


if filtered_df.empty:
    st.warning(
        "No sessions match the selected filters. "
        "Adjust the filters to continue the analysis."
    )
    st.stop()


# --------------------------------------------------
# KPI CALCULATIONS
# --------------------------------------------------

total_sessions = filtered_df["session_id"].nunique()
cart_sessions = filtered_df["add_to_cart"].sum()
checkout_sessions = filtered_df["checkout"].sum()
purchase_sessions = filtered_df["purchase"].sum()

conversion_rate = (
    purchase_sessions / total_sessions * 100
    if total_sessions else 0
)

cart_rate = (
    cart_sessions / total_sessions * 100
    if total_sessions else 0
)

cart_to_checkout = (
    checkout_sessions / cart_sessions * 100
    if cart_sessions else 0
)

checkout_to_purchase = (
    purchase_sessions / checkout_sessions * 100
    if checkout_sessions else 0
)

cart_abandonment = (
    (1 - purchase_sessions / cart_sessions) * 100
    if cart_sessions else 0
)


# --------------------------------------------------
# EXECUTIVE OVERVIEW
# --------------------------------------------------

st.divider()

st.subheader("Executive Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Sessions",
    f"{total_sessions:,}"
)

col2.metric(
    "Purchase Sessions",
    f"{purchase_sessions:,}"
)

col3.metric(
    "Conversion Rate",
    f"{conversion_rate:.2f}%"
)

col4.metric(
    "Cart Abandonment",
    f"{cart_abandonment:.2f}%"
)


# --------------------------------------------------
# FUNNEL
# --------------------------------------------------

st.divider()

st.subheader("Conversion Funnel")

funnel = pd.DataFrame({
    "Stage": [
        "Product View",
        "Add to Cart",
        "Checkout",
        "Purchase"
    ],
    "Sessions": [
        total_sessions,
        cart_sessions,
        checkout_sessions,
        purchase_sessions
    ]
})

funnel["% of Sessions"] = (
    funnel["Sessions"] / total_sessions * 100
).round(2)

fig_funnel = px.bar(
    funnel,
    x="Stage",
    y="Sessions",
    text="Sessions",
    title="Customer Journey Funnel"
)

fig_funnel.update_layout(
    xaxis_title="Funnel Stage",
    yaxis_title="Unique Sessions"
)

st.plotly_chart(
    fig_funnel,
    use_container_width=True
)


stage_metrics = pd.DataFrame({
    "Transition": [
        "View → Cart",
        "Cart → Checkout",
        "Checkout → Purchase"
    ],
    "Conversion Rate (%)": [
        cart_rate,
        cart_to_checkout,
        checkout_to_purchase
    ]
}).round(2)

st.dataframe(
    stage_metrics,
    use_container_width=True,
    hide_index=True
)


# --------------------------------------------------
# TREND ANALYSIS
# --------------------------------------------------

st.divider()

st.subheader("Conversion Trend")

trend_df = filtered_df.copy()

trend_df["week_start"] = (
    trend_df["session_start"]
    .dt.to_period("W")
    .apply(lambda x: x.start_time)
)

weekly = (
    trend_df
    .groupby("week_start", as_index=False)
    .agg(
        sessions=("session_id", "nunique"),
        purchases=("purchase", "sum")
    )
)

weekly["conversion_rate"] = (
    weekly["purchases"]
    / weekly["sessions"] * 100
)

fig_trend = px.line(
    weekly,
    x="week_start",
    y="conversion_rate",
    markers=True,
    title="Weekly Purchase Conversion Rate"
)

fig_trend.update_layout(
    xaxis_title="Week",
    yaxis_title="Conversion Rate (%)"
)

st.plotly_chart(
    fig_trend,
    use_container_width=True
)


# --------------------------------------------------
# SEGMENT DIAGNOSTICS
# --------------------------------------------------

st.divider()

st.subheader("Segment Diagnostics")

st.markdown(
    """
    Overall conversion can hide concentrated performance problems.
    Compare conversion across key business dimensions below.
    """
)


def segment_performance(data, dimension):

    result = (
        data
        .groupby(dimension, as_index=False)
        .agg(
            sessions=("session_id", "nunique"),
            purchases=("purchase", "sum")
        )
    )

    result["conversion_rate"] = (
        result["purchases"]
        / result["sessions"] * 100
    )

    return result.sort_values(
        "conversion_rate",
        ascending=False
    )


tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Device",
        "Acquisition Channel",
        "Category",
        "Customer Type"
    ]
)


with tab1:

    device_perf = segment_performance(
        filtered_df,
        "device"
    )

    fig = px.bar(
        device_perf,
        x="device",
        y="conversion_rate",
        text_auto=".2f",
        title="Conversion by Device"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(
        device_perf.round(2),
        use_container_width=True,
        hide_index=True
    )


with tab2:

    channel_perf = segment_performance(
        filtered_df,
        "acquisition_channel"
    )

    fig = px.bar(
        channel_perf,
        x="acquisition_channel",
        y="conversion_rate",
        text_auto=".2f",
        title="Conversion by Acquisition Channel"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(
        channel_perf.round(2),
        use_container_width=True,
        hide_index=True
    )


with tab3:

    category_perf = segment_performance(
        filtered_df,
        "category"
    )

    fig = px.bar(
        category_perf,
        x="category",
        y="conversion_rate",
        text_auto=".2f",
        title="Conversion by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(
        category_perf.round(2),
        use_container_width=True,
        hide_index=True
    )


with tab4:

    customer_perf = segment_performance(
        filtered_df,
        "customer_type"
    )

    fig = px.bar(
        customer_perf,
        x="customer_type",
        y="conversion_rate",
        text_auto=".2f",
        title="Conversion by Customer Type"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(
        customer_perf.round(2),
        use_container_width=True,
        hide_index=True
    )


# --------------------------------------------------
# ROOT CAUSE DIAGNOSTIC
# --------------------------------------------------

st.divider()

st.subheader("Root-Cause Diagnostic")

st.markdown(
    """
    This section compares segment performance before and after
    **15 May 2026** to identify which device-channel journey
    experienced the largest deterioration relative to its own baseline.
    """
)

diagnostic_df = filtered_df.copy()

diagnostic_df["analysis_period"] = np.where(
    diagnostic_df["session_start"]
    < pd.Timestamp("2026-05-15"),
    "Baseline",
    "Diagnostic"
)

interaction = (
    diagnostic_df[
        diagnostic_df["acquisition_channel"] != "Unknown"
    ]
    .groupby(
        [
            "device",
            "acquisition_channel",
            "analysis_period"
        ],
        as_index=False
    )
    .agg(
        sessions=("session_id", "nunique"),
        purchases=("purchase", "sum")
    )
)

interaction["conversion_rate"] = (
    interaction["purchases"]
    / interaction["sessions"] * 100
)

interaction_pivot = (
    interaction
    .pivot_table(
        index=[
            "device",
            "acquisition_channel"
        ],
        columns="analysis_period",
        values="conversion_rate"
    )
    .reset_index()
)


if (
    "Baseline" in interaction_pivot.columns
    and "Diagnostic" in interaction_pivot.columns
):

    interaction_pivot = interaction_pivot.dropna(
        subset=["Baseline", "Diagnostic"]
    )

    interaction_pivot["Change (pp)"] = (
        interaction_pivot["Diagnostic"]
        - interaction_pivot["Baseline"]
    )

    interaction_pivot = interaction_pivot.sort_values(
        "Change (pp)"
    )

    st.dataframe(
        interaction_pivot.round(2),
        use_container_width=True,
        hide_index=True
    )

    if not interaction_pivot.empty:

        worst = interaction_pivot.iloc[0]

        affected_device = worst["device"]
        affected_channel = worst["acquisition_channel"]

        st.error(
            f"Largest deterioration: "
            f"{affected_device} × {affected_channel} | "
            f"{worst['Baseline']:.2f}% → "
            f"{worst['Diagnostic']:.2f}% "
            f"({worst['Change (pp)']:.2f} pp)"
        )


        # ------------------------------------------
        # FUNNEL DIAGNOSIS OF WORST SEGMENT
        # ------------------------------------------

        affected = diagnostic_df[
            (diagnostic_df["device"] == affected_device)
            & (
                diagnostic_df["acquisition_channel"]
                == affected_channel
            )
        ]

        affected_funnel = (
            affected
            .groupby(
                "analysis_period",
                as_index=False
            )
            .agg(
                sessions=("session_id", "nunique"),
                carts=("add_to_cart", "sum"),
                checkouts=("checkout", "sum"),
                purchases=("purchase", "sum")
            )
        )

        affected_funnel["View → Cart"] = (
            affected_funnel["carts"]
            / affected_funnel["sessions"] * 100
        )

        affected_funnel["Cart → Checkout"] = (
            affected_funnel["checkouts"]
            / affected_funnel["carts"] * 100
        )

        affected_funnel["Checkout → Purchase"] = (
            affected_funnel["purchases"]
            / affected_funnel["checkouts"] * 100
        )


        funnel_long = affected_funnel.melt(
            id_vars="analysis_period",
            value_vars=[
                "View → Cart",
                "Cart → Checkout",
                "Checkout → Purchase"
            ],
            var_name="Funnel Stage",
            value_name="Conversion Rate"
        )

        fig_rca = px.bar(
            funnel_long,
            x="Funnel Stage",
            y="Conversion Rate",
            color="analysis_period",
            barmode="group",
            title=(
                f"Funnel Diagnosis: "
                f"{affected_device} × {affected_channel}"
            )
        )

        st.plotly_chart(
            fig_rca,
            use_container_width=True
        )


        # ------------------------------------------
        # COMMERCIAL IMPACT
        # ------------------------------------------

        impact = (
            affected
            .groupby("analysis_period")
            .agg(
                sessions=("session_id", "nunique"),
                purchases=("purchase", "sum")
            )
        )

        if (
            "Baseline" in impact.index
            and "Diagnostic" in impact.index
        ):

            baseline_rate = (
                impact.loc["Baseline", "purchases"]
                / impact.loc["Baseline", "sessions"]
            )

            diagnostic_sessions = impact.loc[
                "Diagnostic",
                "sessions"
            ]

            actual_purchases = impact.loc[
                "Diagnostic",
                "purchases"
            ]

            expected_purchases = (
                diagnostic_sessions
                * baseline_rate
            )

            estimated_lost = max(
                expected_purchases
                - actual_purchases,
                0
            )

            st.markdown(
                "### Business Impact Scenario"
            )

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Expected Purchases at Baseline",
                f"{expected_purchases:.0f}"
            )

            c2.metric(
                "Actual Purchases",
                f"{actual_purchases:.0f}"
            )

            c3.metric(
                "Estimated Purchase Gap",
                f"{estimated_lost:.0f}"
            )

            st.caption(
                "Scenario estimate based on maintaining the "
                "segment's historical baseline conversion rate. "
                "This should not be interpreted as a causal forecast."
            )

else:

    st.info(
        "The selected filters do not contain sufficient "
        "baseline and diagnostic-period observations for comparison."
    )


# --------------------------------------------------
# BUSINESS INTERPRETATION
# --------------------------------------------------

st.divider()

st.subheader("How to Use This Analysis")

st.markdown(
    """
    **1. Detect**  
    Identify whether overall conversion is changing.

    **2. Decompose**  
    Determine which funnel stage contributes to the change.

    **3. Segment**  
    Compare devices, channels, categories and customer types.

    **4. Diagnose**  
    Test interaction effects rather than assuming that the
    lowest-converting segment caused the decline.

    **5. Quantify**  
    Estimate the potential commercial significance of the issue.

    **6. Act**  
    Prioritize targeted UX, acquisition, checkout or operational
    investigation based on the evidence.
    """
)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Portfolio case study by Disha Pramanick | "
    "Python • SQL • Excel • Streamlit"
)
