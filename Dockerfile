FROM python:3

ENV REPOSITORY_LIST_URL=$REPOSITORY_LIST_URL
ADD dockerfile-list-tool.py .
ADD requirements.txt .

RUN pip3 install -r requirements.txt
CMD ["sh", "-c", "python ./dockerfile-list-tool.py $REPOSITORY_LIST_URL"]
