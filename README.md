# 🛡️ n8n DA Shield: Autonomous Retail Intelligence Pipeline

[![n8n](https://img.shields.io/badge/Orchestration-n8n-FF6D5B?style=flat-square&logo=n8n)](https://n8n.io/)
[![Python](https://img.shields.io/badge/Backend-Python_3.10+-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=flat-square&logo=sqlite)](https://www.sqlite.org/)
[![Docker](https://img.shields.io/badge/Infrastructure-Docker-2496ED?style=flat-square&logo=docker)](https://www.docker.com/)

An end-to-end, autonomous data analysis pipeline designed to solve the **"Decision Velocity"** problem for C-Suite executives. This system transforms raw transactional data into actionable business narratives.

---

## 🏛️ The 3-Pillar Shield Architecture

This project is built on a decoupled, microservices-based architecture to ensure scalability and environment parity.

1.  **Pillar 1: The Warehouse (SQLite)**
    *   Migrates 541k+ transactions from unoptimized Excel files into an ACID-compliant, indexed SQL database.
    *   Achieves **near-instant search speeds** using high-speed database indexing on key relational fields.

2.  **Pillar 2: The Manager (n8n)**
    *   Orchestrates autonomous "Shields" that monitor data health and business risk.
    *   Communicates with the warehouse via a custom **Python REST API (Data Bridge)** to solve container isolation challenges.

3.  **Pillar 3: The Brain (LLM Model)**
    *   Uses advanced reasoning to perform semantic analysis and narrative storytelling.
    *   Converts complex data patterns into "CEO-ready" strategic advice (e.g., "The Fading Giant" narrative for VIP churn).

---

## 📊 Business Impact & Core "Shields"

### 1. The Revenue Shield (Product Leakage)
Detects systemic vs. isolated product return risks.
*   **Metric Identified**: Analyzed **£896,812** in total revenue leakage (returns).
*   **Strategic Value**: Identifies if a surge in returns is a product failure (Systemic) or a single-customer logistical issue (Isolated).

### 2. The VIP Shield (Customer Retention)
Autonomous **RFM (Recency, Frequency, Monetary)** tracking.
*   **Detection**: Automatically flags "Fading VIPs"—high-value wholesales who haven't ordered in 60+ days but historically represent significant revenue.
*   **Strategic Value**: Triggers proactive re-engagement alerts before the relationship churns.

---

## 🛠️ Technology Stack
*   **Workflow Orchestration**: n8n (Desktop/Docker).
*   **Backend / Middleware**: Python (Flask, Pandas, SQLite3).
*   **Database**: SQLite (Serverless SQL Warehouse).
*   **Intelligence Layer**: LLM Model (via OpenRouter).
*   **Infrastructure**: Docker & Docker Compose.

---

## 📁 Repository Structure
```text
├── data_bridge.py          # Flask REST API connecting n8n to SQLite
├── init_warehouse.py       # Data migration and indexing script
├── docker-compose.yml      # Container orchestration blueprint
├── Dataset_Details         # Official variable data dictionary
├── Important_Concepts.md   # Technical supplement for interview preparation
└── README.md               # Project overview and documentation
```

---

## 🚀 Quick Start

1.  **Initialize the Warehouse**:
    ```bash
    python init_warehouse.py
    ```
2.  **Start the Infrastructure**:
    ```bash
    docker-compose up -d
    ```
3.  **Run the Data Bridge**:
    ```bash
    python data_bridge.py
    ```
4.  **Import Workflows**: Import the provided `.json` workflow files into your n8n instance.

---

## 📖 Data Source
This project utilizes the **Online Retail Dataset** (541,909 transactions) from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail).

---
*Developed as a high-impact Technical Showcase for Data Analyst & Analytics Engineering roles.*
