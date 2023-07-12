app_name="docker-flask-app"
 
docker build -t ${app_name} .
 
docker run --rm -it -p 80:5000 --name=${app_name} -v $PWD:/app ${app_name}