# flask-app-xray
Sample Python Flask application with AWS X-Ray tracing

### Dependencies
- flask
- requests
- aws-xray-sdk

### Buliding to ECR
1. Create an ECR repository

2. Get ECR credentials for docker
```sh
AWS_REGION="us-east-1"  # Change as needed
AWS_ACCOUNT_ID="123456789"
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
```

3. Bulid image
```sh
ECR_REPOSITORY_NAME="flask-xray-sample"
docker build -t $ECR_REPOSITORY_NAME .
```

4. Tag and push to ECR
```sh
docker tag $ECR_REPOSITORY_NAME:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY_NAME:latest
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY_NAME:latest
```