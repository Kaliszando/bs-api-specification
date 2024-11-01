<!-- PROJECT LOGO -->
<div align="center">
<h3><img src="https://github.com/Kaliszando/bs-web-client/blob/main/src/assets/img/favicon-16x16.png" alt="Logo" width="16" height="16"> BugStalker API</h3>
</div>

BugStalker projects:
* [bs-business](https://github.com/Kaliszando/bs-business) backend
* [bs-web-client](https://github.com/Kaliszando/bs-web-client) frontend
* [bs-api-specification](https://github.com/Kaliszando/bs-api-specification) API specification and generation tool

<!-- ABOUT THE PROJECT -->
## About The Project

The API specification project serves as the backbone for both frontend and backend development in the BugStalker application.
It defines the API endpoints and data models, required for seamless communication between 
the frontend and backend applications.

In essence, the API Specification project not only documents the endpoints but also provides a mechanism 
to generate implementations of the specified endpoints,
enhancing productivity and maintainability of the BugStalker application.

### Built With

- Swagger + OpenAPI 3
- [ng-openapi-gen](https://github.com/cyclosproject/ng-openapi-gen)

<!-- GETTING STARTED -->
## Getting Started

In order to generate web services and models you need to install [ng-openapi-gen](https://github.com/cyclosproject/ng-openapi-gen).

### Prerequisites

- Java 17
- Maven
- Node.js
- npm
- [ng-openapi-gen](https://github.com/cyclosproject/ng-openapi-gen)
- python*

### Maven profiles

- `api-template-bundler` runs `api-bundler.py` before install phase. 
Bundler merges all yaml models from `src/main/schemas` and endpoints from `src/main/schemas`
into single `openapi.yaml` file.
- `backend-code-gen` enables Java jar file generation.
- `web-code-gen` runs after install phase. 
It generates frontend models and endpoint implementations.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Kaliszando/bs-api-specification.git
   ```
2. Set output directory for fronted project in `package.json`
   ```sh
   "gen-web": "ng-openapi-gen --output ../bs-web-client/src/app/api"
   ```
3. Build API project. 
   ```sh
   mvn clean install
   ```


<!-- CONTACT -->
## Contact

Adam Kalisz kaliszadam99+dev@gmail.com

LinkedIn [@adam-kalisz](https://www.linkedin.com/in/adam-kalisz/)

Other links [linktr.ee/kaliszando](https://linktr.ee/kaliszando)

<p align="right">(<a href="#-bugstalker-api">back to top</a>)</p>
