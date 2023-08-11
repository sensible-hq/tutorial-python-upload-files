import requests

target_file_1_path = "../samples/sample.pdf"
target_file_2_path = "../samples/sample-2.pdf"
target_file_3_path = "../samples/sample-3.pdf"
target_file_4_path = "../samples/sample-4.pdf"

# create references to the files to be uploaded
target_file_1 = open(target_file_1_path, "rb")
target_file_2 = open(target_file_2_path, "rb")
target_file_3 = open(target_file_3_path, "rb")
target_file_4 = open(target_file_4_path, "rb")

# create a dict object with the file objects
target_files = {
    "file-1": target_file_1,
    "file-2": target_file_2,
    "file-3": target_file_3,
    "file-4": target_file_4,
}

# define the target API URL
target_url = "https://httpbin.org/post"

# send the request
response = requests.post(target_url, files=target_files)

# check the result
if response.ok:
    print("Upload complete")
    print(response.text)
else:
    print("Something went wrong")