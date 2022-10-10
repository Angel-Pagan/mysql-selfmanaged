# mysql-selfmanaged

Question 1: What cloud environment you decided to use?

Answer: The Cloud Service that is utilized is Google Cloud Processing

How you set up your VM (what image you selected - imagine writing a brief tutorial to a new user - what would you include and how to quickly and easily set up a new VM)?

Step 1: Setting Up Virtual Machine:

#Create Virtual Machine (Google Cloud)
Hover mouse over Compute engine > Click VM Instance > Create Instance

#Settings of the Virtual Machine  
The Virtual Machine Configuration is Series E2 & Machine type: e2-small (2 vCPU,2 GB memory) [Minimum Specs]
OS is Ubuntu 18.04 LTS x86/64,amd64
Allow HTTP & HTTPS in the Firewall Settings 


The commands you used to setup the OS image (how did you update the OS image? how did you install the mysql?


What changes you needed to make in order to make the mysql instance available to external computers (config file? opening ports?)

#User name Login Command
mysql -u [UserName] -p


