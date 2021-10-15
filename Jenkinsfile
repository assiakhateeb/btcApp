node {

    checkout scm

    docker.withRegistry('https://hub.docker.com/u/assiakhateeb', 'dockerHub') {

        def customImage = docker.build("dockerapp/btc")

        /* Push the container to the custom Registry */
        customImage.push()
    }
}
