# base image  
FROM python:3.9.7
# setup environment variable  
ENV APPDIR=/webapp/  

# set work directory  
RUN mkdir -p $APPDIR  

# where your code lives  
WORKDIR $APPDIR  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
ENV DISABLE_COLLECTSTATIC 1

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . $APPDIR  
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs
EXPOSE 8000

RUN chmod +x ./entrypoint.sh

CMD ["./entrypoint.sh"]

# start server  
# ENTRYPOINT [ "gunicorn mysite.wsgi" ] 