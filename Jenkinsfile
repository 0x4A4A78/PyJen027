pipeline {
    agent any
    triggers { pollSCM('* * * * *') }
    options { timestamps(); disableConcurrentBuilds() }
    stages {
        stage('Build') {
            steps { bat 'python build.py' }
        }
        stage('Test') {
            steps { bat 'python -m unittest discover -v' }
        }
        stage('Deploy') {
            steps { bat 'python deploy.py' }
        }
    }
    post {
        success { archiveArtifacts artifacts: 'dist/calculator.py', fingerprint: true }
    }
}
