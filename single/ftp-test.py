import ftplib

# initialize the FTP library
ftp = ftplib.FTP()

# define the target FTP server's host and port
ftp_server_host = "localhost"
ftp_server_port = 2121

# connect to the ftp server
ftp.connect(ftp_server_host, ftp_server_port)

# define the username and password for authenticating with the FTP server
ftp_server_username = "username"
ftp_server_password = "password"

# authenticate with the username and password
ftp.login(ftp_server_username, ftp_server_password)

# define the relative path of the sample file
file_path = "../samples/sample.pdf"

# create a reference to the file to be uploaded
target_file = open(file_path, "rb")

# define the STOR command to run on the FTP server
ftp_stor_command = "STOR ftp-server/sample.pdf"

# run the STOR command to upload the file to the server
ftp.storbinary(ftp_stor_command, target_file)

# close the file and ftp instance once done
target_file.close()
ftp.quit()