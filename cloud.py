from google.cloud import storage
def create_bucket_class_location(bucket_name):

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "COLDLINE"
    bucket.location = "US"
    new_bucket = storage_client.create_bucket(bucket)

    print("Created bucket {} in {} with storage class {}".format(new_bucket.name, new_bucket.location, new_bucket.storage_class))
    return new_bucket

def download_blob(bucket_name, source_blob_name, destination_file_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(f"Downloaded {source_blob_name} to {destination_file_name}.")
    
def upload_blop(bucket_name,file_name,blob_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_name)
    print(f"File {file_name} uploaded to {bucket_name}/{blob_name}.")


file_name="downloaded.csv"
blob_name = "final_dataset-fee/tution_fee_dataset.csv"
bucket_name = "omerdenemebucket"

download_blob(bucket_name,blob_name,file_name)
# create_bucket_class_location(bucket_name)

