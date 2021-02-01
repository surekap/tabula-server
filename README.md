# tabula-server

Dockerized container which spins up a python3 + Java 11 instance to convert PDF files to CSV
Uses tabula-py, flask and gunicorn

### Usage: 
`http://localhost:8000/pdf_to_lattice?url=<URL>&pages=all`

`http://localhost:8000/pdf_to_stream?url=<URL>&pages=all`


### Build Instructions
`$ sudo docker build -t tabula-server .`

### Run
`$ docker run -p 8000:8000 tabula-server`

### Init Script
```bash
#!/bin/sh
docker run -d -p 8000:8000 tabula-server
```
