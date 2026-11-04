pipeline {
    agent any

    options {
        timestamps()
    }

    stages {

        stage('Build') {
            steps {
                echo 'Building Python application'
                sh 'python3 --version'
                sh 'python3 -m py_compile hello.py test_hello.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests'
                sh 'python3 -m unittest discover -s . -p "test_*.py" -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application'

                sh '''
                    mkdir -p /tmp/bigdata-cicd-deployment
                    cp hello.py /tmp/bigdata-cicd-deployment/
                    python3 /tmp/bigdata-cicd-deployment/hello.py
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed. Check the console output.'
        }
    }
}
