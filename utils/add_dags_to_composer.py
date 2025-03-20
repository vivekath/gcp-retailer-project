import argparse
import glob
import os
import tempfile
from shutil import copytree, ignore_patterns
from google.cloud import storage

def _create_file_list(directory: str, name_replacement: str) -> tuple[str, list[str]]:
    """Copies relevant files to a temporary directory and returns the list."""
    temp_dir = tempfile.mkdtemp()
    files_to_ignore = ignore_patterns("__init__.py", "*_test.py")
    copytree(directory, f"{temp_dir}/", ignore=files_to_ignore, dirs_exist_ok=True)
    files = glob.glob(f"{temp_dir}/*.py") if "dags" in name_replacement else glob.glob(f"{temp_dir}/*")
    return temp_dir, files

def upload_to_composer(directory: str, bucket_name: str, name_replacement: str) -> None:
    """Uploads DAGs or Data files to Composer's Cloud Storage bucket."""
    temp_dir, files = _create_file_list(directory, name_replacement)

    if files:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)

        for file in files:
            file_gcs_path = file.replace(f"{temp_dir}/", name_replacement)

            try:
                blob = bucket.blob(file_gcs_path)
                blob.upload_from_filename(file)
                print(f"Uploaded {file} to gs://{bucket_name}/{file_gcs_path}")
            except FileNotFoundError:
                print(f"Error: {file} not found in {os.listdir()}. Check your directory structure.")
                raise
    else:
        print(f"No files found to upload from {directory}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload DAGs and data to Composer bucket.")
    parser.add_argument("--dags_directory", help="Path to DAGs directory.")
    parser.add_argument("--dags_bucket", help="GCS bucket name for DAGs.")
    parser.add_argument("--data_directory", help="Path to data directory.")

    args = parser.parse_args()

    if args.dags_directory:
        upload_to_composer(args.dags_directory, args.dags_bucket, "dags/")
    
    if args.data_directory:
        upload_to_composer(args.data_directory, args.dags_bucket, "data/")
