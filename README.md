# flask-app-xray
Sample Python Flask application with AWS X-Ray tracing

### Dependencies
- flask
- requests
- aws-xray-sdk

### Buliding to ECR
1. Create an ECR repository
```sh
# Change to appropriate values
ECR_REPOSITORY_NAME="flask-xray-sample-app"
AWS_REGION="us-east-1"
AWS_ACCOUNT_ID="123456789"

aws ecr create-repository --repository-name $ECR_REPOSITORY_NAME --region $AWS_REGION
```

2. Get ECR credentials for docker
```sh
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
```

3. Bulid, tag, and push image to ECR
```sh
docker build -t $ECR_REPOSITORY_NAME .
docker tag ${ECR_REPOSITORY_NAME}:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/${ECR_REPOSITORY_NAME}:latest
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/${ECR_REPOSITORY_NAME}:latest
```