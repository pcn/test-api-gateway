# Test using AWS API gateway with IAM authentication for https requests


Scenario: start up an el-cheapo t4g.micro instance in the test org's infra-test account,
and see if setting up the API gateway per 

https://medium.com/trackit/using-api-gateway-rest-as-a-proxy-for-on-premise-web-services-69c3ca3ad578

Instead of site-to-site etc., let's just use an ALB to provide access to the service
