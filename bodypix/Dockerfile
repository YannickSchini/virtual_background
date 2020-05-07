# Base image with node
FROM node
# Install node package dependencies
WORKDIR /src
COPY package.json /src/
RUN npm install
# Setup our app as the entrypoint
COPY app.js /src/
ENTRYPOINT node /src/app.js
