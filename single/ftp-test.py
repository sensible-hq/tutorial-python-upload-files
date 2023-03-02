import ftplib

# initialize the FTP library
ftp = ftplib.FTP()

# connect to the ftp server
ftp.connect("localhost", 2121)

# authenticate with the username and password
ftp.login("username", "password")

# create a reference to the file to be uploaded
target_file = open("../samples/sample.pdf", "rb")

# run the STOR command to upload the file to the server
ftp.storbinary("STOR ftp-server/sample.pdf", target_file)

# close the file and ftp instance once done
target_file.close()
ftp.quit()