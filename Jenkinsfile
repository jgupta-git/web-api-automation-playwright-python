pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                bat '''
                    python -m venv .venv
                    call .venv\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                    python -m playwright install chromium
                '''
            }
        }
        stage('Test') {
            steps {
                bat '''
                    call .venv\\Scripts\\activate.bat
                    python -m pytest --junitxml=report.xml
                '''
            }
        }
    }
    post {
        always {
            junit allowEmptyResults: true, testResults: 'report.xml'
            archiveArtifacts artifacts: 'downloads/**', allowEmptyArchive: true
        }
    }
}