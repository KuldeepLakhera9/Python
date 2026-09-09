# 🐍 Python for Data Engineering

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Focus](https://img.shields.io/badge/Focus-Data%20Engineering-FF6F00?style=for-the-badge&logo=apache-airflow&logoColor=white)](#-learning-roadmap)
[![Repository](https://img.shields.io/badge/GitHub-KuldeepLakhera9%2FPython-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/KuldeepLakhera9/Python)
[![License](https://img.shields.io/badge/License-MIT-4CAF50?style=for-the-badge)](#-license)

> Welcome to **Python for Data Engineering**! This repository serves as a structured learning journey, hands-on codebase, and reference guide focused on mastering Python specifically for building scalable data pipelines, ETL/ELT workflows, data transformations, and database integrations.

---

## 🎯 Objectives

- 💡 **Master Core Python**: Write clean, efficient, and pythonic code optimized for data processing.
- 📁 **Data Format Manipulation**: Seamlessly handle CSV, JSON, Parquet, Avro, and XML files.
- 🐼 **Data Transformation**: Perform high-performance data manipulation using **Pandas**, **Polars**, and **NumPy**.
- 🗄️ **Database Integration**: Connect Python with SQL databases (PostgreSQL, MySQL, SQLite) using **SQLAlchemy** and **psycopg2**.
- ⚡ **Big Data & Distributed Computing**: Learn the fundamentals of **PySpark** and distributed DataFrames.
- 🛠️ **Production Pipeline Patterns**: Implement error handling, logging, generators, and modular ETL architecture.

---

## 🗺️ Learning Roadmap & Syllabus

| Module | Topic | Core Concepts | Status |
| :--- | :--- | :--- | :---: |
| **01** | [Python Fundamentals](./01_basics/) | Syntax, Variables, Control Flow, f-strings | 🟡 *In Progress* |
| **02** | [Data Structures & Algorithms](./02_data_structures/) | Lists, Dicts, Sets, Tuples, Comprehensions | ⏳ *Planned* |
| **03** | [Modular Python & Scripting](./03_functions_and_modules/) | Functions, Decorators, Generators, Modules | ⏳ *Planned* |
| **04** | [Object-Oriented Programming](./04_oop/) | Classes, Inheritance, Dataclasses, Pydantic | ⏳ *Planned* |
| **05** | [File Handling & Formats](./05_file_handling/) | CSV, JSON, Parquet, Avro, Streaming File I/O | ⏳ *Planned* |
| **06** | [Data Manipulation (Pandas/Polars)](./06_data_processing/) | DataFrames, Aggregations, Merges, Polars | ⏳ *Planned* |
| **07** | [Database Integration & SQL](./07_database_and_sql/) | SQLite, PostgreSQL, SQLAlchemy, Bulk Loading | ⏳ *Planned* |
| **08** | [ETL Pipelines & PySpark](./08_data_pipelines_etl/) | API Ingestion, Distributed Data, PySpark | ⏳ *Planned* |

---

## 📂 Repository Structure

```text
.
├── 01_basics/                  # Python fundamentals & control flow
│   └── 01_syntax_and_variables.py
├── 02_data_structures/         # Lists, Dictionaries, Sets, Tuples & Comprehensions
│   └── README.md
├── 03_functions_and_modules/   # Functions, Generators, Decorators & Modular Code
│   └── README.md
├── 04_oop/                     # OOP principles, Dataclasses & Data Validation
│   └── README.md
├── 05_file_handling/           # CSV, JSON, Parquet, Avro & Memory-efficient I/O
│   └── README.md
├── 06_data_processing/         # Pandas, Polars & NumPy transformations
│   └── README.md
├── 07_database_and_sql/        # SQL connectivity, SQLAlchemy & DB operations
│   └── README.md
├── 08_data_pipelines_etl/      # End-to-end ETL scripts, API ingestion & PySpark
│   └── README.md
├── app.py                      # Main entry point & scratch test runner
├── .gitignore                  # Python & DE file exclusion rules
└── README.md                   # Repository overview & documentation
```

---

## 🚀 Quickstart Guide

### 1. Clone the Repository
```bash
git clone https://github.com/KuldeepLakhera9/Python.git
cd Python
```

### 2. Set Up Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv .venv

# Activate environment (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Activate environment (Linux / macOS)
source .venv/bin/activate
```

### 3. Run a Sample Script
```bash
python 01_basics/01_syntax_and_variables.py
```

---

## 💻 Sample Code Pattern: Basic ETL Pipeline

```python
import json

def extract_raw_data(file_path: str) -> list[dict]:
    """Extract raw records from JSON source."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def transform_records(records: list[dict]) -> list[dict]:
    """Clean and transform data records."""
    return [
        {
            "user_id": item["id"],
            "email": item["email"].strip().lower(),
            "is_active": item.get("status") == "ACTIVE"
        }
        for item in records
        if "email" in item
    ]

def load_data(transformed_data: list[dict]):
    """Load transformed data into target destination."""
    print(f"Successfully loaded {len(transformed_data)} records into Data Warehouse.")
```

---

## 👤 Author

**Kuldeep Lakhera**
- GitHub: [@KuldeepLakhera9](https://github.com/KuldeepLakhera9)
- Domain: **Data Engineering & Python Ecosystem**

---

## 📜 License

This project is licensed under the [MIT License](LICENSE) - free to use, modify, and distribute for learning purposes.
