# FROM ham5312/covidarticle:1.0
FROM ham5312/sherlock:1.0

WORKDIR /app
COPY . .
RUN pip install torch==1.7.1+cu101 torchvision==0.8.2+cu101 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
CMD python3 server.py
