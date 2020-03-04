pipeline {
    agent { node { label 'docker' } }

    environment {
        NEXUS_URL=""
        APP_NAME=""
    }

    stages {
        stage('Build docker image') {
            steps {
                sh "docker image build -t ${env.NEXUS_URL}/${env.APP_NAME}:latest ."
            }
        }
        stage('Build docker push') {
            steps {
                sh "docker image push ${env.NEXUS_URL}/${env.APP_NAME}:latest"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
