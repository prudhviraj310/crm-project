pipeline {
    agent any

    environment {
        SONARQUBE_SCANNER_HOME = tool 'SonarQubeScanner'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/prudhviraj310/crm-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('My SonarQube Server') {
                    sh "${env.SONARQUBE_SCANNER_HOME}/bin/sonar-scanner"
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
