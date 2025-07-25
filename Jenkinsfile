pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('sonar-token') // Add this as Secret Text in Jenkins Credentials
    }

    stages {
        stage('Build') {
            steps {
                echo '🔨 Building CRM project...'
                // You can add actual build steps here (e.g., pip install)
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running tests...'
                // You can add pytest or unit tests later
            }
        }

        stage('SonarQube Analysis') {
            steps {
                dir('backend') {
                    echo '🔍 Running SonarQube analysis...'
                    sh '''
                        sonar-scanner \
                        -Dsonar.projectKey=fastapi-backend \
                        -Dsonar.projectName="FastAPI Backend" \
                        -Dsonar.projectVersion=1.0 \
                        -Dsonar.sources=app \
                        -Dsonar.language=python \
                        -Dsonar.sourceEncoding=UTF-8 \
                        -Dsonar.exclusions=**/__pycache__/**,**/venv/** \
                        -Dsonar.host.url=http://13.218.166.232:9000 \
                        -Dsonar.login=$SONAR_TOKEN
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deploying to EC2...'
                // Add your SSH or deploy script here
            }
        }
    }
}
