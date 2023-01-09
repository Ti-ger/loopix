FROM ubuntu:20.04
WORKDIR /app
COPY loopix . 
EXPOSE 3000
RUN apt-get -y update
RUN apt-get -y install python2.7
RUN apt-get -y dist-upgrade
RUN apt-get -y install python-dev build-essential
RUN apt-get -y install curl
RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
RUN python2 get-pip.py
RUN pip2 --version
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
RUN apt-get -y install libssl-dev libffi-dev git-all
RUN yes | pip install petlib
RUN yes | python2.7 -m pip install --upgrade pip
RUN yes | python2.7 -m pip install --upgrade virtualenv
RUN yes | python2.7 -m pip install twisted==16.6.0
RUN yes | python2.7 -m pip install numpy
RUN yes | python2.7 -m pip install service_identity
RUN yes | python2.7 -m pip install sphinxmix
RUN apt-get -y install htop
#sudo('apt-get -y install tshark')
RUN python -c "import petlib; petlib.run_tests()"
ENV HOST mix0
ENV ID 0
ENV GROUP 0
CMD python setup_mixnode.py 9999 $HOST Mix${ID} $GROUP
