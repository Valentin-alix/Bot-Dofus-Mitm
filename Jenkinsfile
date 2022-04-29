#!/usr/bien/env groovy
node {
    stage('Checkout'){
        steps {
            checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'cb9df461-f2e0-4d16-84da-880e1a9618e5', url: 'https://gitlab.com/Valentin-alix/bot_mitm']]])
        }
    }
    stage('Build'){
        steps {
            bat 'pip -r install requirements.txt'
        }
    }
    stage('Test'){
        steps {
            echo 'et la les tests'
        }
    }
}