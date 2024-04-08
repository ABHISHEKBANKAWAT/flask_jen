pipeline {
    agent any

    environment {
        VENV_PATH = 'myprojectenv'
    }

    stages {
        stage('Prepare and Install dependencies') {
            steps {
                script {
                    // Check for the virtual environment, create it if it doesn't exist
                    // Activate the virtual environment and install dependencies
                    sh '''
                    python3 -m venv $VENV_PATH
                    source $VENV_PATH/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Run tests and Deploy') {
            steps {
                // Assuming tests and deployment are managed here. Replace echo with actual commands.
                echo "Assuming tests and deployment steps are run here. Please replace this with actual test commands and deployment logic."
                // Example for tests: pytest
                // Example for deployment: sh "./delivery.sh"
            }
        }
    }
    post {
        always {
            echo 'Build completed.'
            // Clean up if required. This is optional as the environment deactivates automatically.
            // sh "rm -rf $VENV_PATH"
        }
    }
}
