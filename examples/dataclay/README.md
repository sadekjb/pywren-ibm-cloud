## PyWren runtime creation with DataClay support
Create PyWren runtime action with DataClay APIs suuport, and support for the specific model and session information for the specific user
### Building an image with dataclay support: [Dockerfile](../../runtime/Dockerfile)
#### Build the image by these [instructions]( ../../runtime/README.md)
#### For pre-built docker image use:
	sadek/pywren-sj:3.6
### Adding application data (model and config) to OpenWhisk runtime
#### Model registration and stubs generation example:
	dClayTool.sh NewModel HelloCarsPythonUser pys3cr3tp4ssw0rd Cars_ns13 cars_model python
dClayTool.sh GetStubs HelloCarsPythonUser pys3cr3tp4ssw0rd Cars_ns13 cars_stubs
#### Add stubs and config folder to pywren directory
#### Deploy runtime by these [instructions]( ../../runtime/README.md) getting ibmcf_pywren.zip file
### create action:
	wsk action update -i <action-name> --docker <image> -m 512 -t 300000 ./ibmcf_pywren.zip
