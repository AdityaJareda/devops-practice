## Dockerized Nginx Web Server

This project sets up a simple **Nginx Web Server** using Docker. It includes:
- **Nginx** to serve a static webpage
- **Reverse Proxy** to forward requests
- **Persistent Storage** using Docker volumes
- **Custom Network** for container communication

---


## Project Structure
```bash
containerized-web-server/
    ├── Dockerfile
    ├── index.html
    └── nginx.conf
```

- **Dockerfile**: For building docker image to containerize the web server 
- **nginx.conf**: To configure Nginx as a reverse proxy
- **index.html**: Static webpage

---

## Step 1: Create a Volume for Data Persistence
```bash
docker volume create web-content
```

---

## Step 2: Create a Docker Network
```bash
docker network create web-network
```

---

## Step 3: Build and Run the Nginx Container
1. **Build the Docker Image**
```bash
docker build -t web-nginx .
```

2. **Run the Container**
```bash
docker run -d -p 8080:80 --name web-server --network web-network -v web-content:/usr/share/nginx/html web-nginx
```

---

## Step 4: Copy the HTML file into the volume
```bash
docker ps index.html web-server:/usr/share/nginx/html
```

---

## Step 5: Set Up a Reverse Proxy
1. Add this to your `nginx.conf`:
```nginx
events {}

http {
    server {
        listen 80;
        server_name localhost;

        location / {
            proxy_pass http://web-server:80;
        }
    }
}
```

2. Run the reverse proxy container:
```bash
docker run -d -p 8081:80 --name reverse-proxy --network web-network -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf web-nginx
```

---

## Step 6: Test
- **Web Server:** `http://['localhost' or <VM_IP>]:8080`
- **Reverse Proxy:** `http://['localhost' or <VM_IP>]:8081`

---

## IMPORTANT NOTE :-
- Make sure your **port 80** is open and isn't being used by other services.
- You can check using:
    ```bash
    sudo lsof -i :80
    ```

---

## Additional Commands
- View Logs: `docker logs -f web-server`
- Restart Container: `docker restart web-server`
- Inspect Network: `docker network inspect web-network`
