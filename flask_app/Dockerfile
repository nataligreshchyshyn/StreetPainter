FROM python:3.9

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN apt-get update
RUN apt-get install -y libgdal-dev
RUN pip install GDAL==3.2.2.1
RUN pip install -r requirements.txt


# Bundle app source
COPY . .

EXPOSE 5000
CMD [ "flask","run","--host","0.0.0.0","--port","5000"]
