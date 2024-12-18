FROM python

ENV CHAT_PORT=14447
ENV MAX_USERS=20

COPY packages packages
COPY chat_server.py chat_server.py

ENTRYPOINT ["python3", "chat_server.py"]