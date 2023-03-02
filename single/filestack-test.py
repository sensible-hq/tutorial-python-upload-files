from filestack import Client

# create the Filestack client with the API key
client = Client("<Your API Key Here>")

# upload the file
new_filelink = client.upload(filepath="../samples/sample.pdf")

# print the URL of the file once uploaded
print(new_filelink.url)