import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_data(data):
    logger.info("Validating data")
    # Add your validation logic here
    return True

def extract_data():
    try:
        logger.info("Extracting data from source")
    except Exception as e:
        logger.error(f"Error in extraction: {e}")

def transform_data():
    try:
        logger.info("Transforming data")
    except Exception as e:
        logger.error(f"Error in transformation: {e}")

def load_data():
    try:
        logger.info("Loading data to destination")
    except Exception as e:
        logger.error(f"Error in loading: {e}")

def main():
    logger.info("Starting ETL pipeline")
    extract_data()
    transform_data()
    load_data()
    logger.info("ETL pipeline completed")

if __name__ == "__main__":
    main()