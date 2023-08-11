from filestack import Client

# define the Filestack API key
FILESTACK_API_KEY = "<Your API Key Here>"

# create the Filestack client with the API key
client = Client(FILESTACK_API_KEY)

# define the relative path of the sample file
file_path = "../samples/sample.pdf"

# upload the file
new_filelink = client.upload(filepath=file_path)

# print the URL of the file once uploaded
print(new_filelink.url)