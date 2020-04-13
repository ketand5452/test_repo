# Imports
from azure.storage.blob import (
    BlockBlobService
)
import os

# Read environment variables
instanceId = str(os.environ['instanceId'])
accountName = str(os.environ['accountName'])
accountKey = str(os.environ['accountKey'])
containerName = str(os.environ['containerName'])
file_name = str(os.environ['file_name'])

print("Provided Input File Name is - "+str(file_name))

# Initialize blob
blobService = BlockBlobService(account_name=accountName, account_key=accountKey)

# Get the list with the matching file names
content = blobService.list_blobs(containerName)
blob_list=[]
for blob in content:
        name = blob.name
        if name == file_name:
                blob_list.append(blob.name)
print("Following filenames will be get deleted after successfull execution.")
print(blob_list)

# Delete one-by-one file by looping over a list
for file_to_delete in blob_list:
	blobService.delete_blob(containerName, file_to_delete, snapshot=None)
	print("File "+str(file_to_delete)+" deleted successfully.")
