
# This is a sample Dockerfile you can modify to deploy your own app based on face_recognition

FROM python:3.6-slim-stretch


WORKDIR /app

COPY requirements.txt ./



RUN apt-get update

RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    libxcb-xinerama0 \
    libopenblas-dev \
    liblapack-dev \
    libgl1-mesa-glx \
    libx11-dev \
    libgtk2.0-dev\
    libgtk-3-dev \
    pkg-config \
    python3 \
    python3-dev\
    python3-pip \
    python3-numpy \
    python3-opencv \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*




RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .


EXPOSE 5000

CMD [ "python3", "./main.py" ]



#docker build -t hawkeye-api:latest .
#docker run -p 5000:5000 hawkeye-api:latest
#sudo docker run -p 5000:80 hawkeye-api  


#heroku container:login
#heroku container:push web
#heroku git:remote -a your_app_name
#heroku run -a app
#heroku container:release web 