pipeline {
  agent any
  stages {
    stage('stage1') {
      steps {
        echo 'hey dreygos how u doin?'
      }
    }

    stage('stage2') {
      steps {
        sh '''mkdir -p build
echo "This is the release ${BUILD_NUMBER}" > build/release.txt'''
      }
    }

  }
  environment {
    foo = 'bar'
  }
}