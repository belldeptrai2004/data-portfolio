/* =====================================================================
   OLIST DELIVERY DELAY & CUSTOMER SATISFACTION – SQL ANALYSIS
   Author: Pham Minh Khoi
   Tool: DBeaver Ultimate
   Database: PostgreSQL
   Schema: raw
   Scope: Portfolio (SQL-only), single business story
   ===================================================================== */

/* =====================================================================
   0. PROJECT FRAME
   Business Story:
     - Delivery Delay → Customer Satisfaction (Review Score)

   Core Questions:
     Q1. Do late deliveries receive lower review scores?
     Q2. How does review severity change across delay buckets?
     Q3. Which customer regions exhibit higher late-delivery risk?

   Output Standard (for screenshots/README):
     - Clean, order-level tables with counts, rates, and robust summaries
   ===================================================================== */

/* =====================================================================
   1. BUILD ANALYSIS DATASET (ORDER-LEVEL FACT VIEW)
   File section name: BASE FACT VIEW

   Goal:
     - Create a standardized order-level dataset to support all queries.
     - Join only essential tables:
         raw.orders, raw.order_reviews, raw.customers
     - Derive:
         delivery_days, delay_days, delay_bucket

   Expected Output Columns:
     order_id
     customer_id
     customer_state
     purchase_ts
     delivered_customer_ts
     estimated_delivery_ts
     review_score
     delivery_days
     delay_days
     delay_bucket
   ===================================================================== */

/* =====================================================================
   2. DATA QUALITY CHECKS
   File section name: DATA QUALITY

   Checks:
     - Delivered order coverage vs fact view coverage
     - Duplicate order_id in fact view (should be 1 row per order)
     - Missing timestamps (purchase/delivered/estimated)
     - Impossible sequences (delivered < purchase)

   Expected Outputs:
     - Summary counts table
     - Duplicate list (should be empty)
     - Anomaly count + sample rows (LIMIT 20)
   ===================================================================== */

/* =====================================================================
   3. BASELINE METRICS (SANITY KPIs)
   File section name: KPI BASELINE

   KPIs:
     - Total delivered orders in analysis
     - On-time rate (% delay_days <= 0)
     - Late rate (% delay_days > 0)
     - Median delay_days (overall + late only)
     - Average review_score (overall)

   Expected Outputs:
     - 1 KPI table (single row)
     - Optional: KPI breakdown by delay_bucket
   ===================================================================== */

/* =====================================================================
   4. RELATIONSHIP ANALYSIS (CORE INSIGHT)
   File section name: DELAY VS REVIEW

   Analysis:
     - Review_score summary by delay_bucket
         count_orders
         avg_review_score
         median_review_score
         pct_1_2_star
         pct_5_star
     - Optional: review distribution (counts by score 1–5) per bucket

   Expected Outputs:
     - 1 main summary table (for screenshot)
     - Optional distribution table (for deeper evidence)
   ===================================================================== */

/* =====================================================================
   5. SEGMENTATION (WHERE IS THE RISK?)
   File section name: SEGMENTATION (CUSTOMER REGION)

   Analysis:
     - Late delivery rate by customer_state
         total_orders
         late_orders
         late_rate
         avg_delay_days (late only)
         avg_review_score
     - Rank worst states by late_rate and/or avg_delay_days

   Expected Outputs:
     - Top 10 worst states table
     - Optional: full table export
   ===================================================================== */

/* =====================================================================
   6. SYNTHESIS QUERIES (FINAL TABLES USED IN README)
   File section name: SYNTHESIS

   Goal:
     - Produce final “presentation-ready” outputs:
         - Key Findings table (bucket metrics)
         - Top risk states table

   Expected Outputs:
     - 2 final tables, stable formatting, ready for screenshots
   ===================================================================== */

/* =====================================================================
   7. END OF FILE
   Notes:
     - Keep all queries in this file ordered by sections above.
     - Each section should produce 1–2 screenshot-worthy result tables max.
     - Avoid expanding scope to payments/sellers/categories unless necessary.
   ===================================================================== */
