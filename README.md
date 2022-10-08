# mysql-selfmanaged

Question 1: What cloud environment you decided to use?

Answer: The Cloud Service that is utilized is Google Cloud Processing

How you set up your VM (what image you selected - imagine writing a brief tutorial to a new user - what would you include and how to quickly and easily set up a new VM)?


The Virtual Machine Configuration is Series E2 & Machine type: e2-small (2 vCPU,2 GB memory) 
OS is Ubuntu 18.04 LTS x86/64,amd64

The commands you used to setup the OS image (how did you update the OS image? how did you install the mysql?


What changes you needed to make in order to make the mysql instance available to external computers (config file? opening ports?)

mysql -u [UserName] -p

An example dataset that you have found (selected) to insert into the mysql database (provide the sqlalchemy/python code used to upload/insert the data) [there is no limitations, min/max of what I am looking for here] ---- REMINDER: in your python file, you will likely have to provide credentials, please use a .ENV file to load credentials so you do not hard-code the passwords/usernames into your github repo] [example python file for connecting/creating: https://colab.research.google.com/drive/1MPkNpvwzJgjcQ2fE8AUSOltPt6FtGvRB?usp=sharing] 
