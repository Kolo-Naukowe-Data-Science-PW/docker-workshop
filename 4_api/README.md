### Example simple containerized flask API

### Build

```bash
docker build -t api .
```

### Run with port exposed (-p)

```bash
docker run --name myapi -p 5000:5000 api
```
