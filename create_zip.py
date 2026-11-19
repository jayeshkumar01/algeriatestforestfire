#!/usr/bin/env python3
import os
import zipfile
import sys

def create_deployment_zip():
    files_to_include = [
        'application.py',
        '.ebextensions/',
        'templates/',
        'static/',
        'requirements.txt',
        'README.md',
        'Algerian_forest_fires_dataset_UPDATE.csv',
        'Algerian_forest_fires_cleaned_Dataset.csv',
        'algeriafireforest.ipynb',
        'ridge.pkl',
        'scaler.pkl',
        'classification_scaler.pkl',
        'decisioncv.pkl',
        '.gitignore'
    ]

    zip_path = 'algeriatestforestfire.zip'

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for item in files_to_include:
            if os.path.exists(item):
                if os.path.isdir(item):
                    for root, dirs, files in os.walk(item):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, '.')
                            zipf.write(file_path, arcname)
                else:
                    zipf.write(item, item)
            else:
                print(f"Warning: {item} not found")

    print(f"Created deployment package: {zip_path}")
    return zip_path

if __name__ == '__main__':
    create_deployment_zip()