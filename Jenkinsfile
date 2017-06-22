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
            sh 'echo "build success"'
            cp main.py /home/hankun/main.py
        }
    }
}