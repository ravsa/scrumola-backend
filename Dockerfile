FROM registry.centos.org/centos/centos:7

RUN useradd scrumola
RUN yum install -y gcc &&\
    yum install -y epel-release &&\
    yum install -y python34-pip &&\
    yum install -y redhat-rpm-config gcc libffi-devel httpd-devel python34-devel openssl-devel &&\
    yum clean all

RUN mkdir -p /scrumola_backend
COPY ./ /scrumola_backend
WORKDIR /scrumola_backend
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["gunicorn", "app:app"]
