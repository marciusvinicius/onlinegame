FROM python:3.8.0-slim

WORKDIR /usr/src/app
COPY requirements.txt .

# Dependencies
RUN set -ex; \
    update-ca-certificates; \
    apt update; \
    apt install --no-install-recommends -y gcc python3-dev default-libmysqlclient-dev; \
    pip install --no-cache-dir --upgrade setuptools pip; \
    pip install --no-cache-dir -r requirements.txt; \
    apt remove -y gcc python3-dev; apt autoremove -y; apt autoclean -y; \
    rm -rf /var/lib/apt/lists/*;

COPY . .
EXPOSE 80
RUN python manage.py db init \
    python manage.py db migrate --message 'initial database migration' \
    python manage.py db upgrade
CMD gunicorn -b 0.0.0.0:80 -w 2 --reload wsserver.wsgi