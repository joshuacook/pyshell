FROM python
RUN pip install click
RUN mkdir /main
WORKDIR /main
ADD . /main
