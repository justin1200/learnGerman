#Deriving the latest base image
FROM python:latest

#Labels as key value pair
LABEL Maintainer="j.kelley"

#Set working directory
WORKDIR /usr/app/src

#Move files into container
COPY csv ./csv
COPY game ./game
COPY menu ./menu
COPY gameControl.py ./
COPY global_constants.py ./
COPY main.py ./

#Run learnGerman upon starting container
ENTRYPOINT [ "python", "./main.py" ]
