import requests

# create a reference to the file
target_file = open("../samples/sample.pdf", "rb")

# store the target API URL
target_url = "https://httpbin.org/post"

# send the request
response = requests.post(target_url, files = {"form_field_name": target_file})

# check the result
if response.ok:
    print("Upload complete")
    print(response.text)
else:
    print("Something went wrong")