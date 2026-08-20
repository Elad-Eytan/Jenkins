pipeline {
    agent any

    environment {
        APP_VERSION     = '1.0'
        APP_NAME        = 'EladApp'
        DOCKER_REPO     = 'vocvoc1/'
        FILE_TO_TEST    = "${env.WORKSPACE}/app.txt"
        BUILD_FILE_PATH = "${env.WORKSPACE}/build-info.txt"
    }

    stages {
        stage('Build') {
            steps {
                sh 'echo "================<Build stage>=================="'

                sh 'echo "Test Text 123456 LALILOLELO" > app.txt'

                sh 'echo "The App version is $APP_VERSION"'
                sh 'echo "The App name is $APP_NAME"'
                sh 'echo "The Docker repo is $DOCKER_REPO"'

                sh '''
                    echo "The App version is $APP_VERSION" > build-info.txt
                    echo "The Build number is $BUILD_NUMBER" >> build-info.txt
                    echo "The Date is $(date)" >> build-info.txt
                '''
            }
        }

        stage('Test') {
            parallel {
                stage('File Stage') {
                    steps {
                        sh 'echo "================<File Test>=================="'
                        sh 'echo "The pipeline name is $JOB_NAME"'
                        sh 'echo "The build number is $BUILD_NUMBER"'

                        sh '''
                            if [ -f "$FILE_TO_TEST" ]; then
                                echo "File $FILE_TO_TEST exists!"
                            else
                                echo "The file does not exist!"
                                exit 1
                            fi
                        '''
                    }
                }

                stage('Build Info Stage') {
                    steps {
                        sh 'python3 test.py "$BUILD_FILE_PATH" "Build"'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "================<Deploy stage>=================="'
                sh 'mkdir -p deploy'
                sh 'cp app.txt deploy/'
            }
        }
    }

    post {
        always {
            sh 'echo "Cleaning up..."'
            cleanWs()
        }
    }
}