FROM python:3.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code
CMD ["uvicorn", "main:app", "--reload", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]



#FROM node:18-alpine as build
#WORKDIR /app
#COPY . /app
#RUN npm i
#RUN npm run build
#
#FROM node:18-alpine
#WORKDIR app/
#COPY --from=build /app/build /app/build
#COPY . /app
#RUN npm i -g serve
#CMD ["serve", "-s", "-n", "build", "-l", "3000"]