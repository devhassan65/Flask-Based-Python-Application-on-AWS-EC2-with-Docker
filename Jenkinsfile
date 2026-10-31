
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'hassanzia65/flask-app'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/devhassan65/Flask-Based-Python-Application-on-AWS-EC2-with-Docker.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Test Application') {
            steps {
                sh '''
                    .venv/bin/python -m py_compile app.py
                    echo "Python syntax check passed!"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t $DOCKER_IMAGE:$IMAGE_TAG .
                    docker tag $DOCKER_IMAGE:$IMAGE_TAG $DOCKER_IMAGE:latest
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'Dockerhub_cred',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_TOKEN'
                    )
                ]) {
                    sh '''
                        echo "$DOCKER_TOKEN" | docker login \
                            -u "$DOCKER_USER" --password-stdin

                        docker push $DOCKER_IMAGE:$IMAGE_TAG
                        docker push $DOCKER_IMAGE:latest

                        docker logout
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Docker image pushed to Docker Hub!'
        }

        failure {
            echo 'FAILED: Check Jenkins Console Output.'
        }
    }
}



