# Importing necessary modules and classes for Azure authentication and storage interaction.
from azure.identity import ClientSecretCredential
from azure.core.exceptions import ResourceExistsError  # Exception for checking if a resource already exists.

import os  # For interacting with environment variables and file paths.
from dotenv import load_dotenv  # For loading environment variables from a .env file.

# Importing classes from the Azure Data Lake SDK to interact with Data Lake.
from azure.storage.filedatalake import (
    DataLakeServiceClient,      # Client to interact with the Azure Data Lake service.
    DataLakeDirectoryClient,    # Client to interact with directories within the Data Lake.
    FileSystemClient,           # Client to interact with file systems (containers) within the Data Lake.
    DataLakeFileClient          # Client to interact with files within the directories.
)
from azure.core.exceptions import ResourceExistsError  # Exception for checking if a resource already exists.

# Get the current working directory (local path where the script is running).
local_path = os.getcwd()

# Load environment variables from the .env file.
load_dotenv()

# Fetching necessary Azure Data Lake details from environment variables.
account_name = os.getenv("ACCOUNT_NAME")  # The name of the Azure Data Lake storage account.
container_name = os.getenv("CONTAINER_NAME")  # The name of the container (file system) within the storage account.
directory_name = os.getenv("DIRECTORY_NAME")  # The name of the directory inside the container where the file will be uploaded.
sas_token = os.getenv('SAS_TOKEN')  # The Shared Access Signature (SAS) token for authentication.

# Function to get the DataLakeServiceClient using the account name and SAS token.
def get_service_client_sas(account_name: str, sas_token: str) -> DataLakeServiceClient:
    # Create the service client to connect to Azure Data Lake Storage using the account URL and SAS token.
    account_url = f"https://{account_name}.dfs.core.windows.net"
    service_client = DataLakeServiceClient(account_url, credential=sas_token)
    return service_client

# Attempt to connect to the Azure Data Lake storage account.
try:
    print("About to connect to the storage account")
    # Initialize the DataLakeServiceClient using the account name and SAS token.
    service_client: DataLakeServiceClient = get_service_client_sas(account_name, sas_token=sas_token)
    print("Successfully connected to the storage account")
except Exception as e:
    # Handle and print any errors encountered during the connection attempt.
    print(f"Error connecting to the service account: {e}")


# Function to create a file system (container) in Azure Data Lake if it doesn't already exist.
def create_file_system(service_client: DataLakeServiceClient, file_system_name: str) -> FileSystemClient:
    try:
        print(f"Attempting to create file system (container): {file_system_name}")
        # Create a new file system (container) in the Azure Data Lake storage account.
        file_system_client = service_client.create_file_system(file_system=file_system_name)
        print(f"File system (container) '{file_system_name}' created successfully.")
        return file_system_client
    except ResourceExistsError:
        # Handle the case where the file system already exists and retrieve it.
        print(f"File system (container) '{file_system_name}' already exists.")
        return service_client.get_file_system_client(file_system=file_system_name)
    except Exception as e:
        # Handle any other errors encountered during the file system creation.
        print(f"Error occurred while creating file system (container): {e}")
        raise

# Attempt to create the file system (container).
try:
    print("About to create the container")
    # Create or retrieve the file system (container) using the file system (container) name.
    file_system_client: FileSystemClient = create_file_system(service_client=service_client, file_system_name=container_name)
except Exception as e:
    # Handle any errors encountered during the file system creation.
    print(f"Error during container creation: {e}")


# Function to create a directory within the file system (container) in Azure Data Lake.
def create_directory(file_system_client: FileSystemClient, directory_name: str) -> DataLakeDirectoryClient:
    try:
        print(f"Attempting to create directory: {directory_name}")
        # Create a new directory in the specified file system.
        directory_client = file_system_client.create_directory(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
        return directory_client
    except ResourceExistsError:
        # Handle the case where the directory already exists and retrieve it.
        print(f"Directory '{directory_name}' already exists.")
        return file_system_client.get_directory_client(directory_name)
    except Exception as e:
        # Handle any other errors encountered during the directory creation.
        print(f"Error occurred while creating directory: {e}")
        raise

# Attempt to create the directory using the name from the environment variables.
try:
    print("About to create the directory")
    # Ensure the directory name is fetched correctly from environment variables.
    directory_name = os.getenv("DIRECTORY_NAME")  
    # Create or retrieve the directory within the file system.
    directory_client: DataLakeDirectoryClient = create_directory(file_system_client=file_system_client, directory_name=directory_name)
except Exception as e:
    # Handle any errors encountered during the directory creation.
    print(f"Error during directory creation: {e}")


# Function to upload a file to the directory in Azure Data Lake.
def upload_file_to_directory(directory_client, local_path: str, file_name: str):
    # Get the file client for the specified file within the directory.
    file_client = directory_client.get_file_client(file_name)

    # Open the file in binary read mode and upload it to the Azure Data Lake directory.
    with open(file=os.path.join(local_path, file_name), mode="rb") as data:
        file_client.upload_data(data, overwrite=True)  # Overwrite existing files if necessary.
    print(f"File '{file_name}' uploaded successfully to directory.")

# Define the local file path and file name to be uploaded.
local_path = "./"  # The path to the local directory where the file is located.
file_name = "Data.csv"  # The name of the file to be uploaded.

# First, get the file system (container) client from the service client.
file_system_client = service_client.get_file_system_client(file_system=container_name)

# Then, get the directory client from the file system client for the specified directory.
dir_client = file_system_client.get_directory_client(directory_name)

# Finally, upload the file to the specified directory in Azure Data Lake.
upload_file_to_directory(directory_client=dir_client, local_path=local_path, file_name=file_name)
