pipeline{
    //agent any
    agent {
        docker{
            image "gradle:jdk8"
            args "-u root:root -v /var/run/docker.sock:/var/run/docker.sock"
            registryUrl "https://index.docker.io/"
            registryCredentialsId "docker_hub_credentials"
        }
    }
    
    environment{
        DOCKER_HUB = 'https://index.docker.io/v1/' //'https://hub.docker.com/'
        IMAGE_NAME = "hamsw1005/hsw_nhn_cloud" + ":" + "${env.TAG}"
        DOCKER_HUB_CREDENTIALS = 'docker_hub_credentials' //system domain credentials
    }
    
    stages{
        stage("pre-stage, version check"){
            steps{
                cleanWs()
                sh 'pwd'
                sh 'java -version'
                sh 'gradle -v'
                
                echo "Image Name is : ${IMAGE_NAME}"
            }
         }
        stage("Git Clone"){
            steps{
                git url: "https://github.com/hsw1005/NHN_CICD.git",
                branch: "main",
                credentialsId: "github_credentials"
                
                sh 'ls -alh'
            }
        }
        stage("Gradle Build"){
            steps{
                script{
                    try{
                        sh 'gradle build'
                    }
                    catch(e){
                        echo 'Gradle Build Stage Failed!'
                    }
                }
                sh 'ls -alh'
            }
        }
        stage("Dockerize & Push"){
            steps{
                script{
                    docker.withRegistry(DOCKER_HUB, DOCKER_HUB_CREDENTIALS){
                        def dockerImage = docker.build(IMAGE_NAME, '-f ./Dockerfile .')
                        dockerImage.push(env.TAG)
                    }
                }
            }
        }
        
    }
}
