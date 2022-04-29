#!/usr/bien/env groovy
node {
    stage('Checkout'){
        checkout scm
    }
    stage('Setup'){
        sh "pip install -r requirements.txt"
    }
}