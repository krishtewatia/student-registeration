
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Automated Tests') {
            steps {
                echo 'Testing the student registration form...'
                bat 'python test_form.py'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All registration form tests passed.'
        }
        failure {
            echo 'FAILURE: Registration form tests failed.'
        }
        always {
            echo 'Pipeline execution completed.'
        }
    }
}
