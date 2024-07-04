# MSDS-434 Week 3 Assignment

This is a toy project as part of the [MSDS-434 Data Science and Cloud Computing](https://sps.northwestern.edu/masters/data-science/program-courses.php?course_id=5011) program.

We are supposed to create a toy web app and then host it using Amazon EC2 and Elastic Beanstalk, and then also host it on GCP GAE and GCP Cloud.

## Instructions:

### Amazon EC2 Instance

```
# Launch an EC2 instance the way you normally do.  Get yourself into the terminal
# Note at some point you need to edit the security rules to allow inbound traffic
# - In instance, go to Security --> Security Groups link --> Edit inbound rules
# - Type: All Traffic, Source: Anywhere-IPv4
# - Type: All Traffic, Source: Anywhere-IPv6
sudo apt update
sudo apt-get install git
git clone https://github.com/weswest/msds434wk3
cd msds434wk3
sudo snap install docker
sudo docker build -t flask-dynamic-chart .
sudo docker run -p 8080:8080 flask-dynamic-chart
# Grab the dns from the instance terminal and make sure you go to http://, not https://
```

### Amazon Elastic Beanstalk

1. Zip your project files into a zipfile
2. In Amazon do a search for IAM
    2a. Create a new AWS Service for EC2 role
    2b. In role uses, search for AWSElasticBeanstalk
    2c. Select the three that end in WebTier, WorkerTier, MulticontainerDocker
    2d. Name the role something familiar
3. Do a search for Elastic Beanstalk and then...
    3a. Create a new application.  Web server environment with a Docker platform
    3b. Upload your zipped files
    3c. Accept all other defaults
4. Load everything up.  Wait for the instance to fully start up
5. Click on the domain and you should be taken to the website in working order


### 