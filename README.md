# AWS Lambda scaling demo

Before December 2023, AWS Lambda’s scaling was at the account level, scaling by up to 500-3000 concurrent executions in the first minute (depending on Region), followed by 500 concurrent executions every minute afterwards. 

Lambda functions now scale up at a 12x faster rate. Each function can scale up to a rate of 1,000 concurrent executions every 10 seconds, up to your account concurrency limit. Scaling is more granular, per individual Lambda functions. This benefits workloads that need to absorb traffic fluctuations, all without affecting the scaling rate of any other functions in your account.

## Demo
The demo deploys a Lambda function fronted by an Amazon API Gateway HTTP API.

Use [hey](https://github.com/rakyll/hey) to send load to the API to invoke the function.

The function sleeps for 10 seconds to simulate processing, allowing Lambda to create new execution environments.

> There are costs associated with running this demo!
> 
> It invokes 9 million Lambda functions!

Build and deploy the function using [AWS Serverless Application Model](https://aws.amazon.com/serverless/sam).

```
sam build
```
Deploy the function and API.
```
sam deploy -g
```

Use hey to generate traffic.
This simulates `-c` 10000 workers with a `-q` rate limit of 1 and runs for `-z` 900 seconds (15 minutes)
```
./hey -c 10000 -q 1 -z 900s https://<http_api>.execute-api.<Region>.amazonaws.com  
```

