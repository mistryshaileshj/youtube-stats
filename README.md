# AWS Glue ETL Job for YouTube Channel Statistics

## Overview
This project implements an **AWS Glue-based ETL** (Extract, Transform, Load) job to retrieve statistics for a YouTube channel using the **YouTube Data API**, and stores the structured output in **Amazon S3** as CSV files for further analytics and reporting.

##  Features
- Retrieves YouTube video data using the YouTube Data API v3 via PySpark in AWS Glue.
- Requires a **YouTube API key** and **Channel ID**
- Refer to `get-google-api-key-channelid.txt` for steps to obtain them.
- Extracts key video attributes:
  - video_id - Youtube Video Id
  - title - Video title
  - published_at - Date/Time of publication
  - views - Views count
  - likes - Likes count
  - comments - Comments if any
- Filters the dataset by published year.
- Saves the processed data to s3 in csv format.

## Architecture
AWS Glue (PySpark ETL) -> Data retrieval via google api, Data Cleaning, Transformation & Aggregation -> S3 (CSV files)

##  Technologies used
- AWS Glue (ETL & job orchestration)
- Apache Spark / PySpark (Data processing)
- Amazon S3 (Data storage)

Deploy the script in AWS Glue as a PySpark job.
Execute the job via the AWS Glue console, CLI, or trigger-based workflow.

## Key Functions and it's purpose
- get_upload_playlist_id() -> Returns the channel playlist using apikey and channelid.
- get_all_video_ids() -> Gets the video list for the channel and stores it into a list object.
- get_video_stats() -> Loops through the created video list and gets all the video attributes.

## Security & IAM
Ensure IAM roles assigned to Glue have permissions to:
- S3 full access

## Author
Shailesh Mistry – [LinkedIn](https://www.linkedin.com/in/shailesh-mistry-a346659)
