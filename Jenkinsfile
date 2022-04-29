#!/usr/bien/env groovy
node {
    stage('Checkout'){
        checkout scm
    }
    stage('Build')
    {
        agent {
            docker {
                image 'python:3.9.12-alpine3.14'
            }
        }
    }
    stage('Setup'){
        sh "pip install -r requirements.txt"
    }
}