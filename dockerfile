FROM Python:3.7

# install os modules
RUN apt-update -y &&\
apt install telnet -y &&\
rm -rf /var/lib/apt/lists/*

# Copy source codes
RUN mkdir -p /data-copier
COPY /app /data-copier/app
COPY requirements.txt /data-copier

# install dependencies
RUN pip install -r data-copier/reqirements.txt
