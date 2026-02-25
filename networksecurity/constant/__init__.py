# from networksecurity.constant.training_pipeline import (
#     DATA_INGESTION_COLLECTION_NAME, 
#     DATA_INGESTION_DATABASE_NAME,
#     DATA_INGESTION_DIR_NAME,
#     DATA_INGESTION_FEATURE_STORE_DIR,
#     DATA_INGESTION_INGESTED_DIR,
#     DATA_INGESTION_TRAIN_TEST_SPLIT_RATION,
#     DATA_VALIDATION_DIR_NAME,
#     DATA_VALIDATION_VALID_DIR,
#     DATA_VALIDATION_INVALID_DIR,

#     DATA_VALIDATION_DRIFT_REPORT_DIR,
#     DATA_VALIDATION_DRIFT_REPORT_FILE_NAME,
#     DATA_TRANSFORMATION_DIR_NAME,
#     DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
#     DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
#     DATA_TRANSFORMATION_IMPUTER_PARAMS,
#     DATA_TRANSFORMATION_TRAIN_FILE_PATH,
#     DATA_TRANSFORMATION_TEST_FILE_PATH
#     )

# _all__ = [
#     "DATA_INGESTION_COLLECTION_NAME",
#     "DATA_INGESTION_DATABASE_NAME",
#     "DATA_INGESTION_DIR_NAME",
#     "DATA_INGESTION_FEATURE_STORE_DIR",
#     "DATA_INGESTION_INGESTED_DIR",
#     "DATA_INGESTION_TRAIN_TEST_SPLIT_RATION",
#     "DATA_VALIDATION_DIR_NAME",
#     "DATA_VALIDATION_VALID_DIR",
#     "DATA_VALIDATION_INVALID_DIR",
#     "DATA_VALIDATION_DRIFT_REPORT_DIR",
#     "DATA_VALIDATION_DRIFT_REPORT_FILE_NAME",
#     "DATA_TRANSFORMATION_DIR_NAME",
#     "DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR",
#     "DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR",
#     "DATA_TRANSFORMATION_IMPUTER_PARAMS",
#     "DATA_TRANSFORMATION_TRAIN_FILE_PATH",
#     "DATA_TRANSFORMATION_TEST_FILE_PATH"
# ]


# import os

# # Get the project root directory
# PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# # Create absolute path to schema file
# # SCHEMA_FILE_PATH = os.path.join(PROJECT_ROOT, "data_schema", "schema.yaml")


# import os

# # Get to project root (3 levels up from constant/__init__.py)
# # constant/__init__.py -> constant -> networksecurity -> Network_Security
# PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# # Build path to schema.yaml at project root
# SCHEMA_FILE_PATH = os.path.join(PROJECT_ROOT, "data_schema", "schema.yaml")

# # Verify the path (you can remove this print after testing)
# print(f"SCHEMA_FILE_PATH: {SCHEMA_FILE_PATH}")