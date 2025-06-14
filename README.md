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
AWS Glue (PySpark ETL) -> YouTube API (data extraction) -> Amazon S3 (CSV output)

##  Technologies used
- AWS Glue (ETL & job orchestration)
- Apache Spark / PySpark (Data processing)
- Amazon S3 (for cloud storage)
- YouTube Data API v3 (for fetching video metadata)

Deploy the script in AWS Glue as a PySpark job.
Execute the job via the AWS Glue console, CLI, or trigger-based workflow.

## Key Functions
Functions | Purpose |
- get_upload_playlist_id() | Returns the channel playlist using apikey and channelid.
- get_all_video_ids() | Gets the video list for the channel and stores it into a list object.
- get_video_stats() | Loops through the created video list and gets all the video attributes.

## Security & IAM
Make sure your AWS Glue job role includes the following permissions:
- AmazonS3FullAccess (or more restricted access to your target S3 bucket)
- Logs and Glue-related permissions if triggering via workflow or scheduler

## Deployment
1. Deploy the script in AWS Glue as a **PySpark Job**.
2. Provide script arguments (like API key and channel ID) in the **Job Parameters** section.
3. Run the job via:
   - AWS Glue Console
   - AWS CLI
   - AWS Glue Workflows (optional)

## Author
Shailesh Mistry – [LinkedIn](https://www.linkedin.com/in/shailesh-mistry-a346659)
