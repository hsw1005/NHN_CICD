pipeline{
    agent any
    
    // environment{
    //
    // }
    
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
//         stage("Git Clone"){
//             steps{
//                 git url: "https://github.com/hsw1005/CICD_Test.git",
//                 branch: "main",
//                 credentialsId: "github_credentials"
                
//                 sh 'ls -alh'
//             }
//         }
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
//         stage("Dockerize"){
//             steps{
//                 docker.withRegistry()
//             }
//         }
        
    }
}
