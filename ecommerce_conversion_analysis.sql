
-- E-commerce Product, Conversion Funnel & Growth Analytics


-- 1. Overall Conversion Funnel

SELECT
    COUNT(DISTINCT session_id) AS total_sessions,
    SUM(add_to_cart) AS cart_sessions,
    SUM(checkout) AS checkout_sessions,
    SUM(purchase) AS purchase_sessions,
    ROUND(
        100.0 * SUM(purchase)
        / COUNT(DISTINCT session_id),
        2
    ) AS conversion_rate
FROM sessions;


-- 2. Conversion by Device

SELECT
    device,
    COUNT(DISTINCT session_id) AS sessions,
    SUM(purchase) AS purchases,
    ROUND(
        100.0 * SUM(purchase)
        / COUNT(DISTINCT session_id),
        2
    ) AS conversion_rate
FROM sessions
GROUP BY device
ORDER BY conversion_rate DESC;


-- 3. Conversion by Acquisition Channel

SELECT
    acquisition_channel,
    COUNT(DISTINCT session_id) AS sessions,
    SUM(purchase) AS purchases,
    ROUND(
        100.0 * SUM(purchase)
        / COUNT(DISTINCT session_id),
        2
    ) AS conversion_rate
FROM sessions
GROUP BY acquisition_channel
ORDER BY conversion_rate DESC;


-- 4. Monthly Conversion Trend

SELECT
    month,
    COUNT(DISTINCT session_id) AS sessions,
    SUM(purchase) AS purchases,
    ROUND(
        100.0 * SUM(purchase)
        / COUNT(DISTINCT session_id),
        2
    ) AS conversion_rate
FROM sessions
GROUP BY month
ORDER BY month;
