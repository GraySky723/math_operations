pipeline {
    agent {
        docker {
            // 使用 Python 3.9-slim 镜像（可选，Python 版本不必和本地完全一致）
            image 'python:3.10-slim'
            // 如有需要可以挂载 Docker.sock（此例中主要用于安装依赖与测试）
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    stages {
        stage('Checkout') {
            steps {
                // checkout scm 会自动拉取在 Jenkins 任务配置中指定的 Git 仓库
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }
        stage('Run Application') {
            steps {
                sh 'python math_functions.py'
            }
        }
    }
}
