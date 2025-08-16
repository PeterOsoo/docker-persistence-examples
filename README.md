```markdown
# Docker Persistence Examples

This repository demonstrates two approaches to persisting data in Docker using a minimal Flask web application.  
The app counts page visits and stores the counter either in a **Docker-managed volume** or a **bind mount** on the host.

---

## Project Structure

```

.
├── hello-volume/       # Persistence using a Docker volume
└── hello-bind-mount/   # Persistence using a host bind mount

````

---

## Getting Started

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed  
- [Docker Compose](https://docs.docker.com/compose/) installed  

---

### 1. Run with a Docker Volume
```bash
cd hello-volume
docker compose up --build
````

Application URL: [http://localhost:5000](http://localhost:5000)

Stop and clean up (including the volume):

```bash
CTRL+C
docker compose down -v
```

---

### 2. Run with a Bind Mount

```bash
cd hello-bind-mount
docker compose up --build
```

Application URL: [http://localhost:5000](http://localhost:5000)

Stop the containers (data remains in `./data/visits.txt`):

```bash
CTRL+C
docker compose down
```

---

## Data Persistence

* **Volume**
  Stored in a Docker-managed location (good for production).
  Example: `/var/lib/docker/volumes/...`

* **Bind Mount**
  Stored directly on the host filesystem (good for development).
  Example: `./data/visits.txt`

---

## Key Takeaways

* **Volumes** → safer, portable, recommended for production use.
* **Bind mounts** → flexible, transparent, ideal for local development.

---

## License

This project is provided for educational purposes. Feel free to adapt it for your own learning or projects.

```
```
