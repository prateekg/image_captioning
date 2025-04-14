# image_captioning


## hosting the service inside docker, run it from inside git repo folder
docker build -t captioning-app .
docker run -p 8000:8000 captioning-app


## making inferences
curl -X POST http://localhost:8000/generate_caption/ \
  -F "file=@sample.jpg"