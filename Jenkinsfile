pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        APP_NAME = "service-health-api"
        IMAGE_TAG = "v3"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                  docker build \
                    -t ${APP_NAME}:${IMAGE_TAG} \
                    -f docker/app/Dockerfile .
                """
            }
        }

        stage('Verify Image') {
            steps {
                sh "docker images | grep ${APP_NAME}"
            }
        }
    }

    post {
        success {
            echo "CI SUCCESS: Image ${APP_NAME}:${IMAGE_TAG} built successfully"
        }
        failure {
            echo "CI FAILURE: Docker build failed"
        }
    }
}
