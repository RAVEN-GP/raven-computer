# RAVEN - Computer ("Mission Control")

![Raven Computer](https://img.shields.io/badge/Component-Computer-grey) ![Status](https://img.shields.io/badge/Status-Active-success)

The **Computer** repository hosts the dashboard and pit-station tools used for monitoring the vehicle during operation. It also includes the V2X communication simulation servers.

## 📚 Documentation
> **Full Technical Documentation:** [bosch-future-mobility-challenge-documentation.readthedocs-hosted.com](https://bosch-future-mobility-challenge-documentation.readthedocs-hosted.com)

---

## 🚀 Key Features

| Task ID | Feature Name | Description |
| :--- | :--- | :--- |
| **[007a]** | **Telemetry Dashboard** | Web-based interface to visualize speed, steering, and camera feeds. |
| **[V2X]** | **Traffic Comm Server** | Simulates the competition server for traffic light status and localization. |
| **[Log]** | **Data Analysis** | Tools for parsing and plotting run logs. |

## 🛠️ Usage

### Starting the Dashboard
```bash
cd src/dashboard
python3 app.py
```
Access the dashboard at `http://localhost:5000`.
