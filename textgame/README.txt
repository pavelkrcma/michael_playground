BUILD:
docker build -t textgame .

RUN:
docker run -d --rm -p 2222:22 textgame

CONNECT:
ssh -o StrictHostKeyChecking=accept-new game@localhost -p 2222
pw: hrej
