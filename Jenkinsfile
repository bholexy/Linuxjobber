node {
        stage ('Checkout') {
            checkout scm

            sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
            def lastChanges = readFile('GIT_CHANGES') }

        

        stage ('Deploy') {
            
            sh 'chmod +x deploy.sh'
            sh 'whoami'
            sh 'bash ./deploy.sh'
        }
      }  