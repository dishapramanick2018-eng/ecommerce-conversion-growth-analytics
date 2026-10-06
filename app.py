
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="The Conversion Mystery | E-commerce Analytics",
    page_icon="🕵️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# DESIGN SYSTEM
# ============================================================

st.markdown("""
<style>

/* ==================== GLOBAL ==================== */

.stApp {
    background: #F7F9FC;
}

.block-container {
    max-width: 1380px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

html, body, [class*="css"] {
    font-family: Inter, "Segoe UI", Arial, sans-serif;
    color: #172033;
}

h1, h2, h3 {
    letter-spacing: -0.035em;
}


/* ==================== SIDEBAR ==================== */

[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #1F2937;
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 1.5rem;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {
    color: #F8FAFC !important;
}

[data-testid="stSidebar"] .stCaptionContainer p {
    color: #94A3B8 !important;
}


/* Sidebar input containers */

[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background: #FFFFFF !important;
    border: 1px solid #334155 !important;
    border-radius: 10px !important;
}

[data-testid="stSidebar"] input {
    color: #172033 !important;
}


/* Selected multiselect pills */

[data-testid="stSidebar"] [data-baseweb="tag"] {
    background-color: #DBEAFE !important;
    border: 1px solid #BFDBFE !important;
    border-radius: 7px !important;
}

[data-testid="stSidebar"] [data-baseweb="tag"] span,
[data-testid="stSidebar"] [data-baseweb="tag"] div {
    color: #1E40AF !important;
}

[data-testid="stSidebar"] [data-baseweb="tag"] svg {
    fill: #1E40AF !important;
    color: #1E40AF !important;
}


/* ==================== HERO ==================== */

.hero {
    background:
        radial-gradient(
            circle at 88% 10%,
            rgba(59,130,246,0.24),
            transparent 31%
        ),
        linear-gradient(
            135deg,
            #0F172A 0%,
            #111827 55%,
            #172554 100%
        );

    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 24px;
    padding: 48px 50px;
    margin-bottom: 34px;

    box-shadow:
        0 20px 50px rgba(15,23,42,0.11);
}

.hero-eyebrow {
    color: #93C5FD;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.17em;
    margin-bottom: 14px;
}

.hero-title {
    color: #FFFFFF;
    font-size: 3rem;
    line-height: 1.02;
    font-weight: 780;
    letter-spacing: -0.05em;
    margin-bottom: 18px;
}

.hero-subtitle {
    color: #CBD5E1;
    font-size: 1rem;
    line-height: 1.75;
    max-width: 790px;
}

.hero-flow {
    display: inline-block;
    color: #E2E8F0;
    border: 1px solid #475569;
    background: rgba(255,255,255,0.045);
    border-radius: 999px;
    padding: 9px 15px;
    margin-top: 23px;
    font-size: 0.82rem;
}


/* ==================== SECTION HEADINGS ==================== */

.section-kicker {
    color: #2563EB;
    font-size: 0.69rem;
    font-weight: 800;
    letter-spacing: 0.17em;
    text-transform: uppercase;
    margin-bottom: 7px;
}

.section-title {
    color: #172033;
    font-size: 1.65rem;
    font-weight: 760;
    letter-spacing: -0.04em;
    margin-bottom: 6px;
}

.section-copy {
    color: #64748B;
    font-size: 0.91rem;
    line-height: 1.65;
    max-width: 960px;
    margin-bottom: 21px;
}


/* ==================== KPI CARDS ==================== */

.metric-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 17px;
    padding: 21px 21px 19px;
    min-height: 126px;

    box-shadow:
        0 5px 18px rgba(15,23,42,0.035);
}

.metric-label {
    color: #64748B;
    font-size: 0.68rem;
    font-weight: 800;
    letter-spacing: 0.11em;
    text-transform: uppercase;
    margin-bottom: 13px;
}

.metric-value {
    color: #0F172A;
    font-size: 1.9rem;
    line-height: 1;
    font-weight: 780;
    letter-spacing: -0.045em;
}

.metric-note {
    color: #94A3B8;
    font-size: 0.73rem;
    line-height: 1.45;
    margin-top: 11px;
}


/* ==================== FUNNEL METRICS ==================== */

.stage-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 15px;
    padding: 18px 20px;

    box-shadow:
        0 4px 14px rgba(15,23,42,0.025);
}

.stage-label {
    color: #64748B;
    font-size: 0.72rem;
    font-weight: 700;
    margin-bottom: 7px;
}

.stage-value {
    color: #0F172A;
    font-size: 1.65rem;
    font-weight: 760;
    letter-spacing: -0.04em;
}

.stage-note {
    color: #94A3B8;
    font-size: 0.69rem;
    margin-top: 6px;
}


/* ==================== RCA ==================== */

.rca-shell {
    background:
        linear-gradient(
            135deg,
            #0F172A 0%,
            #172554 100%
        );

    border-radius: 19px;
    padding: 28px 30px;
    margin: 12px 0 23px;

    box-shadow:
        0 12px 30px rgba(15,23,42,0.10);
}

.rca-eyebrow {
    color: #93C5FD;
    font-size: 0.69rem;
    font-weight: 800;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin-bottom: 9px;
}

.rca-segment {
    color: #FFFFFF;
    font-size: 1.55rem;
    font-weight: 760;
    letter-spacing: -0.035em;
    margin-bottom: 10px;
}

.rca-description {
    color: #CBD5E1;
    font-size: 0.91rem;
    line-height: 1.7;
}

.rca-number {
    color: #FFFFFF;
    font-weight: 750;
}


/* ==================== INSIGHT ==================== */

.insight-card {
    background: #EFF6FF;
    border: 1px solid #DBEAFE;
    border-left: 4px solid #2563EB;
    border-radius: 14px;
    padding: 18px 21px;
    margin: 14px 0 24px;
}

.insight-title {
    color: #172033;
    font-size: 0.92rem;
    font-weight: 750;
}

.insight-copy {
    color: #64748B;
    font-size: 0.80rem;
    line-height: 1.6;
    margin-top: 5px;
}


/* ==================== ACTION CARDS ==================== */

.action-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 20px;
    min-height: 145px;

    box-shadow:
        0 4px 14px rgba(15,23,42,0.025);
}

.action-number {
    color: #2563EB;
    font-size: 0.67rem;
    font-weight: 800;
    letter-spacing: 0.12em;
}

.action-title {
    color: #172033;
    font-size: 0.98rem;
    font-weight: 740;
    margin-top: 10px;
}

.action-copy {
    color: #64748B;
    font-size: 0.77rem;
    line-height: 1.6;
    margin-top: 8px;
}


/* ==================== BUSINESS CASE ==================== */

.business-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin: 8px 0 28px;
}

.business-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 15px;
    padding: 18px 18px 17px;
    min-height: 126px;
}

.business-label {
    color: #2563EB;
    font-size: 0.66rem;
    font-weight: 800;
    letter-spacing: 0.10em;
    text-transform: uppercase;
    margin-bottom: 9px;
}

.business-question {
    color: #172033;
    font-size: 0.91rem;
    font-weight: 720;
    line-height: 1.45;
}

.owner {
    display: inline-block;
    margin-top: 10px;
    color: #2563EB;
    background: #EFF6FF;
    border-radius: 999px;
    padding: 4px 8px;
    font-size: 0.66rem;
    font-weight: 750;
}

@media (max-width: 900px) {
    .business-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 600px) {
    .business-grid { grid-template-columns: 1fr; }
}

/* ==================== STREAMLIT ==================== */

div[data-testid="stPlotlyChart"] {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 17px;
    padding: 7px;

    box-shadow:
        0 4px 16px rgba(15,23,42,0.025);
}

[data-testid="stDataFrame"] {
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    overflow: hidden;
}


/* Tabs */

.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    border-bottom: 1px solid #E2E8F0;
}

.stTabs [data-baseweb="tab"] {
    height: 42px;
    padding: 0 13px;
    color: #475569;
}

.stTabs [aria-selected="true"] {
    color: #2563EB !important;
    font-weight: 650;
}


/* Expanders */

[data-testid="stExpander"] {
    border: 1px solid #E2E8F0 !important;
    border-radius: 11px !important;
    background: #FFFFFF;
}


/* Dividers */

hr {
    border: none;
    border-top: 1px solid #E2E8F0;
    margin: 2.6rem 0;
}


/* ==================== FOOTER ==================== */

.portfolio-footer {
    text-align: center;
    color: #94A3B8;
    font-size: 0.75rem;
    line-height: 1.7;
    padding: 20px 0 5px;
}


/* ==================== RESPONSIVE ==================== */

@media (max-width: 768px) {

    .block-container {
        padding-top: 1rem;
    }

    .hero {
        padding: 31px 25px;
        border-radius: 18px;
    }

    .hero-title {
        font-size: 2.15rem;
    }

    .hero-subtitle {
        font-size: 0.90rem;
    }

    .metric-card,
    .stage-card,
    .action-card {
        margin-bottom: 8px;
    }
}

/* ==================== PLAYABLE CASE V2 ==================== */
.case-nav{display:flex;flex-wrap:wrap;gap:8px;margin:-10px 0 24px}
.case-pill{display:inline-block;padding:8px 12px;border:1px solid #DCE5F0;border-radius:999px;background:#FFF;color:#475569;font-size:.70rem;font-weight:800;text-decoration:none!important}
.case-pill:hover{border-color:#2563EB;color:#2563EB;transform:translateY(-1px)}
.case-pill.active{background:#172554;color:#FFF;border-color:#172554}
.mission-card{background:linear-gradient(135deg,#FFF 0%,#F8FAFF 100%);border:1px solid #DCE5F0;border-left:4px solid #2563EB;border-radius:17px;padding:21px 23px;margin:4px 0 25px}
.mission-label,.answer-kicker{color:#2563EB;font-size:.68rem;font-weight:850;letter-spacing:.14em}
.mission-title{color:#172033;font-size:1.18rem;font-weight:780;margin-top:7px}
.mission-copy,.answer-copy{color:#64748B;font-size:.84rem;line-height:1.65;margin-top:6px}
.answer-card{background:#F8FAFC;border:1px solid #DCE5F0;border-radius:15px;padding:18px 20px;margin:8px 0 16px}
.answer-title{color:#172033;font-size:1.02rem;font-weight:780;margin-top:6px}
.answer-number{color:#0F172A;font-weight:800}
.case-closed{background:#ECFDF5;border:1px solid #A7F3D0;border-radius:17px;padding:22px 24px;margin:8px 0 24px}
.case-closed-label{color:#047857;font-size:.68rem;font-weight:850;letter-spacing:.14em}
.case-closed-title{color:#064E3B;font-size:1.20rem;font-weight:780;margin-top:6px}
.case-closed-copy{color:#475569;font-size:.83rem;line-height:1.6;margin-top:6px}
div[data-testid="stExpander"] details summary{font-weight:760}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    data = pd.read_csv(
        "streamlit_session_data.csv"
    )

    data["session_start"] = pd.to_datetime(
        data["session_start"]
    )

    return data


df = load_data()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    "## Investigation Controls"
)

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
    df["device"]
    .dropna()
    .unique()
)

channels = sorted(
    df["acquisition_channel"]
    .dropna()
    .unique()
)

categories = sorted(
    df["category"]
    .dropna()
    .unique()
)

customer_types = sorted(
    df["customer_type"]
    .dropna()
    .unique()
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

compare_mode = st.sidebar.selectbox(
    "Compare against",
    ["Historical baseline", "Previous period"],
    help=(
        "Historical baseline uses the case-study split date. "
        "Previous period compares the selected date window with the immediately preceding window of equal length."
    )
)


st.sidebar.divider()

st.sidebar.caption(
    "DIAGNOSTIC FRAMEWORK"
)

st.sidebar.markdown(
    "**Monitor → Decompose → Detect → Segment → Diagnose → Quantify → Act**"
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


if len(date_range) == 2:

    start_date = pd.Timestamp(
        date_range[0]
    )

    end_date = (
        pd.Timestamp(date_range[1])
        + pd.Timedelta(days=1)
    )

    filtered_df = filtered_df[
        (
            filtered_df["session_start"]
            >= start_date
        )
        &
        (
            filtered_df["session_start"]
            < end_date
        )
    ]


filtered_df = filtered_df[
    filtered_df["device"].isin(
        selected_devices
    )
    &
    filtered_df["acquisition_channel"].isin(
        selected_channels
    )
    &
    filtered_df["category"].isin(
        selected_categories
    )
    &
    filtered_df["customer_type"].isin(
        selected_customer_types
    )
]


if filtered_df.empty:

    st.warning(
        "No sessions match the current filter selection. "
        "Adjust the filters to continue."
    )

    st.stop()


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_sessions = (
    filtered_df["session_id"]
    .nunique()
)

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
    purchase_sessions
    / total_sessions
    * 100
    if total_sessions
    else 0
)


cart_rate = (
    cart_sessions
    / total_sessions
    * 100
    if total_sessions
    else 0
)


cart_to_checkout = (
    checkout_sessions
    / cart_sessions
    * 100
    if cart_sessions
    else 0
)


checkout_to_purchase = (
    purchase_sessions
    / checkout_sessions
    * 100
    if checkout_sessions
    else 0
)


cart_abandonment = (
    (
        1
        - purchase_sessions
        / cart_sessions
    )
    * 100
    if cart_sessions
    else 0
)


# ============================================================
# HERO
# ============================================================

hero_html = (
    '<div class="hero" id="case-brief">'
    '<div class="hero-eyebrow">INTERACTIVE ANALYTICS CASE • YOUR MISSION</div>'
    '<div class="hero-title">The Conversion Mystery</div>'
    '<div class="hero-subtitle"><b>30,000 customer sessions. One hidden performance problem.</b><br>'
    'Follow the evidence, form a hypothesis, identify the affected journey, locate the funnel friction, '
    'and quantify the business impact.</div>'
    '<div class="hero-flow">START CASE → FOLLOW CLUES → MAKE A CALL → UNLOCK DIAGNOSIS</div>'
    '</div>'
)

st.markdown(
    hero_html,
    unsafe_allow_html=True
)

st.markdown(
    '''
<div class="case-nav">
<a class="case-pill active" href="#case-brief">CASE BRIEF</a>
<a class="case-pill" href="#signal">01 · SIGNAL</a>
<a class="case-pill" href="#funnel">02 · FUNNEL</a>
<a class="case-pill" href="#timing">03 · TIMING</a>
<a class="case-pill" href="#segments">04 · SEGMENTS</a>
<a class="case-pill" href="#diagnosis">05 · DIAGNOSIS</a>
<a class="case-pill" href="#impact">06 · IMPACT</a>
<a class="case-pill" href="#action">07 · ACTION</a>
</div>
<div class="mission-card">
<div class="mission-label">CASE BRIEF</div>
<div class="mission-title">Can you find what is hurting conversion?</div>
<div class="mission-copy">Follow the evidence in sequence. Compare each journey with its own baseline, make a hypothesis, then unlock the diagnosis.</div>
</div>
''',
    unsafe_allow_html=True
)

st.markdown(
    '''
<div class="section-kicker">MISSION OBJECTIVES</div>
<div class="section-title">Four questions. One case to solve.</div>
<div class="section-copy">Click a question to reveal the analytical clue, then use the evidence below to test it yourself.</div>
''',
    unsafe_allow_html=True
)

with st.expander("01 · WHAT CHANGED?  →  When did conversion performance begin to deteriorate?"):
    st.markdown('''
**How to solve it:** Track purchase conversion over time rather than relying on the overall average.

**Formula:** `Purchase Conversion Rate = Purchase Sessions ÷ Total Sessions × 100`

Go to **Clue 03 — Timing**. Its month-by-month explanation changes with the filters.
''')

with st.expander("02 · WHERE?  →  Which stage of the purchase funnel weakened most?"):
    st.markdown('''
**How to solve it:** Follow `Product View → Add to Cart → Checkout → Purchase`.

The overall funnel shows customer progression. The diagnosis later compares the affected journey with its own baseline to find the transition with the largest deterioration.
''')

with st.expander("03 · WHO?  →  Which device × acquisition-channel journey is driving the decline?"):
    st.markdown('''
**Your challenge:** Explore Device and Acquisition Channel performance, then lock a hypothesis.

The reveal compares each device × channel journey with its own baseline — it does not simply choose the lowest conversion rate.
''')

with st.expander("04 · WHAT NEXT?  →  What is the impact, and what should the business investigate?"):
    st.markdown('''
**Final objective:** Estimate the purchase gap at baseline performance and translate the signal into focused actions for Growth / Marketing, Product / UX and Analytics.

The purchase gap is a scenario estimate, not a causal forecast.
''')



# ============================================================
# 01 EXECUTIVE OVERVIEW
# ============================================================

st.markdown(
    """
<div id="signal"></div>
<div class="section-kicker">CLUE 01 • MONITOR THE SIGNAL</div>
<div class="section-title">Something changed. Start with the topline.</div>
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
# 02 PURCHASE FUNNEL
# ============================================================

st.divider()


st.markdown(
    """
<div id="funnel"></div>
<div class="section-kicker">CLUE 02 • DECOMPOSE THE JOURNEY</div>
<div class="section-title">Where are customers disappearing?</div>
<div class="section-copy">
Identify where customer progression weakens across the purchase journey.
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


fig_funnel.update_traces(

    textposition="inside",

    textinfo="value",

    marker_color="#2563EB",

    connector=dict(
        fillcolor="#BFDBFE",
        line=dict(
            color="#BFDBFE"
        )
    )
)


fig_funnel.update_layout(

    height=410,

    margin=dict(
        l=35,
        r=35,
        t=20,
        b=20
    ),

    paper_bgcolor="white",

    plot_bgcolor="white",

    font=dict(
        family="Inter, Segoe UI, Arial",
        color="#64748B"
    )
)


st.plotly_chart(
    fig_funnel,
    use_container_width=True,
    config={
        "displayModeBar": False
    }
)


s1, s2, s3 = st.columns(3)


with s1:

    st.markdown(
        f"""
<div class="stage-card">
<div class="stage-label">VIEW → CART</div>
<div class="stage-value">{cart_rate:.2f}%</div>
<div class="stage-note">Product-view sessions reaching cart</div>
</div>
""",
        unsafe_allow_html=True
    )


with s2:

    st.markdown(
        f"""
<div class="stage-card">
<div class="stage-label">CART → CHECKOUT</div>
<div class="stage-value">{cart_to_checkout:.2f}%</div>
<div class="stage-note">Cart sessions reaching checkout</div>
</div>
""",
        unsafe_allow_html=True
    )


with s3:

    st.markdown(
        f"""
<div class="stage-card">
<div class="stage-label">CHECKOUT → PURCHASE</div>
<div class="stage-value">{checkout_to_purchase:.2f}%</div>
<div class="stage-note">Checkout sessions completing purchase</div>
</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# 03 CONVERSION TREND
# ============================================================

st.divider()


st.markdown(
    """
<div id="timing"></div>
<div class="section-kicker">CLUE 03 • FIND THE TIMING</div>
<div class="section-title">When did behaviour begin to change?</div>
<div class="section-copy">
Monitor weekly conversion to identify when customer purchase
behaviour begins to change.
</div>
""",
    unsafe_allow_html=True
)


trend_df = filtered_df.copy()


trend_df["week_start"] = (
    trend_df["session_start"]
    .dt.to_period("W")
    .apply(
        lambda period:
        period.start_time
    )
)


weekly = (

    trend_df

    .groupby(
        "week_start",
        as_index=False
    )

    .agg(
        sessions=(
            "session_id",
            "nunique"
        ),

        purchases=(
            "purchase",
            "sum"
        )
    )
)


weekly["conversion_rate"] = (
    weekly["purchases"]
    / weekly["sessions"]
    * 100
)


fig_trend = px.line(

    weekly,

    x="week_start",

    y="conversion_rate",

    markers=True
)


fig_trend.update_traces(

    line=dict(
        color="#2563EB",
        width=3
    ),

    marker=dict(
        size=7,
        color="#FFFFFF",
        line=dict(
            width=2,
            color="#2563EB"
        )
    ),

    hovertemplate=(
        "<b>%{x|%d %b %Y}</b><br>"
        "Conversion: %{y:.2f}%"
        "<extra></extra>"
    )
)


fig_trend.update_layout(

    height=410,

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

    hovermode="x unified",

    font=dict(
        family="Inter, Segoe UI, Arial",
        color="#64748B"
    )
)


fig_trend.update_xaxes(
    showgrid=False,
    linecolor="#E2E8F0"
)


fig_trend.update_yaxes(
    gridcolor="#EEF2F7",
    zeroline=False
)


st.plotly_chart(

    fig_trend,

    use_container_width=True,

    config={
        "displayModeBar": False
    }
)

monthly = (
    trend_df.assign(month=trend_df["session_start"].dt.to_period("M").dt.to_timestamp())
    .groupby("month", as_index=False)
    .agg(sessions=("session_id", "nunique"), purchases=("purchase", "sum"))
)
monthly["conversion_rate"] = monthly["purchases"] / monthly["sessions"] * 100
monthly["change_pp"] = monthly["conversion_rate"].diff()
month_story = " → ".join(
    f"{row.month.strftime('%b')}: {row.conversion_rate:.2f}%"
    for row in monthly.itertuples()
)

if len(monthly) >= 2:
    changes = monthly.dropna(subset=["change_pp"])
    drop_row = changes.loc[changes["change_pp"].idxmin()]
    drop_month = drop_row["month"].strftime("%B")
    drop_pp = drop_row["change_pp"]
    if drop_pp < 0:
        timing_read = (
            f"The largest month-over-month deterioration occurs in "
            f"<span class='answer-number'>{drop_month}</span>: "
            f"<span class='answer-number'>{drop_pp:.2f} pp</span> versus the previous month."
        )
    else:
        timing_read = "No month in the selected range shows a month-over-month decline."
else:
    timing_read = "The selected range does not contain enough months for a month-over-month comparison."

st.markdown(
    f'''
<div class="answer-card">
<div class="answer-kicker">WHAT THE CHART TELLS US</div>
<div class="answer-title">{month_story}</div>
<div class="answer-copy">{timing_read}</div>
<div class="answer-copy"><b>Next question:</b> Is the deterioration broad-based, or concentrated in one customer journey?</div>
</div>
''',
    unsafe_allow_html=True
)


# ============================================================
# 04 PERFORMANCE DIAGNOSTICS
# ============================================================

st.divider()


st.markdown(
    """
<div id="segments"></div>
<div class="section-kicker">CLUE 04 • BUILD THE SUSPECT LIST</div>
<div class="section-title">Which customer journey deserves investigation?</div>
<div class="section-copy">
Compare customer journeys across major business dimensions.
A low conversion rate alone does not establish root cause;
the direction of change relative to historical performance matters.
</div>
""",
    unsafe_allow_html=True
)


def segment_performance(
    data,
    dimension
):

    result = (

        data

        .groupby(
            dimension,
            as_index=False
        )

        .agg(
            sessions=(
                "session_id",
                "nunique"
            ),

            purchases=(
                "purchase",
                "sum"
            )
        )
    )


    result["conversion_rate"] = (
        result["purchases"]
        / result["sessions"]
        * 100
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

    (
        "device",
        "Device"
    ),

    (
        "acquisition_channel",
        "Acquisition Channel"
    ),

    (
        "category",
        "Category"
    ),

    (
        "customer_type",
        "Customer Type"
    )
]


for tab, (
    dimension,
    label
) in zip(
    tabs,
    dimensions
):

    with tab:

        performance = (
            segment_performance(
                filtered_df,
                dimension
            )
        )


        fig_segment = px.bar(

            performance,

            x=dimension,

            y="conversion_rate",

            text="conversion_rate"
        )


        fig_segment.update_traces(

            marker_color="#2563EB",

            texttemplate="%{text:.2f}%",

            textposition="inside",

            insidetextanchor="end",

            textfont=dict(
                color="white",
                size=12
            ),

            hovertemplate=(
                "<b>%{x}</b><br>"
                "Conversion: %{y:.2f}%"
                "<extra></extra>"
            )
        )


        fig_segment.update_layout(

            height=380,

            xaxis_title=None,

            yaxis_title=(
                "Conversion rate (%)"
            ),

            margin=dict(
                l=35,
                r=25,
                t=25,
                b=35
            ),

            paper_bgcolor="white",

            plot_bgcolor="white",

            font=dict(
                family=(
                    "Inter, Segoe UI, Arial"
                ),
                color="#64748B"
            )
        )


        fig_segment.update_xaxes(
            showgrid=False,
            linecolor="#E2E8F0"
        )


        fig_segment.update_yaxes(
            gridcolor="#EEF2F7",
            zeroline=False
        )


        st.plotly_chart(

            fig_segment,

            use_container_width=True,

            config={
                "displayModeBar": False
            }
        )


        display_table = (
            performance.copy()
        )


        display_table = (
            display_table.rename(
                columns={
                    dimension: label,
                    "sessions": "Sessions",
                    "purchases": "Purchases",
                    "conversion_rate":
                    "Conversion Rate (%)"
                }
            )
        )


        st.dataframe(

            display_table.round(2),

            use_container_width=True,

            hide_index=True
        )



# ============================================================
# RECRUITER CHALLENGE — LOCK A HYPOTHESIS
# ============================================================

st.markdown(
    '''
<div class="mission-card">
<div class="mission-label">YOUR TURN · LOCK A HYPOTHESIS</div>
<div class="mission-title">Who is your leading suspect?</div>
<div class="mission-copy">Use the segment evidence above. Pick the device × acquisition-channel journey you think deteriorated most versus its own baseline.</div>
</div>
''',
    unsafe_allow_html=True
)

guess1, guess2 = st.columns(2)
with guess1:
    hypothesis_device = st.selectbox("Device hypothesis", devices, key="hypothesis_device")
with guess2:
    hypothesis_channel = st.selectbox(
        "Channel hypothesis",
        [c for c in channels if c != "Unknown"],
        key="hypothesis_channel"
    )

# ============================================================
# 05 ROOT-CAUSE DIAGNOSTIC
# ============================================================

st.divider()


st.markdown(
    """
<div id="diagnosis"></div>
<div class="section-kicker">REVEAL • TEST YOUR HYPOTHESIS</div>
<div class="section-title">Diagnosis Unlocked</div>
<div class="section-copy">
Compare each device-channel journey against its own comparison
baseline rather than assuming that the lowest-converting segment
caused the decline.
</div>
""",
    unsafe_allow_html=True
)


if compare_mode == "Previous period" and len(date_range) == 2:

    current_start = pd.Timestamp(date_range[0])
    current_end = pd.Timestamp(date_range[1]) + pd.Timedelta(days=1)
    window_days = (current_end - current_start).days

    previous_start = current_start - pd.Timedelta(days=window_days)

    diagnostic_df = df[
        df["device"].isin(selected_devices)
        & df["acquisition_channel"].isin(selected_channels)
        & df["category"].isin(selected_categories)
        & df["customer_type"].isin(selected_customer_types)
        & (df["session_start"] >= previous_start)
        & (df["session_start"] < current_end)
    ].copy()

    diagnostic_df["analysis_period"] = np.where(
        diagnostic_df["session_start"] < current_start,
        "Baseline",
        "Diagnostic"
    )

else:

    diagnostic_df = filtered_df.copy()

    diagnostic_df["analysis_period"] = np.where(
        diagnostic_df["session_start"] < pd.Timestamp("2026-05-15"),
        "Baseline",
        "Diagnostic"
    )


interaction = (

    diagnostic_df[
        diagnostic_df[
            "acquisition_channel"
        ]
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
        sessions=(
            "session_id",
            "nunique"
        ),

        purchases=(
            "purchase",
            "sum"
        )
    )
)


interaction[
    "conversion_rate"
] = (

    interaction[
        "purchases"
    ]

    / interaction[
        "sessions"
    ]

    * 100
)


interaction_pivot = (

    interaction

    .pivot_table(

        index=[
            "device",
            "acquisition_channel"
        ],

        columns=(
            "analysis_period"
        ),

        values=(
            "conversion_rate"
        )
    )

    .reset_index()
)


if (
    "Baseline"
    in interaction_pivot.columns

    and

    "Diagnostic"
    in interaction_pivot.columns
):


    interaction_pivot = (
        interaction_pivot.dropna(
            subset=[
                "Baseline",
                "Diagnostic"
            ]
        )
    )


    interaction_pivot[
        "Change (pp)"
    ] = (

        interaction_pivot[
            "Diagnostic"
        ]

        - interaction_pivot[
            "Baseline"
        ]
    )


    interaction_pivot = (
        interaction_pivot.sort_values(
            "Change (pp)"
        )
    )


    if not interaction_pivot.empty:


        worst = (
            interaction_pivot.iloc[0]
        )


        affected_device = (
            worst["device"]
        )

        affected_channel = (
            worst[
                "acquisition_channel"
            ]
        )


        # --------------------------------------------
        # SAFE RCA CARD
        # No indented multiline HTML
        # --------------------------------------------

        rca_html = (
            '<div class="rca-shell">'
            '<div class="rca-eyebrow">'
            'DIAGNOSTIC SPOTLIGHT'
            '</div>'
            '<div class="rca-segment">'
            f'{affected_device} × {affected_channel}'
            '</div>'
            '<div class="rca-description">'
            'This journey shows the largest deterioration '
            'relative to its own historical baseline: '
            f'<span class="rca-number">{worst["Baseline"]:.2f}%</span>'
            ' → '
            f'<span class="rca-number">{worst["Diagnostic"]:.2f}%</span>'
            ', representing a '
            f'<span class="rca-number">{worst["Change (pp)"]:.2f} pp</span>'
            ' change.'
            '</div>'
            '</div>'
        )


        st.markdown(
            rca_html,
            unsafe_allow_html=True
        )

        if hypothesis_device == affected_device and hypothesis_channel == affected_channel:
            st.success(
                f"🎯 Hypothesis confirmed — {affected_device} × {affected_channel} "
                "shows the largest deterioration versus its own baseline."
            )
        else:
            st.info(
                f"🔓 Diagnosis unlocked — the evidence points to {affected_device} × {affected_channel}. "
                f"Your hypothesis was {hypothesis_device} × {hypothesis_channel}. "
                "Inspect the funnel comparison below to see where this journey weakened."
            )


        with st.expander(
            "View device × channel comparison"
        ):


            comparison_table = (
                interaction_pivot.rename(
                    columns={
                        "device":
                        "Device",

                        "acquisition_channel":
                        "Acquisition Channel",

                        "Baseline":
                        "Baseline (%)",

                        "Diagnostic":
                        "Diagnostic (%)"
                    }
                )
            )


            st.dataframe(

                comparison_table.round(2),

                use_container_width=True,

                hide_index=True
            )


        # ============================================
        # FUNNEL DIAGNOSIS
        # ============================================

        affected = (

            diagnostic_df[

                (
                    diagnostic_df[
                        "device"
                    ]
                    == affected_device
                )

                &

                (
                    diagnostic_df[
                        "acquisition_channel"
                    ]
                    == affected_channel
                )
            ]
        )


        affected_funnel = (

            affected

            .groupby(
                "analysis_period",
                as_index=False
            )

            .agg(

                sessions=(
                    "session_id",
                    "nunique"
                ),

                carts=(
                    "add_to_cart",
                    "sum"
                ),

                checkouts=(
                    "checkout",
                    "sum"
                ),

                purchases=(
                    "purchase",
                    "sum"
                )
            )
        )


        affected_funnel[
            "View → Cart"
        ] = (

            affected_funnel[
                "carts"
            ]

            / affected_funnel[
                "sessions"
            ]

            * 100
        )


        affected_funnel[
            "Cart → Checkout"
        ] = (

            affected_funnel[
                "checkouts"
            ]

            / affected_funnel[
                "carts"
            ]

            * 100
        )


        affected_funnel[
            "Checkout → Purchase"
        ] = (

            affected_funnel[
                "purchases"
            ]

            / affected_funnel[
                "checkouts"
            ]

            * 100
        )


        funnel_long = (
            affected_funnel.melt(

                id_vars=(
                    "analysis_period"
                ),

                value_vars=[
                    "View → Cart",
                    "Cart → Checkout",
                    "Checkout → Purchase"
                ],

                var_name=(
                    "Funnel Stage"
                ),

                value_name=(
                    "Conversion Rate"
                )
            )
        )


        fig_rca = px.bar(

            funnel_long,

            x="Funnel Stage",

            y="Conversion Rate",

            color="analysis_period",

            barmode="group",

            color_discrete_map={
                "Baseline":
                "#1D4ED8",

                "Diagnostic":
                "#93C5FD"
            }
        )


        fig_rca.update_traces(

            texttemplate=(
                "%{y:.1f}%"
            ),

            textposition=(
                "outside"
            )
        )


        fig_rca.update_layout(

            height=420,

            xaxis_title=None,

            yaxis_title=(
                "Conversion rate (%)"
            ),

            legend_title=None,

            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="left",
                x=0
            ),

            margin=dict(
                l=35,
                r=25,
                t=55,
                b=35
            ),

            paper_bgcolor="white",

            plot_bgcolor="white",

            font=dict(
                family=(
                    "Inter, Segoe UI, Arial"
                ),
                color="#64748B"
            )
        )


        fig_rca.update_xaxes(
            showgrid=False,
            linecolor="#E2E8F0"
        )


        fig_rca.update_yaxes(
            gridcolor="#EEF2F7",
            zeroline=False
        )


        st.plotly_chart(

            fig_rca,

            use_container_width=True,

            config={
                "displayModeBar": False
            }
        )


        # ============================================
        # PRIMARY FUNNEL FRICTION
        # ============================================

        funnel_compare = (

            affected_funnel

            .set_index(
                "analysis_period"
            )

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
            "Baseline"
            in funnel_compare.columns

            and

            "Diagnostic"
            in funnel_compare.columns
        ):


            funnel_compare[
                "Change (pp)"
            ] = (

                funnel_compare[
                    "Diagnostic"
                ]

                - funnel_compare[
                    "Baseline"
                ]
            )


            funnel_compare = (
                funnel_compare.sort_values(
                    "Change (pp)"
                )
            )


            primary_friction = (
                funnel_compare.index[0]
            )


            primary_change = (
                funnel_compare.iloc[0][
                    "Change (pp)"
                ]
            )


            friction_html = (
                '<div class="insight-card">'
                '<div class="insight-title">'
                f'Primary funnel friction: {primary_friction}'
                '</div>'
                '<div class="insight-copy">'
                'This transition experienced the largest deterioration '
                'within the affected journey '
                f'({primary_change:.2f} pp versus baseline).'
                '</div>'
                '</div>'
            )


            st.markdown(
                friction_html,
                unsafe_allow_html=True
            )


        # ============================================
        # 06 COMMERCIAL IMPACT
        # ============================================

        impact = (

            affected

            .groupby(
                "analysis_period"
            )

            .agg(

                sessions=(
                    "session_id",
                    "nunique"
                ),

                purchases=(
                    "purchase",
                    "sum"
                )
            )
        )


        if (
            "Baseline"
            in impact.index

            and

            "Diagnostic"
            in impact.index
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


            diagnostic_sessions = (
                impact.loc[
                    "Diagnostic",
                    "sessions"
                ]
            )


            actual_purchases = (
                impact.loc[
                    "Diagnostic",
                    "purchases"
                ]
            )


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
<div id="impact"></div>
<div class="section-kicker">FINAL CLUE • QUANTIFY THE IMPACT</div>
<div class="section-title">What did the deterioration cost in purchases?</div>
<div class="section-copy">
Estimate the purchase opportunity associated with maintaining
historical baseline performance.
</div>
""",
                unsafe_allow_html=True
            )


            i1, i2, i3 = (
                st.columns(3)
            )


            with i1:

                st.markdown(
                    f"""
<div class="metric-card">
<div class="metric-label">Expected Purchases</div>
<div class="metric-value">{expected_purchases:.0f}</div>
<div class="metric-note">At baseline conversion</div>
</div>
""",
                    unsafe_allow_html=True
                )


            with i2:

                st.markdown(
                    f"""
<div class="metric-card">
<div class="metric-label">Actual Purchases</div>
<div class="metric-value">{actual_purchases:.0f}</div>
<div class="metric-note">Diagnostic period</div>
</div>
""",
                    unsafe_allow_html=True
                )


            with i3:

                st.markdown(
                    f"""
<div class="metric-card">
<div class="metric-label">Purchase Gap</div>
<div class="metric-value">{estimated_lost:.0f}</div>
<div class="metric-note">Scenario-based estimate</div>
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
        "baseline and diagnostic-period observations "
        "for comparison."
    )


# ============================================================
# 07 DECISION FRAMEWORK
# ============================================================

st.divider()


st.markdown(
    """
<div id="action"></div>
<div class="section-kicker">CASE CLOSED • RECOMMEND THE NEXT MOVE</div>
<div class="section-title">You found the signal. Now make the business call.</div>
<div class="section-copy">
Translate the diagnostic signal into targeted business investigation
rather than treating the entire funnel as equally problematic.
</div>
""",
    unsafe_allow_html=True
)


a1, a2, a3 = st.columns(3)


with a1:

    st.markdown(
        """
<div class="action-card">
<div class="action-number">INVESTIGATE</div>
<div class="action-title">Journey Experience</div>
<div class="action-copy">
Landing relevance, traffic quality and campaign-to-page alignment.
</div>
<div class="owner">Owner · Growth / Marketing</div>
</div>
""",
        unsafe_allow_html=True
    )


with a2:

    st.markdown(
        """
<div class="action-card">
<div class="action-number">VALIDATE</div>
<div class="action-title">Funnel Friction</div>
<div class="action-copy">
Mobile journey, checkout errors, payment failures and completion behaviour.
</div>
<div class="owner">Owner · Product / UX</div>
</div>
""",
        unsafe_allow_html=True
    )


with a3:

    st.markdown(
        """
<div class="action-card">
<div class="action-number">MONITOR</div>
<div class="action-title">Segment Health</div>
<div class="action-copy">
Device × channel conversion and material week-over-week deterioration.
</div>
<div class="owner">Owner · Analytics</div>
</div>
""",
        unsafe_allow_html=True
    )


st.markdown(
    '''
<div class="case-closed">
<div class="case-closed-label">✓ CASE CLOSED</div>
<div class="case-closed-title">You moved from a topline signal to a focused business investigation.</div>
<div class="case-closed-copy">The case used funnel behaviour, timing, segmentation, baseline comparison and a commercial-impact scenario to decide what should be investigated next — without claiming causality the data cannot prove.</div>
</div>
''',
    unsafe_allow_html=True
)


# ============================================================
# ABOUT THIS ANALYSIS
# ============================================================

st.divider()

st.markdown(
    """
<div class="section-kicker">PROJECT CONTEXT</div>
<div class="section-title">About This Analysis</div>
<div class="section-copy">
A decision-oriented e-commerce analytics case study built to move from a topline conversion signal to a focused business investigation.
</div>
""",
    unsafe_allow_html=True
)

about1, about2, about3, about4 = st.columns(4)

with about1:
    st.markdown(
        f"""<div class="metric-card"><div class="metric-label">Dataset</div><div class="metric-value">{len(df):,}</div><div class="metric-note">E-commerce sessions</div></div>""",
        unsafe_allow_html=True
    )

with about2:
    st.markdown(
        """<div class="metric-card"><div class="metric-label">Business Focus</div><div class="action-title">Conversion & Funnel</div><div class="metric-note">Customer journey and growth diagnostics</div></div>""",
        unsafe_allow_html=True
    )

with about3:
    st.markdown(
        """<div class="metric-card"><div class="metric-label">Analysis</div><div class="action-title">Trend · Segment · Baseline</div><div class="metric-note">Root-cause and scenario analysis</div></div>""",
        unsafe_allow_html=True
    )

with about4:
    st.markdown(
        """<div class="metric-card"><div class="metric-label">Built With</div><div class="action-title">Python · SQL · Excel</div><div class="metric-note">Interactive delivery in Streamlit</div></div>""",
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

**View → Cart Rate**  
Add-to-cart sessions ÷ total sessions

**Cart → Checkout Rate**  
Checkout sessions ÷ cart sessions

**Checkout → Purchase Rate**  
Purchase sessions ÷ checkout sessions

**Cart Abandonment Rate**  
Cart sessions without purchase ÷ cart sessions

**Root-cause approach**  
Each device-channel segment is compared with its own selected
comparison baseline rather than using the lowest absolute conversion rate
as evidence of root cause.

**Commercial impact**  
The purchase gap is a scenario estimate based on maintaining
historical baseline conversion. It is not a causal forecast.
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

