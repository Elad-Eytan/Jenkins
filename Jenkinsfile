pipeline {
    agent any

    environment {
        APP_VERSION = '1.0'
        APP_NAME    = 'EladApp'
        DOCKER_REPO = 'vocvoc1'
        FILE_TO_TEST = "${env.WORKSPACE}/app.txt"
        BUILD_FILE_PATH = "${env.WORKSPACE}/build-info.txt"
    }

    stages {
        stage('Build') {
            steps {
                sh 'echo "================<Build stage>=================="'
                sh 'echo "Test Text 123456 LALILOLELO" >> app.txt'
                sh 'echo "The App version is ${APP_VERSION}"'
                sh 'echo "The App name is ${APP_NAME}"'
                sh 'echo "The Docker repo is ${DOCKER_REPO}"'
                sh 'touch build-info.txt'
                sh '''
                   echo "The App version is ${APP_VERSION}" >> build-info.txt
                   echo "The Build number is $BUILD_NUMBER" >> build-info.txt
                   echo "The Date is $(date)" >> build-info.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh 'echo "================<Test stage>=================="'
                sh 'echo "The Pipeline name is $JOB_NAME"'
                sh 'echo "The Build number is $BUILD_NUMBER"'
                parallel{
                    stage('File Stage'){
                        sh '''
                            if [ -f "app.txt" ]; then
                                echo "File app.txt exists!!!"
                            else
                                echo "The file dose not exist!!!"
                                exit 1
                            fi
                           '''
                    }
                    stage('Build Info Stage'){
                        sh 'python3 test.py "$BUILD_FILE_PATH" "Build"'
                    }
                }
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