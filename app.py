
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="E-commerce Conversion Intelligence",
    page_icon="↗",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM DESIGN SYSTEM
# ============================================================

st.markdown(
    """
    <style>

    /* -------------------------------------------------------
       GLOBAL
    ------------------------------------------------------- */

    .stApp {
        background: #f7f8fa;
    }

    .block-container {
        max-width: 1380px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    html, body, [class*="css"] {
        font-family: "Inter", "Segoe UI", Arial, sans-serif;
    }

    h1, h2, h3 {
        letter-spacing: -0.03em;
    }

    /* -------------------------------------------------------
       SIDEBAR
    ------------------------------------------------------- */

    [data-testid="stSidebar"] {
        background: #111827;
        border-right: 1px solid #1f2937;
    }

    [data-testid="stSidebar"] * {
        color: #f9fafb;
    }

    [data-testid="stSidebar"] label {
        font-weight: 500;
    }

    /* -------------------------------------------------------
       HERO
    ------------------------------------------------------- */

    .hero {
        background: #111827;
        border-radius: 22px;
        padding: 42px 46px;
        margin-bottom: 24px;
        box-shadow: 0 12px 35px rgba(17, 24, 39, 0.10);
    }

    .hero-eyebrow {
        font-size: 0.76rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        color: #93c5fd;
        margin-bottom: 12px;
    }

    .hero-title {
        font-size: 2.65rem;
        line-height: 1.05;
        font-weight: 750;
        letter-spacing: -0.045em;
        color: #ffffff;
        margin: 0;
    }

    .hero-subtitle {
        max-width: 820px;
        font-size: 1.03rem;
        line-height: 1.7;
        color: #cbd5e1;
        margin-top: 18px;
        margin-bottom: 0;
    }

    .hero-flow {
        display: inline-block;
        margin-top: 24px;
        padding: 9px 14px;
        border: 1px solid #374151;
        border-radius: 999px;
        color: #e5e7eb;
        font-size: 0.82rem;
        letter-spacing: 0.02em;
    }

    /* -------------------------------------------------------
       SECTION LABELS
    ------------------------------------------------------- */

    .section-kicker {
        color: #2563eb;
        font-size: 0.72rem;
        font-weight: 750;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        margin-bottom: 5px;
    }

    .section-title {
        color: #111827;
        font-size: 1.65rem;
        font-weight: 730;
        letter-spacing: -0.035em;
        margin-bottom: 5px;
    }

    .section-copy {
        color: #64748b;
        font-size: 0.94rem;
        line-height: 1.6;
        margin-bottom: 18px;
    }

    /* -------------------------------------------------------
       KPI CARDS
    ------------------------------------------------------- */

    .metric-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 20px 20px 18px 20px;
        min-height: 118px;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.035);
    }

    .metric-label {
        color: #64748b;
        font-size: 0.76rem;
        font-weight: 650;
        letter-spacing: 0.07em;
        text-transform: uppercase;
        margin-bottom: 12px;
    }

    .metric-value {
        color: #111827;
        font-size: 1.85rem;
        line-height: 1;
        font-weight: 760;
        letter-spacing: -0.04em;
    }

    .metric-note {
        color: #94a3b8;
        font-size: 0.74rem;
        margin-top: 10px;
    }

    /* -------------------------------------------------------
       INSIGHT / DIAGNOSTIC CARDS
    ------------------------------------------------------- */

    .insight-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-left: 4px solid #2563eb;
        border-radius: 14px;
        padding: 20px 22px;
        margin: 12px 0 20px 0;
    }

    .diagnostic-card {
        background: #111827;
        border-radius: 18px;
        padding: 25px 28px;
        margin: 16px 0 22px 0;
        color: #ffffff;
    }

    .diagnostic-label {
        color: #93c5fd;
        font-size: 0.72rem;
        font-weight: 750;
        letter-spacing: 0.14em;
        text-transform: uppercase;
    }

    .diagnostic-title {
        color: #ffffff;
        font-size: 1.4rem;
        font-weight: 720;
        margin-top: 8px;
        margin-bottom: 7px;
    }

    .diagnostic-copy {
        color: #cbd5e1;
        font-size: 0.9rem;
        line-height: 1.6;
    }

    /* -------------------------------------------------------
       STREAMLIT COMPONENTS
    ------------------------------------------------------- */

    [data-testid="stDataFrame"] {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        overflow: hidden;
    }

    div[data-testid="stPlotlyChart"] {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 8px;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }

    .stTabs [data-baseweb="tab"] {
        background: #ffffff;
        border-radius: 10px;
        padding: 8px 16px;
        border: 1px solid #e5e7eb;
    }

    hr {
        border: none;
        border-top: 1px solid #e5e7eb;
        margin: 2.2rem 0;
    }

    /* -------------------------------------------------------
       FOOTER
    ------------------------------------------------------- */

    .portfolio-footer {
        text-align: center;
        color: #94a3b8;
        font-size: 0.78rem;
        padding-top: 22px;
    }

    /* -------------------------------------------------------
       MOBILE
    ------------------------------------------------------- */

    @media (max-width: 768px) {

        .block-container {
            padding-top: 1rem;
        }

        .hero {
            padding: 30px 24px;
        }

        .hero-title {
            font-size: 2rem;
        }

        .hero-subtitle {
            font-size: 0.92rem;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DATA
# ============================================================

@st.cache_data
def load_data():

    data = pd.read_csv("streamlit_session_data.csv")

    data["session_start"] = pd.to_datetime(
        data["session_start"]
    )

    return data


df = load_data()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("## Analysis Controls")

st.sidebar.caption(
    "Filter the customer journey and investigate "
    "conversion performance."
)

min_date = df["session_start"].min().date()
max_date = df["session_start"].max().date()

date_range = st.sidebar.date_input(
    "Date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

devices = sorted(
    df["device"].dropna().unique()
)

channels = sorted(
    df["acquisition_channel"].dropna().unique()
)

categories = sorted(
    df["category"].dropna().unique()
)

customer_types = sorted(
    df["customer_type"].dropna().unique()
)

selected_devices = st.sidebar.multiselect(
    "Device",
    devices,
    default=devices
)

selected_channels = st.sidebar.multiselect(
    "Acquisition channel",
    channels,
    default=channels
)

selected_categories = st.sidebar.multiselect(
    "Product category",
    categories,
    default=categories
)

selected_customer_types = st.sidebar.multiselect(
    "Customer type",
    customer_types,
    default=customer_types
)

st.sidebar.divider()

st.sidebar.caption(
    "Diagnostic framework"
)

st.sidebar.markdown(
    "**Monitor → Detect → Diagnose → Quantify → Act**"
)


# ============================================================
# FILTER DATA
# ============================================================

filtered_df = df.copy()

if len(date_range) == 2:

    start_date = pd.Timestamp(date_range[0])

    end_date = (
        pd.Timestamp(date_range[1])
        + pd.Timedelta(days=1)
    )

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
        "No sessions match the current filter selection."
    )

    st.stop()


# ============================================================
# CALCULATIONS
# ============================================================

total_sessions = filtered_df["session_id"].nunique()

cart_sessions = int(
    filtered_df["add_to_cart"].sum()
)

checkout_sessions = int(
    filtered_df["checkout"].sum()
)

purchase_sessions = int(
    filtered_df["purchase"].sum()
)

conversion_rate = (
    purchase_sessions / total_sessions * 100
    if total_sessions
    else 0
)

cart_rate = (
    cart_sessions / total_sessions * 100
    if total_sessions
    else 0
)

cart_to_checkout = (
    checkout_sessions / cart_sessions * 100
    if cart_sessions
    else 0
)

checkout_to_purchase = (
    purchase_sessions / checkout_sessions * 100
    if checkout_sessions
    else 0
)

cart_abandonment = (
    (1 - purchase_sessions / cart_sessions) * 100
    if cart_sessions
    else 0
)


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-eyebrow">
            E-COMMERCE • PRODUCT ANALYTICS
        </div>

        <div class="hero-title">
            Conversion & Growth<br>Diagnostic
        </div>

        <div class="hero-subtitle">
            Explore the customer purchase journey, detect conversion
            deterioration, isolate the segments driving the change,
            and translate analytical signals into business action.
        </div>

        <div class="hero-flow">
            Product View → Cart → Checkout → Purchase
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# EXECUTIVE OVERVIEW
# ============================================================

st.markdown(
    """
    <div class="section-kicker">01 • Monitor</div>
    <div class="section-title">Executive Overview</div>
    <div class="section-copy">
        A high-level view of customer traffic and purchase performance
        for the selected population.
    </div>
    """,
    unsafe_allow_html=True
)


k1, k2, k3, k4 = st.columns(4)

with k1:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Sessions</div>
            <div class="metric-value">{total_sessions:,}</div>
            <div class="metric-note">Unique shopping sessions</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with k2:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Purchases</div>
            <div class="metric-value">{purchase_sessions:,}</div>
            <div class="metric-note">Sessions completing purchase</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with k3:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Conversion</div>
            <div class="metric-value">{conversion_rate:.2f}%</div>
            <div class="metric-note">Purchase sessions ÷ sessions</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with k4:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Cart Abandonment</div>
            <div class="metric-value">{cart_abandonment:.2f}%</div>
            <div class="metric-note">Cart sessions without purchase</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FUNNEL
# ============================================================

st.divider()

st.markdown(
    """
    <div class="section-kicker">02 • Decompose</div>
    <div class="section-title">Purchase Funnel</div>
    <div class="section-copy">
        Identify where customer progression weakens across the
        purchase journey.
    </div>
    """,
    unsafe_allow_html=True
)


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


fig_funnel = px.funnel(
    funnel,
    y="Stage",
    x="Sessions"
)

fig_funnel.update_layout(
    height=430,
    margin=dict(
        l=40,
        r=40,
        t=30,
        b=30
    ),
    paper_bgcolor="white",
    plot_bgcolor="white",
    font=dict(
        family="Inter, Arial",
        color="#334155"
    )
)

st.plotly_chart(
    fig_funnel,
    use_container_width=True
)


s1, s2, s3 = st.columns(3)

s1.metric(
    "View → Cart",
    f"{cart_rate:.2f}%"
)

s2.metric(
    "Cart → Checkout",
    f"{cart_to_checkout:.2f}%"
)

s3.metric(
    "Checkout → Purchase",
    f"{checkout_to_purchase:.2f}%"
)


# ============================================================
# TREND
# ============================================================

st.divider()

st.markdown(
    """
    <div class="section-kicker">03 • Detect</div>
    <div class="section-title">Conversion Trend</div>
    <div class="section-copy">
        Monitor weekly conversion to identify when customer
        purchase behaviour begins to change.
    </div>
    """,
    unsafe_allow_html=True
)


trend_df = filtered_df.copy()

trend_df["week_start"] = (
    trend_df["session_start"]
    .dt.to_period("W")
    .apply(lambda period: period.start_time)
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
    markers=True
)

fig_trend.update_layout(
    height=420,
    xaxis_title=None,
    yaxis_title="Conversion rate (%)",
    margin=dict(
        l=35,
        r=25,
        t=25,
        b=35
    ),
    paper_bgcolor="white",
    plot_bgcolor="white",
    font=dict(
        family="Inter, Arial",
        color="#334155"
    )
)

fig_trend.update_xaxes(
    showgrid=False
)

fig_trend.update_yaxes(
    gridcolor="#eef2f7"
)

st.plotly_chart(
    fig_trend,
    use_container_width=True
)


# ============================================================
# SEGMENT ANALYSIS
# ============================================================

st.divider()

st.markdown(
    """
    <div class="section-kicker">04 • Segment</div>
    <div class="section-title">Performance Diagnostics</div>
    <div class="section-copy">
        Compare customer journeys across major business dimensions.
        A low conversion rate alone does not establish root cause;
        the direction of change relative to historical performance
        matters.
    </div>
    """,
    unsafe_allow_html=True
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


tabs = st.tabs(
    [
        "Device",
        "Acquisition Channel",
        "Category",
        "Customer Type"
    ]
)


dimensions = [
    ("device", "Conversion by Device"),
    (
        "acquisition_channel",
        "Conversion by Acquisition Channel"
    ),
    ("category", "Conversion by Product Category"),
    ("customer_type", "Conversion by Customer Type")
]


for tab, (dimension, title) in zip(
    tabs,
    dimensions
):

    with tab:

        performance = segment_performance(
            filtered_df,
            dimension
        )

        fig = px.bar(
            performance,
            x=dimension,
            y="conversion_rate",
            text_auto=".2f"
        )

        fig.update_layout(
            height=390,
            xaxis_title=None,
            yaxis_title="Conversion rate (%)",
            margin=dict(
                l=35,
                r=25,
                t=25,
                b=35
            ),
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(
                family="Inter, Arial",
                color="#334155"
            )
        )

        fig.update_yaxes(
            gridcolor="#eef2f7"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.dataframe(
            performance.round(2),
            use_container_width=True,
            hide_index=True
        )


# ============================================================
# ROOT CAUSE ANALYSIS
# ============================================================

st.divider()

st.markdown(
    """
    <div class="section-kicker">05 • Diagnose</div>
    <div class="section-title">Root-Cause Diagnostic</div>
    <div class="section-copy">
        Compare each device-channel journey against its own
        historical baseline rather than assuming that the
        lowest-converting segment caused the decline.
    </div>
    """,
    unsafe_allow_html=True
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
        diagnostic_df["acquisition_channel"]
        != "Unknown"
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

    interaction_pivot = (
        interaction_pivot
        .dropna(
            subset=[
                "Baseline",
                "Diagnostic"
            ]
        )
    )

    interaction_pivot["Change (pp)"] = (
        interaction_pivot["Diagnostic"]
        - interaction_pivot["Baseline"]
    )

    interaction_pivot = (
        interaction_pivot
        .sort_values("Change (pp)")
    )


    if not interaction_pivot.empty:

        worst = interaction_pivot.iloc[0]

        affected_device = worst["device"]

        affected_channel = worst[
            "acquisition_channel"
        ]


        st.markdown(
            f"""
            <div class="diagnostic-card">

                <div class="diagnostic-label">
                    Diagnostic Spotlight
                </div>

                <div class="diagnostic-title">
                    {affected_device} × {affected_channel}
                </div>

                <div class="diagnostic-copy">
                    This journey shows the largest deterioration
                    relative to its own baseline:
                    <strong>{worst['Baseline']:.2f}%</strong>
                    → <strong>{worst['Diagnostic']:.2f}%</strong>,
                    a change of
                    <strong>{worst['Change (pp)']:.2f}
                    percentage points</strong>.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


        with st.expander(
            "View device × channel comparison",
            expanded=False
        ):

            st.dataframe(
                interaction_pivot.round(2),
                use_container_width=True,
                hide_index=True
            )


        # ----------------------------------------------------
        # AFFECTED FUNNEL
        # ----------------------------------------------------

        affected = diagnostic_df[
            (
                diagnostic_df["device"]
                == affected_device
            )
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
            barmode="group"
        )


        fig_rca.update_layout(
            height=430,
            xaxis_title=None,
            yaxis_title="Conversion rate (%)",
            legend_title=None,
            margin=dict(
                l=35,
                r=25,
                t=25,
                b=35
            ),
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(
                family="Inter, Arial",
                color="#334155"
            )
        )


        fig_rca.update_yaxes(
            gridcolor="#eef2f7"
        )


        st.plotly_chart(
            fig_rca,
            use_container_width=True
        )


        # ----------------------------------------------------
        # PRIMARY FRICTION
        # ----------------------------------------------------

        funnel_compare = (
            affected_funnel
            .set_index("analysis_period")
            [
                [
                    "View → Cart",
                    "Cart → Checkout",
                    "Checkout → Purchase"
                ]
            ]
            .T
        )


        if (
            "Baseline" in funnel_compare.columns
            and "Diagnostic" in funnel_compare.columns
        ):

            funnel_compare["Change (pp)"] = (
                funnel_compare["Diagnostic"]
                - funnel_compare["Baseline"]
            )

            funnel_compare = (
                funnel_compare
                .sort_values("Change (pp)")
            )

            primary_friction = (
                funnel_compare.index[0]
            )

            primary_change = (
                funnel_compare.iloc[0][
                    "Change (pp)"
                ]
            )


            st.markdown(
                f"""
                <div class="insight-card">
                    <strong>Primary funnel friction:</strong>
                    {primary_friction}<br>
                    <span style="color:#64748b;">
                    This transition experienced the largest
                    deterioration within the affected journey
                    ({primary_change:.2f} pp).
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )


        # ----------------------------------------------------
        # COMMERCIAL IMPACT
        # ----------------------------------------------------

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
                impact.loc[
                    "Baseline",
                    "purchases"
                ]
                / impact.loc[
                    "Baseline",
                    "sessions"
                ]
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
                """
                <div class="section-kicker">
                    06 • Quantify
                </div>
                <div class="section-title">
                    Commercial Impact Scenario
                </div>
                <div class="section-copy">
                    Estimate the purchase opportunity associated
                    with maintaining historical baseline
                    performance.
                </div>
                """,
                unsafe_allow_html=True
            )


            i1, i2, i3 = st.columns(3)


            with i1:

                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-label">
                            Expected Purchases
                        </div>
                        <div class="metric-value">
                            {expected_purchases:.0f}
                        </div>
                        <div class="metric-note">
                            At baseline conversion
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            with i2:

                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-label">
                            Actual Purchases
                        </div>
                        <div class="metric-value">
                            {actual_purchases:.0f}
                        </div>
                        <div class="metric-note">
                            Diagnostic period
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            with i3:

                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-label">
                            Purchase Gap
                        </div>
                        <div class="metric-value">
                            {estimated_lost:.0f}
                        </div>
                        <div class="metric-note">
                            Scenario-based estimate
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            st.caption(
                "Scenario estimate based on maintaining the "
                "segment's historical baseline conversion rate. "
                "This is not a causal forecast."
            )


else:

    st.info(
        "The selected filters do not contain sufficient "
        "baseline and diagnostic-period observations."
    )


# ============================================================
# ACTION FRAMEWORK
# ============================================================

st.divider()

st.markdown(
    """
    <div class="section-kicker">07 • Act</div>
    <div class="section-title">Decision Framework</div>
    <div class="section-copy">
        Translate the diagnostic signal into targeted business
        investigation rather than treating the entire funnel as
        equally problematic.
    </div>
    """,
    unsafe_allow_html=True
)


a1, a2, a3 = st.columns(3)


with a1:

    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-label">Investigate</div>
            <div style="font-weight:650;color:#111827;">
                Journey Experience
            </div>
            <div class="metric-note">
                Landing relevance, mobile UX, page performance
                and campaign alignment.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with a2:

    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-label">Validate</div>
            <div style="font-weight:650;color:#111827;">
                Funnel Friction
            </div>
            <div class="metric-note">
                Cart progression, checkout errors, payment
                failures and completion behaviour.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with a3:

    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-label">Monitor</div>
            <div style="font-weight:650;color:#111827;">
                Segment Health
            </div>
            <div class="metric-note">
                Device × channel conversion and material
                week-over-week deterioration.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# METHODOLOGY
# ============================================================

with st.expander(
    "Methodology & metric definitions"
):

    st.markdown(
        """
        **Analytical grain:** Unique shopping session

        **Purchase Conversion Rate**  
        Purchase sessions ÷ total sessions

        **Cart Rate**  
        Add-to-cart sessions ÷ total sessions

        **Cart → Checkout Rate**  
        Checkout sessions ÷ cart sessions

        **Checkout → Purchase Rate**  
        Purchase sessions ÷ checkout sessions

        **Cart Abandonment Rate**  
        Cart sessions without purchase ÷ cart sessions

        **Root-cause comparison**  
        Segment diagnostic-period conversion is compared with
        the same segment's historical baseline.

        **Commercial impact**  
        Scenario estimate based on maintaining historical
        baseline conversion. It is not interpreted as a causal
        forecast.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="portfolio-footer">
        Disha Pramanick · Analytics Portfolio<br>
        Python · SQL · Excel · Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
