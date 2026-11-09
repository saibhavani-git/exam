pipeline{
    agent any
    stages {
        stage('Build'){
            steps{
                echo 'Building Docker image...'
                bat 'docker build -t registration-app .'
            }
        }
        stage('Run'){
            steps{
                echo 'Running Docker container...'
                bat 'docker rm -f registration-container || exit 0'
                bat 'docker run -d -p 5000:5000 --name registration-container registration-app'

            }
        }
    }
    post{
        success{
            echo 'Pipeline completed successfully.'
        }
        failure{
            echo 'Pipeline failed.' 
        }
    }
}
