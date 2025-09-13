# Uptime Checker

A simple Python script to monitor the uptime of websites and alert you to any downtime.

---

## Features

- Website Monitoring: Checks the availability of URLs listed in a `sites.txt` file.
- Customizable Timeout: Configurable timeout settings to adjust the response time threshold.
- Notification Support: Sends alerts via email (SMTP) when a site is down.
- Docker Support: Easily deployable using Docker for consistent environments.

---

## Prerequisites

- Python 3.8 or higher
- Docker (optional, for containerized deployment)
- SMTP server credentials for email notifications

---

## Setup & Configuration

### 1. Clone the Repository
```bash
git clone https://github.com/ca5ual/uptime-checker.git
cd uptime-checker
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Sites

Edit the `sites.txt` file to include the URLs you wish to monitor.

### 4. Configure SMTP Settings

Update the `checker.py` script with your SMTP server credentials for email notifications.

### 5. Run the Script
```bash
python checker.py
```

The script will check the availability of the sites listed in `sites.txt` and send email alerts if any are down.

---

## Docker Deployment (Optional)

### 1. Build the Docker Image
```bash
docker build -t uptime-checker .
```

### 2. Run the Docker Container
```bash
docker run -d --name uptime-checker uptime-checker
```
Ensure that your SMTP configuration is correctly set within the container environment.

---

## License

This project is licensed under the MIT License - see