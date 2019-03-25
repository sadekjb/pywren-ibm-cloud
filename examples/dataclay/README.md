### First build new image from the [Dockerfile] (../../runtime/Dockerfile)
### for prepared docker image use:
	sadek/pywren-sj:3.6
### Register model and generate stubs:
	dClayTool.sh NewModel HelloCarsPythonUser pys3cr3tp4ssw0rd Cars_ns13 cars_model python
	dClayTool.sh GetStubs HelloCarsPythonUser pys3cr3tp4ssw0rd Cars_ns13 cars_stubs
### Add stubs and config folder to pywren directory
### run deploy_runtime script:
	./deploy_runtime create <repository>/<name>
### create action:
	wsk action update -i <action-name> --docker <image> -m 512 -t 300000 ./ibmcf_pywren.zip
