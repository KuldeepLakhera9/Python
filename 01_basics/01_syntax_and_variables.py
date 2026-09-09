"""
01_basics / 01_syntax_and_variables.py
---------------------------------------
Basic Python concepts for Data Engineering:
- Variables & Dynamic Typing
- Basic Data Types (int, float, str, bool)
- Print statements & string formatting
"""

def main():
    print("=== Python for Data Engineering: Fundamentals ===")
    
    # 1. Variables & Types
    pipeline_name = "ETL_Sales_Daily"
    records_processed = 150500
    success_rate = 99.85
    is_active = True
    
    print(f"Pipeline Name     : {pipeline_name} (Type: {type(pipeline_name).__name__})")
    print(f"Records Processed : {records_processed} (Type: {type(records_processed).__name__})")
    print(f"Success Rate      : {success_rate}% (Type: {type(success_rate).__name__})")
    print(f"Pipeline Active   : {is_active} (Type: {type(is_active).__name__})")
    
    # 2. String Formatting (f-strings)
    summary = f"Summary: Pipeline '{pipeline_name}' completed with {records_processed:,} records."
    print("\n" + summary)
    
    # 3. Simple ASCII Output
    print("\nData Flow Visualizer:")
    print("   [Source DB] ---> (ETL Pipeline) ---> [Data Warehouse]")

if __name__ == "__main__":
    main()
