# Example of how to run A-Frame locally using `<script>` tags without bundlers / package managers

## If only HTTP needed

```
python -m SimpleHTTPServer 8080
```

## For HTTTPS

- Generate certificate

```
openssl req -new -x509 -keyout key.pem -out server.pem -days 365 -nodes
```

- Run server

```
  python https-server.py
 ```