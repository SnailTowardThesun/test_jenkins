pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }

    post {
        success {
            cp main.py /home/hankun/main.py
        }
    }
}