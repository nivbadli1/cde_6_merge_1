def extract_data():
    try:
        print("Extracting data from source")
    except Exception as e:
        print(f"Error in extraction: {e}")

def transform_data():
    try:
        print("Transforming data")
    except Exception as e:
        print(f"Error in transformation: {e}")

def load_data():
    try:
        print("Loading data to destination")
    except Exception as e:
        print(f"Error in loading: {e}")

def main():
    extract_data()
    transform_data()
    load_data()

if __name__ == "__main__":
    main()