#!/usr/bin/env python3
import boto3
import sys
from datetime import datetime
import os

def upload_to_s3(backup_dir, bucket_name, s3_folder):
    try:
        s3 = boto3.client('s3')
        date_str = datetime.now().strftime("%Y%m%d")
        backup_file = f"backup_{date_str}.sql.gz"
        local_path = os.path.join(backup_dir, backup_file)
        s3_path = f"{s3_folder.rstrip('/')}/{backup_file}"
        
        # Check if file exists
        if not os.path.exists(local_path):
            print(f"Error: Backup file {local_path} not found")
            sys.exit(1)
            
        # Upload to S3
        s3.upload_file(local_path, bucket_name, s3_path)
        print(f"Successfully uploaded {backup_file} to s3://{bucket_name}/{s3_path}")
        
    except Exception as e:
        print(f"Error uploading to S3: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: upload_backup_to_s3.py <backup_dir> <bucket_name> <s3_folder>")
        print("Example: upload_backup_to_s3.py /path/to/backups my-bucket bucket-folder")
        sys.exit(1)
        
    backup_dir = sys.argv[1]
    bucket_name = sys.argv[2]
    s3_folder = sys.argv[3]
    upload_to_s3(backup_dir, bucket_name, s3_folder)