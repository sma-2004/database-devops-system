pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Backup Script') {
            steps {
                sh 'python backup/backup.py'
            }
        }

        stage('Run Monitoring') {
            steps {
                sh 'python monitoring/monitor.py &'
            }
        }
    }
}