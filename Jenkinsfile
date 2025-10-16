// The 'pipeline' block is the main wrapper for the entire process.
pipeline {
    // 'agent any' means this pipeline can run on any available Jenkins agent.
    agent any

    // 'environment' block defines variables that will be available to all stages.
    environment {
        // IMPORTANT: Replace 'YOUR_DOCKERHUB_USERNAME' with your actual Docker Hub username.
        DOCKERHUB_USERNAME = "parthagre"
        // We'll create a unique image name using the username and the Jenkins build number.
        DOCKER_IMAGE_NAME = "${DOCKERHUB_USERNAME}/cicd-assignment:${env.BUILD_NUMBER}"
    }

    // 'stages' contains the sequence of all the major tasks in our pipeline.
    stages {
        
        // --- STAGE 1: CHECKOUT ---
        stage('Checkout Code') {
            steps {
                echo "Cloning the repository..."
                // --- FIX IS HERE ---
                // We've added branch: 'main' to be explicit.
                git branch: 'main', url: 'https://github.com/ParthAgre/cicd-assignment.git'
            }
        }

        // --- STAGE 2: BUILD ---
        stage('Build Docker Image') {
            steps {
                echo "Building the Docker image: ${DOCKER_IMAGE_NAME}"
                // The 'sh' step executes a shell command. Here, we build the Docker image.
                sh "docker build -t ${DOCKER_IMAGE_NAME} ."
            }
        }

        // --- STAGE 3: TEST ---
        stage('Run Automated Tests') {
            steps {
                echo "Running tests inside a new container..."
                // We run a temporary container from the image we just built
                // and execute our tests inside it. If tests fail, the pipeline stops here.
                sh "docker run --rm ${DOCKER_IMAGE_NAME} pytest"
            }
        }

        // --- STAGE 4: PUSH ARTIFACT ---
        stage('Push Image to Docker Hub') {
            steps {
                echo "Pushing ${DOCKER_IMAGE_NAME} to Docker Hub..."
                // This 'withCredentials' block securely loads the credentials we will set up in Jenkins.
                // It makes them available as environment variables (DOCKER_USER, DOCKER_PASS).
                // IMPORTANT: 'dockerhub-creds' is the ID we will give our credentials in Jenkins.
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    sh "docker push ${DOCKER_IMAGE_NAME}"
                }
            }
        }
        
        // --- STAGE 5: DEPLOY (Placeholder) ---
        stage('Deploy') {
            steps {
                echo "Deployment step is a placeholder for this assignment."
                echo "In a real-world scenario, you would have a script here to deploy"
                echo "${DOCKER_IMAGE_NAME} to a cloud server."
            }
        }
    }
}
