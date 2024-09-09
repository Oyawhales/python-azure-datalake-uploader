# Managing Azure Data Lake with Python and Azure SDK

## Overview

This project demonstrates data ingestion into Azure Data Lake using the Azure SDK and Python. It covers the use of key Azure SDK components like DataLakeServiceClient, FileSystemClient, DataLakeDirectoryClient, and DataLakeFileClient.The project uses **environment variables** to handle sensitive data such as storage account names and SAS tokens.

By following this guide, you’ll have a fully functional Python-based solution to interact with Azure Data Lake, making it easier to organize and upload your data to the cloud.

---

## Prerequisites

Before you begin, make sure you have the following:

1. **Azure Subscription**: You'll need an Azure account with a storage account created and **Azure Data Lake Storage** enabled.
2. **Python 3.7+**: Ensure Python is installed on your system.
3. **SAS Token**: Generate a **Shared Access Signature (SAS)** token to securely access Azure Data Lake.
4. **Azure Portal Access**: Familiarize yourself with the Azure portal for managing your storage resources.

---

## Project Structure

Here’s a breakdown of the important files in this repository:

├── Azure_file_upload.py         # Main Python script to interact with Azure Data Lake

├── .env                         # Environment variables (not shared publicly)

├── README.md                    # Project documentation

├── requirements.txt             # Python dependencies

└── Data.csv                     # Sample data file for uploading


---

## Key Azure SDK Components Used

1. **DataLakeServiceClient**: Connects to Azure Data Lake Storage and allows interaction with the account.
2. **FileSystemClient**: Manages file systems (sometimes called containers) within Azure Data Lake Storage.
3. **DataLakeDirectoryClient**: Manages directories within a file system in the Data Lake.
4. **DataLakeFileClient**: Handles file operations such as uploading, downloading, and deleting files in Azure Data Lake.

---

## Setup Instructions

### Step 1: Clone the Repository

Start by cloning this repository:

git clone https://github.com/Oyawhales/python-azure-datalake-uploader.git

cd python-azure-datalake-uploader


### Step 2: Set Up a Virtual Environment
Set up a virtual environment for the project to isolate dependencies:

![Set Up a Virtual Environment](./Img/1%20create%20ve.png)

### Step 3: Install Required Python Packages
Install the necessary Python packages using pip:

![Python Package](./Img/2%20Python%20package.png)

 ### Step 4 Configuration
 1. To securely manage sensitive information, create a .env file in the root directory with the following values:
 
![env opened](./Img/env%20file%20opened.png)

2. Generate a SAS Token
. In the Azure portal, follow these steps:
. Navigate to your storage account.
. Select Shared Access Signature.
. Set the required permissions (such as Read, Write, Create, and List).
. Generate and copy the SAS token, then add it to the .env file.

### Step 5 Running the Script
Once everything is set up, run the Python script to interact with Azure Data Lake:

![upload](./Img/final%20file%20upload.png)


## Technical Walkthrough

1. Connecting to Azure Data Lake Storage
The script uses DataLakeServiceClient to establish a connection to the Azure Data Lake account using the provided SAS token:

![connecting](./Img/6%20Datalakeserviceclient.png)

2. Creating and Managing File Systems
The FileSystemClient is used to interact with file systems. The script checks if the specified file system exists, and creates it if necessary:

![file system](./Img/7%20create%20file%20.png)

3. Managing Directories
The DataLakeDirectoryClient is responsible for managing directories. The script will create a new directory or retrieve an existing one:

![create directory](./Img/8%20create%20directory.png)

4. Uploading Files to Azure Data Lake
Finally, the DataLakeFileClient is used to upload a file to the specified directory in Azure Data Lake Storage:

![upload](./Img/9%20Upload.png)


## Screenshots and Results
Below are some visual representations of the results from running the script:

SAS Token Generated:
![sas](./Img/B%20generate%20sas%20token.png)

File System and Directory Managed:
![upload](./Img/C%20container%20created%20.png)

![upload](./Img/D%20directory%20created%20.png)

File Uploaded:
![upload](./Img/E%20data%20loaded%20.png)









