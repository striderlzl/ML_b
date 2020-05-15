# CarmaCam scoring module platform
a website, ML pipline integrated with YOLO v3, kalman-filter, OpenALPR and a couple of ML models to process video data, detect traffic violations.
only webiste source code
# Tehnique
- Django
- Tensorflow

# How to use

### Acquire data
upload traffic violation possibly video, choose the model (yolo or tracking)you want to use and get the data json file.

### Calculate violation possibilities
- [x] speeding
- [x] stop sign
- [ ] traffic light
- [ ] unsafe lane change

# Step by Step
### Home page - login
![alt text](img/LOGIN.png)

### Select a possible traffic violation video
![alt text](img/1-speedingvideo.png)

### Upload video
![alt text](img/2-speedingvideouploading.png)

### video is processing on the backend service and will take few minutes to calculate
![alt text](img/3-speedingvideouploaded.png)

### result!!!
![alt text](img/DATA.png)

### stop_sign(do work in video game GTA V and real life video)
![alt text](img/stopsign_gta.png)
![alt text](img/speeding.png)

# TODO
- [x] upload video
- [ ] connect to CarmaCam db
- [x] connect to ML model
- [x] add openalpr into backend
...
