📦 Olist E-commerce SQL Analysis

A complete end-to-end SQL analytics project using the Brazilian Olist E-commerce Dataset.
This project uses PostgreSQL + DBeaver, with data stored under schema raw.

📌 1. Objective

The goal of this project is to analyze customer behavior, order performance, delivery efficiency, product categories, and seller operations using SQL only.

This project simulates a real analytics workflow:

Business Questions → Data Modeling → SQL Analysis → Insights

📚 2. Dataset Overview

The Olist dataset contains 9 raw tables, each representing a key part of the e-commerce operation:

Table	Description
customers	Customer IDs, city, state
orders	Order lifecycle timestamps & statuses
order_items	Product, seller, price, freight
order_payments	Payment type and amount
order_reviews	Customer satisfaction feedback
products	Product attributes
sellers	Seller information
geolocation	Geospatial mapping
product_category_name_translation	Category names EN → PT
Database structure:
database: olist
schema: raw


CSV files are stored locally and excluded from Git via .gitignore.

🎯 3. Business Questions (Analytics Scope)

To reflect a real analytics workflow, questions are grouped into five themes.

🟦 A. Orders & Revenue Performance
Q1.1 – Monthly revenue, order count, AOV over time

Insights from SQL results:

Sales activity begins to scale significantly from January 2017, growing from a few hundred orders per month to several thousand.

Monthly revenue shows a strong upward trajectory throughout 2017 and early 2018, peaking at 1.15M BRL (Nov 2017) and consistently remaining above 1M BRL during 2018.

Order volume reaches its highest levels around May–July 2018, with 6,700–7,000+ orders per month.

AOV stays stable between 150–170 BRL, indicating consistent customer spending even as order volume rises.

Extremely low early months (e.g., Dec 2016: 1 order) are edge cases—likely due to incomplete dataset coverage at the start.

Overall trend: Strong sustained growth in revenue and orders → a healthy, rapidly expanding marketplace.

Q1.2 – Order status funnel

Delivered, shipped, canceled, unpaid distribution.

Q1.3 – Daily & weekly sales trends

Seasonality, weekday patterns, peak days.

Q1.4 – Freight impact on revenue

How freight value varies across states and its relation to order size.

🟩 B. Customer Behavior & Loyalty

Q2.1 – Returning vs one-time customers (repeat rate)

Q2.2 – Customer LTV approximation (based on total order value)

Q2.3 – Delivery time differences across regions

🟧 C. Delivery & Logistics Efficiency

Q3.1 – Actual vs estimated delivery time

Q3.2 – Late deliveries by state & by seller

Q3.3 – Inconsistent timestamps (e.g., delivered before shipped)

🟪 D. Product & Category Insights

Q4.1 – Best-selling categories (quantity & revenue)

Q4.2 – Categories with highest review scores

Q4.3 – Price distribution across categories

🟨 E. Seller Performance

Q5.1 – Top sellers by revenue

Q5.2 – Seller cancellation rate

Q5.3 – Seller delivery performance

(You may expand these analyses further.)

🗺️ 4. Data Model (ERD)

The Olist dataset follows a star-schema-like structure:

customers  ←  orders  →  order_items  →  sellers
                                 ↓
                             products
                                 ↓
                 product_category_name_translation


You can add your ERD diagram later:

![ERD](./docs/erd.png)

🧠 5. SQL Queries

All SQL queries are stored in:

👉 queries.sql

Each query is labeled and aligned with the question numbers above.

🛠️ 6. Tools Used

PostgreSQL 16

DBeaver (Community or Ultimate)

Git & GitHub

(Optional) Power BI or Python for extended analysis

🚀 7. How to Use This Repository

Clone the repo

Create PostgreSQL database olist

Create schema raw

Import CSV files into tables

Run queries inside queries.sql

🔮 8. Future Extensions

After SQL analysis is complete, future work will include:

Power BI dashboard

Python exploratory analysis

ML mini-model: delivery delay prediction

📄 9. License

This project is open-source under the MIT License.