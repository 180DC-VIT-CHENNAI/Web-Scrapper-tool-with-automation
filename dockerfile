FROM mcr.microsoft.com/playwright:v1.58.0-jammy

# Install n8n (Node is already present)
RUN npm install -g n8n

# Install Python (minimal set)
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Install Node deps (for your scraper)
COPY package.json package-lock.json /tmp/
RUN cd /tmp && npm ci --omit=dev

# Security: create non-root user (matches n8n expectations)
RUN useradd -ms /bin/bash node

USER node
WORKDIR /workspace

# Assigns ownership of home dir to node
RUN mkdir -p /home/node/.n8n && chown -R node:node /home/node

# Explicit start (important when not using n8n image)
CMD ["n8n", "start"]
