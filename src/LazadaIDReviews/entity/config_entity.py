from dataclasses import dataclass
from pathlib import Path

# NOTE: 'frozen=True' in dataclass decorator
# means you can't add any new functionality

@dataclass(frozen=True)
class DataIngestionSQLConfig:
    root_dir: Path
    source_URI: str
    reviews_table: str
    reviews_path: Path
    items_table: str
    items_path: Path
    category_table: str
    category_path: Path

@dataclass(frozen=True)
class DataDumpConfig:
    root_dir: Path
    reviews_path: Path
    input_train_path: Path
    input_test_path: Path
    output_train_path: Path
    output_test_path: Path
    params_test_size: float

@dataclass(frozen=True)
class DataPreprocessingConfig:
    root_dir: Path
    input_train_path: Path
    input_test_path: Path
    vectorized_train_path: Path
    vectorized_test_path: Path
    model_dir: Path
    vectorizer_model_path: Path

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    input_train_path: Path
    output_train_path: Path
    vectorized_train_path: Path
    model_path: Path
    params_max_iter: int
    params_solver: str
    params_n_jobs: int

@dataclass(frozen=True)
class TrainEvaluationConfig:
    root_dir: Path
    input_train_path: Path
    input_test_path: Path
    output_train_path: Path
    output_test_path: Path
    vectorized_train_path: Path
    vectorized_test_path: Path
    vectorizer_model_path: Path
    model_path: Path
    score_path: Path
    mlflow_dataset_path: Path
    mlflow_dataset_column: list
    minio_endpoint_url: str
    minio_access_key_id: str
    minio_secret_access_key: str
    mlflow_tracking_uri: str
    mlflow_exp_name: str
    mlflow_dataset_bucket: str
    mlflow_run_name: str

@dataclass(frozen=True)
class PredictionConfig:
    root_dir: Path
    mlflow_tracking_uri: str
    mlflow_model_name: Path
    mlflow_deploy_model_alias: Path
    mlflow_vectorizer_model_path: Path

@dataclass(frozen=True)
class UnitTestConfig:
    root_dir: Path
    mlflow_tracking_uri: str
    mlflow_model_name: str
    mlflow_deploy_model_alias: Path
    mlflow_input_example_path: Path
    app_endpoint: str