upstream web {
    server web:8000;
}

server {

    listen 80;
    server_name debt.makarenko.tech;
    return 301 https://debt.makarenko.tech$request_uri;
}

server {

    listen 443 ssl;
    server_name debt.makarenko.tech;

    ssl_certificate /etc/ssl/cert/makarenko.crt;
    ssl_certificate_key /etc/ssl/cert/makarenko.key;



    location / {

        proxy_pass http://web;
        proxy_redirect off;
        proxy_set_header Host $http_host;
        proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
    }
}
