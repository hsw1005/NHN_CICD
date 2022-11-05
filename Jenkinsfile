pipeline{
    agent any
    
    environment{
        DOCKER_HUB = "https://hub.docker.com/"
        IMAGE_NAME = "hamsw1005/hsw_nhn_cloud" + ":" + "${env.TAG}"
        DOCKER_HUB_CREDENTIALS = credentials("docker_hub_credentials")
    }
    
    stages{
        stage("pre-stage, version check"){
            steps{
                cleanWs()
                sh 'pwd'
                sh 'java -version'
                sh 'gradle -v'
                sh 'whoami'
                sh 'pwd'
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
        stage("Dockerize"){
            steps{
                docker.withRegistry(DOCKER_HUB, DOCKER_HUB_CREDENTIALS){
                    def dockerImage = docker.build(IMAGE_NAME, '-f ./Dockerfile ./')
                    docker.push()
                }
            }
        }
        
    }
}
