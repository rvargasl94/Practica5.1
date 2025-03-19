pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Especificamos la rama correcta (main)
                git branch: 'main', url: 'https://github.com/rvargasl94/Practica5.1.git'
            }
        }

        stage('Pruebas Unitarias') {
            steps {
                sh 'python -m unittest test_calculator.py'
            }
        }
    }

    post {
        success {
            echo '¡La canalización se completó exitosamente!'
        }
        failure {
            echo 'La canalización falló. Revisa los logs para más detalles.'
        }
    }
}
