FROM python:3.10

COPY ./requirements.txt ./usr/app/src/requirements.txt
WORKDIR /usr/app/src

RUN pip install -r requirements.txt
RUN pip install -U git+https://github.com/Pycord-Development/pycord
RUN pip install 'pymongo[srv]'

COPY . /usr/app/src

CMD [ "python3","-u", "./bot.py"]