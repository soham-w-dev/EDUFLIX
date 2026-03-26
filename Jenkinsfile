pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t eduflix-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker stop eduflix-container || exit 0'
                bat 'docker rm eduflix-container || exit 0'
            }
        }

        stage('Run New Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name eduflix-container eduflix-app'
            }
        }
    }
}