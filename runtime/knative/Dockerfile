FROM ibmfunctions/action-python-v3.6:master

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

ADD https://github.com/sadekjb/pywren-ibm-cloud/tree/kn-dev/pywren_ibm_cloud ./pywren_ibm_cloud

ADD https://github.com/sadekjb/pywren-ibm-cloud/tree/kn-dev/runtime/knative/app.py ./app.py

RUN pip install Flask gunicorn

# Run the web service on container startup.

ENV PORT 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
