from zipfile import ZipFile

SCRATCH_DIR = "scratch"

with ZipFile("scratch/zip_file_f91ef4b7-a2ee-4422-84e2-be18e6e8b41f.zip", 'r') as f:
    f.extractall("scratch/zip_file_f91ef4b7-a2ee-4422-84e2-be18e6e8b41f")