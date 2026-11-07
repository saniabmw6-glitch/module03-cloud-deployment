# AWS Cloud Deployment Project

## Overview
A cloud-based web application deployment project developed as part of Module 03: Cloud Services & Web App Deployment.

## Technologies
- AWS EC2
- AWS IAM
- AWS S3
- AWS Systems Manager Parameter Store
- AWS CloudWatch
- Nginx
- Python Flask
- Linux Ubuntu
- Git and GitHub

## Key Features
- Web application deployed on AWS EC2.
- Nginx configured as a reverse proxy.
- Flask backend API.
- Secure configuration using AWS Systems Manager Parameter Store.
- S3 integration for visit counter storage.
- IAM role-based access.
- Application logging and monitoring.
  ## 🌐 Live Website Preview

![Cloud Deployment Project](screenshots/website.png)

## Architecture
See [Architecture Diagram Source](documentation/architecture.mmd).

## Security
- IAM role instead of hardcoded AWS credentials.
- Least-privilege permissions.
- Private S3 bucket.
- Sensitive files excluded from Git.

## API Endpoint
`/api/status`

## Learning Outcomes
- AWS cloud deployment
- Linux administration
- Nginx configuration
- Flask deployment
- IAM and cloud security
- AWS monitoring and logging

## Author
Sania Chaudhary
