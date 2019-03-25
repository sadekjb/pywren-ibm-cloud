### First build new image from the Dockerfile (link)
### for prepared docker image use:
	sadek/pywren-sj:3.6
### Add stubs and config folder to pywren directory
### run deploy_runtime script:
	./deploy_runtime create <repository>/<name>
### create action:
	wsk action update -i <action-name> --docker <image> -m 512 -t 300000 ./ibmcf_pywren.zip
