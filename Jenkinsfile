pipeline {
    agent any
    environment {
        SONAR_TOKEN = credentials('sonar-token')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/prudhviraj310/crm-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests & Generate Coverage') {
            steps {
                sh 'pytest --cov=app --cov-report=xml'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                    sonar-scanner \
                      -Dsonar.projectKey=fastapi-backend \
                      -Dsonar.sources=app \
                      -Dsonar.python.coverage.reportPaths=coverage.xml \
                      -Dsonar.host.url=http://13.218.166.232:9000 \
                      -Dsonar.login=$SONAR_TOKEN
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // your deployment step here
            }
        }
    }
}
