# Web-based Microservices Library Application

This is a microservices-based web application built with Flask, consisting of several independent services that communicate with each other using HTTP requests. The application demonstrates a simple book store with books and authors.

## Services

The application is composed of the following services:

1. **Book Service**: Handles book-related operations (get all books, get a specific book).
2. **Author Service**: Handles author-related operations (get all authors, get a specific author).
3. **API Gateway**: Acts as an entry point for clients and routes requests to the appropriate service.
4. **Web Frontend**: Serves the web application for users, interacting with the API Gateway to fetch and display data.

## Getting Started

### Prerequisites

- Docker
- Docker Compose (optional)

### Running the Application

1. Clone the repository:

    `git clone https://github.com/Thaaaraka97/simple-library-app.git`

    `cd microservices-web-app`

2. Build the Docker images:

    `docker-compose build`

3. Start the containers:

    `docker-compose up`

    This will start all the services as separate Docker containers and map the respective ports to the host machine.

4. Access the web application:

    Once all the containers are running, you can access the web application by opening your web browser and navigating to `http://localhost:5003`.

## Deployment Options

In addition to the standard Docker Compose setup, this application can also be deployed using Kubernetes and Docker Swarm.

### Kubernetes

The Kubernetes deployment manifests are located in the `kubernetes/` directory. To deploy the application on a Kubernetes cluster, follow these steps:

1. Ensure you have a running Kubernetes cluster.
2. Navigate to the `k8-manifests/` directory.

    `cd k8-manifests`

3. Apply the manifests using the `kubectl` command:

    `kubectl apply -f deployments.yaml`
    
    `kubectl apply -f services.yaml`

4. Monitor the deployment progress using the following commands:

    `kubectl get pods -o wide`
    
    `kubectl get services`

### Docker Swarm

The Docker Swarm deployment configuration is provided in the `docker-stack.yml` as a stack file. To deploy the application on a Docker Swarm cluster, follow these steps:

1. Ensure you have a running Docker Swarm cluster.
2. Deploy the stack using the `docker stack deploy` command:

    `docker stack deploy -c docker-stack.yml library-stack`

3. Monitor the deployment progress using the following commands:

    `docker stack services library-stack`
    
    `docker stack ps library-stack`


## Contributing

Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).