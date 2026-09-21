# 📰 Terminal News Data Pipeline

![Python](https://img.shields.io/badge/Python-3.14%2B-blue)
![Dependencies](https://img.shields.io/badge/Dependencies-feedparser%20%7C%20rich-success)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)

An enterprise-grade, API-free command-line application that acts as a robust Data Extraction and Visualization Pipeline. It scrapes real-time RSS feeds, builds a dynamic terminal dashboard, and exports structured JSON reports. 

Built as a data engineering portfolio project to demonstrate resilient system design, this pipeline operates entirely locally—bypassing cloud API rate limits or server outages. It is engineered for strict stability, making it an ideal showcase of architectural skills for rigorous technical environments, such as Indian government IT infrastructure or large-scale enterprise systems.

## ✨ Features

* **Real-Time Data Extraction:** Pulls live RSS data instantly without requiring external Large Language Models or API keys.
* **Rich Terminal Dashboard:** Utilizes the `rich` library for color-coded panels, structured data grids, and dynamic loading spinners.
* **Automated JSON Export:** Implements an ETL methodology by automatically formatting and exporting raw scraped data into timestamped JSON files for downstream analytics.
* **Interactive Browser Routing:** Allows users to select and open specific articles natively in their default macOS/system web browser directly from the CLI.
* **Bulletproof Architecture:** Designed with continuous execution loops and graceful error handling to prevent sudden crashes.

## 🛠 Tech Stack

* **Language:** Python 3.14
* **Libraries:** 
  * `feedparser` (RSS Data Extraction)
  * `rich` (Advanced UI/UX in CLI)
  * `urllib`, `json`, `os` (Core standard Python libraries)

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR-USERNAME/terminal-news-pipeline.git](https://github.com/YOUR-USERNAME/terminal-news-pipeline.git)
   cd terminal-news-pipeline
