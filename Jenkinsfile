pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'echo "================<Build stage>=================="'
                sh 'echo "Test Text" >> app.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'echo "================<Test stage>=================="'
                sh '''
                if [ -f "app.txt" ]; then
                    echo "File app.txt exists!!!"
                else
                    echo "The file dose not exist!!!"
                    exit 1
                fi
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "================<Deploy stage>=================="'
                sh 'mkdir deploy'
                sh 'cp app.txt ./deploy'
            }
        }
    }

    post {
        always {
            sh 'echo "Cleaning up..."'
            deleteDir()
        }
    }
}