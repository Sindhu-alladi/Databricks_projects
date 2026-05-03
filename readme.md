# HEALTHCAREX_PROJECT

End-to-End Healthcare Data Engineering Pipeline

---

## Project Overview

This is a project I built to learn data engineering in healthcare. I played two roles: the client who creates messy data, and the data engineer who cleans it up.

As the client, I designed a Hospital Management System (HMS) and filled it with fake patient, doctor, visit, treatment, and claim data. I made it realistic by adding problems like duplicates, bad formatting, and missing info - just like real data.

As the data engineer, I built a pipeline to take that messy data and turn it into clean tables for analysis. It uses the Medallion Architecture: Bronze (raw), Silver (cleaned), Gold (ready for business).

The goal is to show how data moves from source to analytics, and how to fix quality issues along the way.

---

## Project Objective

From the client side, I created a system with real data problems. From the engineer side, I processed it into useful datasets.

This lets us analyze things like patient trends, treatment costs, doctor stats, visits, and claims.

---

## Tools & Technologies

I used these tools:

- Python with Faker: To make fake healthcare data.
- MySQL: For the database.
- Pentaho Data Integration: For moving data between files and database.
- Databricks: For processing data in the cloud.
- Apache Spark: For fast data handling in Databricks.

---

## Project Folder Structure

This project has two main areas: the client side that creates source data, and the data engineering side that processes it.

```
data_engineer_project/
├── client/
│   ├── source/
│   ├── hms_csv_output/
│   ├── sql/
│   └── transformations/
└── data_engineer/
    ├── Medallion Architecture notebooks/
    ├── vw_csv_job/
    ├── vw_csv_transformations/
    └── workbench_output/
```

- `client/source/`: Python script that generates the HMS data.
- `client/hms_csv_output/`: Raw CSV files created from the source data.
- `client/sql/`: SQL scripts for table and view creation.
- `client/transformations/`: Pentaho jobs to load CSVs into MySQL.
- `data_engineer/Medallion Architecture notebooks/`: Notebooks for Bronze, Silver, and Gold processing.
- `data_engineer/vw_csv_job/`: Pentaho job that exports data from views.
- `data_engineer/vw_csv_transformations/`: Pentaho transformations for view exports.
- `data_engineer/workbench_output/`: Final CSVs ready for Databricks.

---

## End-to-End Project Flow

Here's how the data flows:

1. Start with MySQL database.
2. Use Python to export messy CSVs.
3. Load CSVs into MySQL with Pentaho.
4. Create views in MySQL.
5. Export views to clean CSVs with Pentaho.
6. Ingest into Databricks Bronze.
7. Clean in Silver.
8. Aggregate in Gold.

---

## Phase-Wise Implementation

### Phase 1: HMS Design & Data Generation (Client)

I designed MySQL tables for patients, doctors, etc., with keys and rules. Then used Python to generate data—500 patients, 50 doctors, etc. Added issues like duplicates to make it real.

### Phase 2: CSV to MySQL with Pentaho

Loaded the CSVs into MySQL tables using Pentaho transformations.

### Phase 3: Views & Clean CSVs

Made MySQL views to pick useful columns. Exported them to CSVs.

### Phase 4: Raw Data

Just stored the data as-is.

### Phase 5: Medallion in Databricks

- Bronze: Ingest raw CSVs as strings.
- Silver: Fix types, remove duplicates, clean data.
- Gold: Make summary tables for analysis.

---

## Key Learnings

- How data flows end-to-end.
- Why data quality matters.
- Using tools like Pentaho and Databricks.
- Thinking from client and engineer views.

---

## Conclusion

This project helped me learn data engineering. I got experience with real tools and processes.