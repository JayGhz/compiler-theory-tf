FROM python:3.12

RUN apt-get update && apt-get install -y \
    openjdk-21-jre-headless \
    llvm \
    llvm-dev \
    clang \
    vim \
    build-essential \
    wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN wget https://www.antlr.org/download/antlr-4.13.1-complete.jar

COPY requirements.txt .
COPY Quantum.g4 .
COPY example.q .
COPY quantum_compiler.py .
COPY run_compiler.py .

RUN pip install --no-cache-dir -r requirements.txt
RUN java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor Quantum.g4

# Crear directorio de salida
RUN mkdir -p /output

CMD ["/bin/bash"]