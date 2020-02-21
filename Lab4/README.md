# Questions:
Q45a: What has happened? Why do you think that has happened?
    
1. When we terminated the EC2 Instance, the health feature stop sending metrics to the elastic beanstalk. The status every time went from green to red. Later, a new instance is created and added to the beanstalk.

Q45b: What has happened? Why do you think that has happened? Check both EC2 and EB consoles. Add your responses to README.md.

1. All the instances from EC3 are terminated. Due to this, buckets got deleted and the environment was terminated. 
	 
Q45c: Can you terminate the application using the command line? What is the command? if it exists.

Yes, we can terminate the application using the following command `aws elasticbeanstalk delete-application --application-name gsg-signup --terminate-env-by-force`.In our case, it did not work. So, we terminated the environment of the application from the command line and we used the command `eb terminate`.


Q45d: What parameters have you added to the eb create command to create your environment? Explain why you have selected each parameter.

We added the following parameter for instance profile and key `--instance_profile gsg-signup-role -keyname gs-new` for running it correctly through command line.
And also we added the following parameter to update service role `--service-role aws-elasticbeanstalk-service-role`
	
Complete command :
eb create --instance_profile gsg-signup-role --keyname gs-new --envvars DEBUG=True,STARTUP_SIGNUP_TABLE=gsg-signup-table,AWS_REGION=eu-west-1 --service-role aws-elasticbeanstalk-service-role



Q46: How long have you been working on this session? What have been the main difficulties you have faced and how have you solved them? 

It took 7 hours for us to complete this lab exercise.
Main difficulties faced where:
1. In the beginning the python environment didn't have sqlite installed. 
2. Searching the right configuration for each step took a lot of time.
3. Also the cli command for creating the env didn't work for us.