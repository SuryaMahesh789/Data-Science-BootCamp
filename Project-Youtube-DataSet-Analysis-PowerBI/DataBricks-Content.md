DataBricks

Data Engineering in the YouTube Dataset Project

In this project, Databricks was utilized to efficiently process and analyze the YouTube dataset using PySpark. The primary goal was to perform Exploratory Data Analysis (EDA), but several important Data Engineering tasks were essential to prepare the data for analysis.


Key Data Engineering Tasks:

1. Data Ingestion
Source: The YouTube dataset was ingested from Azure Blob Storage, a cloud storage solution integrated with Databricks.
Task: Data was directly read from Azure Blob Storage into Databricks using PySpark’s DataFrame API for distributed processing.

2. Data Cleaning
Handling Missing Data: Missing values in columns such as ratings, views, or comments were handled by removing incomplete records.

3. Data Transformation
Task: Data transformation involved:
Feature Engineering: Created a video_popularity column by combining views, comments, and ratings.
Normalization: The video_popularity field was normalized to bring it onto a consistent scale for fair comparison across all videos.

4. Data Aggregation
Task: Aggregate data to compute metrics like total views, total ratings, and average comments for analysis.

5. Data Exploration (EDA)
Task: Perform exploratory analysis to identify trends in video performance, such as:
Which categories have the highest average views and ratings?