# [SBI - Image Document Optimization](https://www.techgig.com/hackathon/image-document-optimization)

## Scope of Work of the PoC

The POC curently is restricted to handling only 
    
    1. cropping and compressing for pdf 
    2. cropping/compressing/alignment witha  reference image for Images
    3. PDF's are restricted to NON-OCR pdfs but can be extended by writing a loigc to extract images from the OCR pdf and passing them as images to the code.
    4. PDF compressing uses Ghost script and is its required to be installed and present in path.


Features - 

    1. Automatically detects the margins and can crop a given percentage of them.
    2. Can crop all the pages to the same size to give a uniform appearance 
    3. Renders and analyzes page images to find the bounding boxes, which allows it to deal with noisy scanned PDFs.
    4. Can deal with at least simple cases of password-encrypted files.
    5. Can crop images with white background or scnaned images to reduce whitespace

Post POC Work - 

    1. Create a auto alignment detection for images using labelled data to use alignment without reference images and key feature matching algorithms
    2. Image cropping can be imporved by getting more better ROI and then aligning it using prepective tarnsformation opencv.

## Pre-requisites from the Bank’s side
1. Azure Account
2. Works with both CPU and GPU and would not need a specifc GPU right now
3. Setup & Deployment will not require more than a week.

## Infrastructure required for setting up the PoC. 
1. The Images can be uplaoded to a container storage and can be called using azure functions,
2. An Azure function to deploy this code and call it using REST API's.

## Setting up the PoC infrastructure on Microsoft Azure cloud setup
1. [Creating a resource Group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#create-resource-groups)
2. [Creating a storage account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal)
3. [Creating a container](https://docs.microsoft.com/en-us/azure/storage/blobs/blob-containers-cli#create-a-container)
4. [Creating a function app](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-function-app-portal#create-a-function-app)
5. [Deploy code in azure function](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-function-app-portal#create-function)
6. [Writing scipts to download and upload images to the azure function for processing in azure](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?tabs=environment-variable-windows#upload-blobs-to-a-container)


## High level PoC Key Performance Indicators (KPIs) 
Samples Processed are provide in the [sample_data](./sample_data/) directpry and Video of execution can be found [here](https://drive.google.com/file/d/1dpWAH5H_FHObzFMh_8nxP1sH8T46GXl0/view?usp=sharing)

## Deployment Guide
Local Deployment
1. [Ghostscript](https://www.ghostscript.com/doc/current/Install.htm)
2. [pdftoppm](https://poppler.freedesktop.org/)

```cmd
pip3 install vitualenv
virtualenv img_opt
source img_opt/bin/activate   
pip3 install -r requirements.txt
python process.py
```