FROM node:14.13.1-alpine

WORKDIR /app/frontend

COPY package.json /app/frontend/package.json
RUN npm install

ENTRYPOINT ["npm", "start"]
