# E-commerce Product Conversion & Growth Analytics

An end-to-end product analytics case study focused on diagnosing conversion deterioration across the e-commerce purchase funnel, identifying the customer journeys driving the decline, and translating analytical findings into measurable business impact.

## Live Analysis

🌐 **Interactive Streamlit App:**  
https://ecommerce-conversion-growth-analytics.streamlit.app/

📓 **Python Analysis:**  
`Ecommerce_Product_Conversion_Growth_Analytics.ipynb`

📊 **Excel Business Analysis:**  
`Ecommerce_Conversion_Growth_Analysis.xlsx`

🗄️ **SQL Analysis:**  
`ecommerce_conversion_analysis.sql`

---

## Business Problem

An e-commerce business is experiencing deterioration in purchase conversion despite continued customer traffic.

The objective of this analysis is not simply to identify the lowest-converting segment, but to determine:

- When did conversion performance begin to deteriorate?
- Which customer journeys experienced the largest decline relative to their own historical performance?
- At which stage of the purchase funnel is the deterioration concentrated?
- Is the decline explained by traffic mix or by weaker within-segment performance?
- What is the potential commercial impact of the observed deterioration?
- Which areas should the business investigate first?

The analysis follows a structured diagnostic framework:

**Monitor → Detect → Diagnose → Quantify → Act**

---

## Dataset

This project uses a **synthetic event-level e-commerce dataset created for analytical case-study purposes**.

The dataset represents customer activity across the purchase journey:

**Product View → Add to Cart → Checkout → Purchase**

It contains customer-session and event information including:

- Session ID
- Event timestamp
- Device
- Acquisition channel
- Product category
- Customer type
- Funnel events
- Order ID
- Purchase value

The data covers approximately **30,000 shopping sessions** across January–June 2026.

> The dataset does not contain real customer or company data.

---

## Data Quality & Preparation

Before analysis, the event-level dataset was validated and cleaned to create a reliable analytical foundation.

### Key Data Quality Checks

- Raw event records: **68,692**
- Exact duplicate records identified: **137**
- Clean event records: **68,555**
- Missing acquisition-channel records: **274**
- Acquisition channels recovered from the same session: **218**
- Remaining unresolved channels: **56**
- Missing purchase order IDs after cleaning: **0**

Unresolved acquisition channels were retained as **Unknown** rather than incorrectly assigning them to another channel.

---

## Analytical Design

The raw dataset is event-level, but conversion is fundamentally a **session-level metric**.

Therefore, event records were transformed into a session-level analytical table before calculating conversion metrics.

This prevents customers generating multiple events within the same session from artificially inflating funnel denominators.

### Core Metrics

**Purchase Conversion Rate**

`Purchase Sessions ÷ Total Sessions`

**View → Cart Rate**

`Add-to-Cart Sessions ÷ Total Sessions`

**Cart → Checkout Rate**

`Checkout Sessions ÷ Add-to-Cart Sessions`

**Checkout → Purchase Rate**

`Purchase Sessions ÷ Checkout Sessions`

**Cart Abandonment Rate**

`Cart Sessions Without Purchase ÷ Cart Sessions`

---

## Executive Baseline

Across the full analysis period:

| KPI | Result |
|---|---:|
| Total Sessions | 30,000 |
| Purchase Sessions / Orders | 5,482 |
| Conversion Rate | 18.27% |
| GMV | ₹15.29M |
| Average Order Value | ₹2,788.55 |
| Cart Abandonment Rate | 51.59% |

These metrics establish the overall commercial baseline before deeper diagnostic analysis.

---

## Conversion Trend

Monthly conversion performance showed a visible deterioration toward the end of the analysis period.

| Month | Conversion Rate |
|---|---:|
| January 2026 | 19.01% |
| February 2026 | 19.10% |
| March 2026 | 18.17% |
| April 2026 | 19.02% |
| May 2026 | 18.12% |
| June 2026 | 16.26% |

The decline becomes particularly visible in **June 2026**, where conversion falls to **16.26%**.

This establishes **when** performance weakened, but not yet **why**.

---

## Root-Cause Framework

A key principle of the analysis is:

> **The lowest-converting segment is not automatically the cause of the overall decline.**

Each segment is therefore compared against **its own historical baseline**.

For diagnostic analysis, the periods were defined as:

- **Baseline:** Before 15 May 2026
- **Diagnostic Period:** 15 May 2026 onward

Performance was investigated across:

- Device
- Acquisition channel
- Device × Acquisition Channel
- Product category
- Customer type
- Funnel stage

---

## Key Diagnostic Finding

The largest deterioration relative to historical performance was concentrated in:

### Mobile × Paid Search

Conversion moved from approximately:

**17.65% → 9.40%**

representing a decline of approximately:

**-8.25 percentage points**

This is more informative than simply identifying a low-converting segment because the comparison measures **change relative to that journey's own previous performance**.

---

## Funnel Root-Cause Analysis

After isolating the affected **Mobile × Paid Search** journey, the purchase funnel was decomposed into:

1. View → Cart
2. Cart → Checkout
3. Checkout → Purchase

The analysis showed that **View → Cart remained comparatively stable**, while deterioration became more pronounced deeper in the purchase journey.

The largest decline was concentrated at:

### Checkout → Purchase

with an estimated deterioration of approximately:

**-24.20 percentage points versus baseline**

This suggests that the strongest analytical signal is located near **purchase completion**, rather than initial product engagement.

This result should be treated as a diagnostic signal rather than proof of a specific causal mechanism.

---

## Segment Context

Overall conversion rates also provide useful context.

### Device

| Device | Conversion Rate |
|---|---:|
| Desktop | 20.02% |
| Tablet | 17.78% |
| Mobile | 17.69% |

### Acquisition Channel

| Channel | Conversion Rate |
|---|---:|
| Email | 23.20% |
| Direct | 18.96% |
| Organic Search | 18.81% |
| Affiliate | 18.66% |
| Paid Search | 17.06% |
| Social | 15.83% |

### Customer Type

| Customer Type | Conversion Rate |
|---|---:|
| Returning | 21.21% |
| New | 16.13% |

These absolute conversion rates provide context, while the root-cause analysis focuses on **deterioration relative to historical performance**.

---

## Traffic Mix vs Performance Effect

A decline in overall conversion can occur because:

1. Traffic shifts toward naturally lower-converting segments, or
2. Existing segments themselves begin converting less effectively.

The analysis therefore separates **traffic-mix effects** from **within-segment performance deterioration**.

The diagnostic evidence indicates that the decline cannot be understood from traffic composition alone.

A meaningful portion of the deterioration is concentrated within specific customer journeys, particularly the identified **Mobile × Paid Search** segment.

---

## Commercial Impact Scenario

To translate the diagnostic finding into business terms, the affected segment's diagnostic-period purchase volume was compared with a scenario where its historical baseline conversion rate had been maintained.

For the identified journey:

| Metric | Result |
|---|---:|
| Expected Purchases at Baseline Performance | ~210 |
| Actual Purchases | 112 |
| Estimated Purchase Gap | ~98 |

This represents a **scenario-based opportunity estimate**, not a causal forecast.

It quantifies the commercial magnitude associated with the observed conversion deterioration and helps prioritize further investigation.

---

## Business Recommendations

Based on the diagnostic evidence, the next investigation should focus on the affected customer journey rather than applying broad changes across all traffic.

### 1. Investigate Mobile Journey Experience

Review:

- Mobile landing-page experience
- Page-load performance
- Product-page usability
- Campaign-to-landing-page alignment
- Mobile-specific navigation friction

### 2. Validate Checkout & Purchase Friction

Investigate:

- Checkout errors
- Payment failures
- Payment-method availability
- Form or address-validation issues
- Unexpected shipping or pricing changes
- Purchase-completion latency

### 3. Review Paid Search Traffic Quality

Compare:

- Campaign
- Keyword
- Landing page
- New vs returning users
- Conversion before and after the deterioration period

### 4. Monitor Segment-Level Conversion

Track:

**Device × Channel × Funnel Stage**

rather than relying only on aggregate conversion.

This allows deterioration to be detected before it becomes hidden inside overall averages.

---

## Interactive Diagnostic App

The project includes a Streamlit application designed as an analytical decision tool rather than a static dashboard.

### The app allows users to:

- Filter by date
- Filter by device
- Filter by acquisition channel
- Filter by product category
- Filter by customer type
- Monitor executive conversion KPIs
- Explore the purchase funnel
- Track weekly conversion
- Compare segment performance
- Identify the largest device-channel deterioration
- Diagnose the affected funnel stage
- Estimate commercial impact

### Live App

https://ecommerce-conversion-growth-analytics.streamlit.app/

---

## SQL Analysis

SQL was used to reproduce core analytical questions independently from the Python workflow.

The SQL analysis includes:

- Overall funnel performance
- Monthly conversion trends
- Device × Channel diagnostics
- Customer-segment performance

File:

`ecommerce_conversion_analysis.sql`

---

## Excel Analysis

A business-facing Excel workbook was created to provide an additional analytical output outside the Python environment.

It includes structured analysis tables and KPI summaries suitable for business review.

File:

`Ecommerce_Conversion_Growth_Analysis.xlsx`

---

## Project Deliverables

| Deliverable | Purpose |
|---|---|
| `Ecommerce_Product_Conversion_Growth_Analytics.ipynb` | End-to-end Python analysis and root-cause investigation |
| `app.py` | Interactive Streamlit diagnostic application |
| `streamlit_session_data.csv` | Session-level dataset used by the application |
| `clean_ecommerce_events.csv` | Cleaned event-level dataset |
| `ecommerce_session_analytics.csv` | Session-level analytical dataset |
| `ecommerce_conversion_analysis.sql` | SQL business analysis |
| `Ecommerce_Conversion_Growth_Analysis.xlsx` | Excel business analysis |
| `requirements.txt` | Application dependencies |

---

## Tools & Skills Demonstrated

**Python**
- Pandas
- NumPy
- Data cleaning
- Data validation
- Exploratory analysis
- Root-cause analysis
- Funnel analysis

**SQL**
- Aggregations
- Conditional logic
- Segmentation
- Funnel metrics
- Conversion analysis

**Excel**
- Business analysis
- KPI reporting
- Analytical summaries

**Product & Business Analytics**
- Conversion analysis
- Funnel diagnostics
- Segmentation
- Baseline comparison
- Root-cause investigation
- Commercial-impact estimation
- Business recommendations

**Streamlit & Plotly**
- Interactive analytics application
- Dynamic filtering
- KPI monitoring
- Diagnostic visualization

---

## Why This Project

This project goes beyond reporting **what happened**.

The analysis is structured to answer progressively deeper business questions:

**What changed?**  
Conversion deteriorated toward the end of the period.

**Where did it change?**  
The deterioration was concentrated within specific customer journeys.

**Which journey showed the strongest signal?**  
Mobile × Paid Search.

**Where in that journey did performance weaken most?**  
Checkout → Purchase.

**Why does it matter commercially?**  
Maintaining historical baseline performance corresponds to an estimated purchase gap of approximately 98 orders in the diagnostic scenario.

**What should the business investigate next?**  
Mobile purchase completion, checkout/payment friction, and Paid Search journey quality.

---

## Repository Structure

```text
ecommerce-conversion-growth-analytics/
│
├── Ecommerce_Product_Conversion_Growth_Analytics.ipynb
├── Ecommerce_Conversion_Growth_Analysis.xlsx
├── ecommerce_conversion_analysis.sql
├── clean_ecommerce_events.csv
├── ecommerce_session_analytics.csv
├── streamlit_session_data.csv
├── app.py
├── requirements.txt
└── README.md
```

---

## Author

**Disha Pramanick**  
Data Analyst | Business & Product Analytics

**Portfolio:**  
https://dishapramanick2018-eng.github.io/

**LinkedIn:**  
https://www.linkedin.com/in/disha-pramanick-96545a380/

**GitHub:**  
https://github.com/dishapramanick2018-eng
