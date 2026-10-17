pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                bat '''
                    "C:\\Users\\jigya\\AppData\\Local\\Python\\pythoncore-3.15-64\\python.exe" -m venv .venv
                    call .venv\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                    python -m pip install pytest-html
                    python -m playwright install chromium
                '''
            }
        }
        stage('Test') {
            steps {
                bat '''
                    call .venv\\Scripts\\activate.bat
                    python -m pytest --junitxml=report.xml --html=report.html --self-contained-html --tracing=on --screenshot=on
                '''
            }
        }
    }
    post {
        always {
            junit allowEmptyResults: true, testResults: 'report.xml'
            archiveArtifacts artifacts: 'report.html, test-results/**, downloads/**', allowEmptyArchive: true
        }
    }
}