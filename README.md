*Please :star: this repo if you find it useful*

<p align="left"><br>
<a href="https://www.paypal.com/paypalme/techblogil?locale.x=he_IL" target="_blank"><img src="http://khrolenok.ru/support_paypal.png" alt="PayPal" width="250" height="48"></a>
</p>



# Gotenberg-ui
Gotenberg-ui is [FastAPI](https://fastapi.tiangolo.com/) based web application allowing us to to convert documents, html pages and url to pdf documents and even merge multiple pdf files to single PDF.
Actualy Gotenberg-ui is UI Wrapper of Gotenberg wich is "Docker-powered stateless API for PDF files" written in GO Lang.

## Gotenberg-ui Features:
####  Convert URL to pdf file
[![Convert URL](https://github.com/t0mer/gotenberg-ui/blob/main/screenshots/gotenberg%20-%20convert%20web%20page.png?raw=true "Convert URL")](https://github.com/t0mer/gotenberg-ui/blob/main/screenshots/gotenberg%20-%20convert%20web%20page.png?raw=true "Convert URL")

####  Convert HTML file to pdf file
[![Convert HTML file](https://github.com/t0mer/gotenberg-ui/blob/main/screenshots/gotenberg%20-%20convert%20html%20file.png?raw=true "Convert HTML file")](https://github.com/t0mer/gotenberg-ui/blob/main/screenshots/gotenberg%20-%20convert%20html%20file.png?raw=true "Convert HTML file")

####  Convert Documents to pdf file
[![Convert Documents](https://github.com/t0mer/gotenberg-ui/blob/main/screenshots/gotenberg%20-%20convert%20documents.png?raw=true "Convert Documents")](https://github.com/t0mer/gotenberg-ui/blob/main/screenshots/gotenberg%20-%20convert%20documents.png?raw=true "Documents")

####  Merge multiple pdf documents to single file
[![Merge Documents](https://github.com/t0mer/gotenberg-ui/blob/main/screenshots/gotenberg%20-%20merge%20pdf%20files.png?raw=true "Merge Documents")](https://github.com/t0mer/gotenberg-ui/blob/main/screenshots/gotenberg%20-%20merge%20pdf%20files.png?raw=true "Merge Documents")


# Installation

#### Gotenberg Installation
Deepstack Trainer installation is very easy using docker-compose:
```
version: "3.7"

services:
  gotenberg:
    image: thecodingmachine/gotenberg:latest
    container_name: gotenberg
    restart: always
    ports:
      - "3000:3000"
```
#### Gotenberg UI Installation
Deepstack Trainer installation is very easy using docker-compose:
```
version: "3.7"

services:
  gotenbergui:
    image: techblog/gotenbergui
    container_name: gotenbergui
    restart: always
    environment:
      - GOTENBERG_API_ADDRESS=[Address and port of gotenberg docker]
    ports:
      - "8080:8080"
```
# Components and Libraries used in DeCompose
* [Gotenberg](https://gotenberg.dev/docs/about)
* [FastAPI](https://fastapi.tiangolo.com/)
* [w3layouts](https://w3layouts.com/)

