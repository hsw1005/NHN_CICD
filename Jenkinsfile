pipeline{
    agent any
    //agent {
    //    docker{
    //        image "gradle:jdk8"
    //        registryUrl "https://hub.docker.com/"
    //        registryCredentialsId "docker_hub_credentials"
    //    }
    //}
    
    environment{
        DOCKER_HUB = "https://hub.docker.com/"
        IMAGE_NAME = "hamsw1005/hsw_nhn_cloud" + ":" + "${env.TAG}"
        DOCKER_HUB_CREDENTIALS = "hamsw1005"
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
        stage("Dockerize"){
            steps{
                script{
                    docker.withRegistry(env.DOCKER_HUB, env.DOCKER_HUB_CREDENTIALS){
                        def dockerImage = docker.build(env.IMAGE_NAME, '-f ./Dockerfile .')
                    docker.push()
                    }
                }
            }
        }
        
    }
}
