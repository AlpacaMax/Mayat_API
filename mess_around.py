from zipfile import ZipFile

SCRATCH_DIR = "scratch"

with ZipFile("scratch/zip_file_cbf12dc1-a117-49df-8f10-cc5511f8ae24.zip", 'r') as f:
    f.extractall("scratch/zip_file_cbf12dc1-a117-49df-8f10-cc5511f8ae24")