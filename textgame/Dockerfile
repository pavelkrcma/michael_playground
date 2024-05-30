FROM python:3.12-slim

# Install openssh-server
RUN apt-get update && \
    apt-get install -y --no-install-recommends openssh-server && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /var/run/sshd

# Add a user and set password for SSH access
RUN useradd -m game
RUN echo 'game:hrej' | chpasswd

# Configure SSH server
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config
RUN echo "AllowUsers game" >> /etc/ssh/sshd_config
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
RUN echo "ForceCommand /usr/bin/python3 /usr/src/app/text_game.py" >> /etc/ssh/sshd_config

# Set the working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
