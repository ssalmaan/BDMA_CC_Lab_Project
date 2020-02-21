## Questions:

**Q611: What happens when you use https://your-load-balancer-url instead of http://your-load-balancer-url ? Why does that happen? How could you fix it?**
 **Your connection is not private** window starts to show up. This happened as we upload a free certificate from the free website **(http://www.selfsignedcertificate.com/)**. This is insecure and can be a security vulnerability. This can be fixed by buying verified certificates from certificate providers to configure our website.

**Q612. Stop all three EC2 instances and wait aprox. 5 minutes. What happens? Why?**
 Two new instances were created and started running after 5 minutes. After stopping the instances, Health check signal cannot be detected by the image. As it is configured every 300s so, they were considered to be dead. Due to Auto scaling configuration for the instances, the 2 new instances were created automatically to replace the stopped instances.

**Q613. Terminate all three EC2 instances and wait aprox. 5 minutes. What happens? Why?**
 Again two new instances were created and started running automatically. The AMI image for apache-web-server will provide the configuration settings for creating and initialising the new instances after terminating the old ones.

**Q614. How are you going to end this section regarding the use of AWS resources?**
 To end this section, we first have to deregister the AMI we created. We also have to delete the load balancer and the auto scaling group created. We also need to terminate all existing EC2 instances to prevent new instances being created due to Auto-scaling.

**Q615. Create a piece of code (Python or bash) to reproduce the above steps required to launch a new set of web servers with a load balancer. Start using the AMI that you have already created.**

**Q621. What is the list of events that the above URL triggers?**
{"Items": [], "Count": 0, "ScannedCount": 0, "ResponseMetadata": {"RequestId": "CDKSLBA04CMEEM341P0C9S8NN3VV4KQNSO5AEMVJF66Q9ASUAAJG", "HTTPStatusCode": 200, "HTTPHeaders": {"server": "Server", "date": "Fri, 11 Apr 2019 14:38:00 GMT", "content-type": "application/x-amz-json-1.0", "content-length": "39", "connection": "keep-alive", "x-amzn-requestid": "CDKSLBA04CMEEM341P0C9S8NN3VV4KQNSO5AEMVJF66Q9ASUAAJG", "x-amz-crc32": "3413411624"}, "RetryAttempts": 0}}

**Q622. Does the reply of the above URL match what it should be expected? Why?**
The reply of the above URL is as expected. Note that the Items value is an empty list as the table is currently empty. It also lists metadata for the table.

**Q623. Explain what happens (actions and parts activated) when you type the URL in your browser to obtain the page updated with the shopping list.**
The items from the "shopping-list" table are displayed on typing the URL in the browser. This is achieved through a call to the API Gateway Get method.

**Q624. Explain what happens (actions and parts activated) when you type a new item in the New Thing box.**
The new item is added to the tabe in the **ThingId** column. This is achieved through a call to the API Gateway Post method.

**Q625. Have you been able to debug the code of the Lambda function? If the answer is yes, check that you are using the root API keys. Erase such keys and create a new testing user with the required permissions.**
Yes, we were able to debug the code. We were using the root API keys.

**Q626. What are the minimum permissions that the user's API keys needs to execute the Lambda function locally?**
For log streaming, your function needs access to Amazon CloudWatch Logs.
To insert items and access items, it needs access to the dynamodb table.
