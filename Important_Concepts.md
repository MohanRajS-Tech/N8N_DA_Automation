# 🧠 Shield Project: Important Concepts for Interviews

This document is your "Cheat Sheet" for explaining the high-level engineering decisions made in this project. Use these concepts to demonstrate **Senior-level thinking**.

---

## 1. The 3-Pillar Architecture 🏛️
Instead of a messy script, we built a **Modular System**. 

| Pillar | Component | Role | ELI5 |
| :--- | :--- | :--- | :--- |
| **Pillar 1** | **The Warehouse** (SQLite) | Data Integrity | A robust filing cabinet that holds 541k records safely. |
| **Pillar 2** | **The Manager** (n8n) | Orchestration | The "Brain" that decides when to check data and who to tell. |
| **Pillar 3** | **The Brain** (LLM Model) | Strategic Analysis | The "Expert" who reads the data and gives business advice. |

---

## 2. Microservices Architecture 🏗️
**Concept:** Breaking one big, heavy app into small, specialized "workers."

*   **Our Implementation:** We have a separate **Data Bridge** (Python) and a separate **Orchestrator** (n8n).
*   **ELI5:** Instead of one person trying to cook and clean simultaneously, we have a **Chef** and a **Cleaner** in different rooms talking through a window.
*   **Why it's Pro:** If n8n crashes, your data bridge is still safe. If you want to change your database, you only change the bridge, not the whole n8n setup. This is called **Decoupling**.

---

## 3. Docker & Docker Compose 🐳
**Concept:** "Packaging" your software so it runs exactly the same on every computer.

*   **Docker:** A container (a "bubble") that holds n8n and all its dependencies.
*   **Docker Compose:** The **Blueprint** for the whole office. It tells Docker which containers to start, which ports to open, and where to save the data.
*   **Interview Tip:** "I used Docker Compose to ensure local environment parity, making the entire orchestration layer portable and reproducible with a single command."

---

## 4. The "Data Bridge" (REST API) 🌉
**Concept:** Connecting two different systems using the "Language of the Internet" (HTTP).

*   **How it works:** n8n sends an **HTTP POST** request to your Python script. The script runs the SQL and sends back **JSON**.
*   **Why we did it:** This solved the "Docker Isolation" problem. Since n8n is in a container, it can't "see" your Windows files. The bridge acts as a **Connector**.
*   **Keywords:** RESTful API, JSON Payload, 200 OK Response, 415 Error (Media Type mismatch).

---

## 5. SQLite vs. PostgreSQL 📦
*   **ELI5:** SQLite is a **Notebook** (a single file). PostgreSQL is a **Library** (a complex server).
*   **Pro Decision:** We chose SQLite because it is "Serverless" and "Zero-Configuration." For a POC with 500k rows, it provides massive performance with zero overhead.

---

## 6. ACID Compliance 🛡️
**Concept:** Guaranteeing that your data never gets corrupted.
*   **A**tomic: Transactions are "all or nothing."
*   **C**onsistency: Data follows strict rules.
*   **I**solation: Multiple queries don't trip over each other.
*   **D**urability: Once saved, it's safe even if the power goes out.

---

---

## 7. Concentration Risk Analysis (The "Pareto" Principle) 🎯
**Concept:** Identifying if a problem is systemic or isolated.
*   **Our Implementation:** We check the `UniqueCustomers` count for returned items.
*   **ELI5:** If 100 people return a shirt, the shirt is bad (**Systemic**). If 1 person returns 100 shirts, the person is the problem (**Isolated**).
*   **Strategic Value:** Tells the CEO whether to fire a supplier or renegotiate a customer contract.

---

## 8. RFM Analysis (Customer Health) 👑
**Concept:** A powerful marketing framework used to understand customer value.
*   **R**ecency: When was the last order? (Lower is better).
*   **F**requency: How often do they buy? (Higher is better).
*   **M**onetary: How much do they spend? (Higher is better).
*   **Our Implementation:** Identified "Fading Giants"—VIPs with high Monetary value but high Recency (Silent for 60+ days).

---

## 9. Decision-Driven Analytics (DDA) 🧠
**Concept:** Starting with the **Decision** the stakeholder needs to make, not the data.
*   **The Framework:** Instead of saying "Here is a list of returns," we say "Here is the story behind the leak and the strategic move you need to take."
*   **Storytelling:** Using metaphors like "The Isolated Fracture" or "The Fading Giant" to drive executive action.

---

> [!TIP]
> **The "Golden Sentence" for your Resume:** 
> "Architected an autonomous Dual-Pillar AI Shield system (Revenue Shield & VIP Shield) that uses RFM analysis and storytelling to detect £100k+ revenue leakage and customer churn risks in a 541k+ row retail warehouse."

