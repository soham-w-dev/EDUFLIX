pipeline {
    agent any

    stages {
        stage('Create Docker Network') {
            steps {
                bat 'docker network create eduflix-network || exit 0'
            }
        }

        stage('Run PostgreSQL Container') {
            steps {
                bat 'docker stop postgres-db || exit 0'
                bat 'docker rm postgres-db || exit 0'
                bat '''
                docker run -d ^
                --name postgres-db ^
                --network eduflix-network ^
                -e POSTGRES_USER=postgres ^
                -e POSTGRES_PASSWORD=admin ^
                -e POSTGRES_DB=STUDYFLIX ^
                -p 5432:5432 ^
                postgres
                '''
            }
        }

            stage('Wait for DB') {
                steps {
                    bat 'ping 127.0.0.1 -n 10 > nul'
                }
            }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t eduflix-app .'
            }
        }

        stage('Run Application Container') {
            steps {
                bat 'docker stop eduflix-container || exit 0'
                bat 'docker rm eduflix-container || exit 0'
                bat '''
                docker run -d ^
                --name eduflix-container ^
                --network eduflix-network ^
                -p 5000:5000 ^
                eduflix-app
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Application is running at http://localhost:5000"
        }
        failure {
            echo "❌ Pipeline failed. Check logs."
        }
    }
}