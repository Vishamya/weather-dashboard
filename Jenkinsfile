pipeline {
    agent any

    // Parameters allow dynamic values at build time
    parameters {
        string(name: 'GIT_REPO', defaultValue: 'https://github.com/Vishamya/weather-dashboard.git', description: 'Git repository URL')
        string(name: 'GIT_BRANCH', defaultValue: 'main', description: 'Git branch to build')
        string(name: 'EC2_HOST', defaultValue: '23.22.106.217', description: 'Public IP of EC2 to deploy')
        string(name: 'IMAGE', defaultValue: 'weather-dashboard', description: 'Docker image name')
        string(name: 'AWS_REGION', defaultValue: 'us-east-1', description: 'AWS region')
        string(name: 'AWS_ACCOUNT_ID', defaultValue: '514015377403', description: 'AWS Account ID')
    }

    environment {
        TAG = "${env.BUILD_NUMBER}"
        EC2_USER = "ec2-user"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: "${params.GIT_BRANCH}", url: "${params.GIT_REPO}", credentialsId: 'github-access'
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'docker run --rm -v $WORKSPACE:/app -w /app python:3.11-slim bash -c "pip install -r requirements.txt && pytest -q"'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${params.IMAGE}:${TAG} ."
            }
        }

        stage('AWS Login & Push Docker Image') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'AWS Credentials']]) {
                    sh """
                        aws ecr get-login-password --region ${params.AWS_REGION} | \
                        docker login --username AWS --password-stdin ${params.AWS_ACCOUNT_I
