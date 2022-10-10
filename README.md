# mysql-selfmanaged


# Creating and Setting Up Virtual Machine:

#Create Virtual Machine (Google Cloud)

Hover mouse over Compute engine > Click VM Instance > Create Instance

#Settings of the Virtual Machine  

The Virtual Machine Configuration is Series E2 & Machine type: e2-small (2 vCPU,2 GB memory) [Minimum Specs]

OS is Ubuntu 18.04 LTS x86/64,amd64

Allow HTTP & HTTPS in the Firewall Settings 

Click on the 'Blue' Create button in the bottom left of the screen

# Update Virtual Machine OS and Install MySQL

To Update OS use command " sudo apt-get update "

To Install MySQL use command " sudo apt install mysql-server mysql-client "

# ADD USERS AND Configure Users

To enter mySQL as admin use command " sudo mysql "

To Create a User use command " CREATE USER '[NAME OF USER]'@'[IP ADDRESS]' IDENTIFIED BY '[USER PASSWORD]'

To Add Security Attributes use command " GRANT ALL PRIVILEGES ON *.* TO '[USERNAME]'@'[IP ADDRESS]' WITH GRANT OPTIONS

# User name Login Command

mysql -u [UserName] -p

[Enter Password]

# Configuring IP ADDRESS to allow inbound connections to VM mySQL

to modify mySQL special configurations file enter "sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf"

Modify the bound ip address value to " 0.0.0.0"

Press Control+O (save changes) and press Control +x (to exit nano)

for changes to take effect restart mySQL by using command " sudo /etc/init.d/mysql restart"

Changes should have taken effect and now allow inbound connections





