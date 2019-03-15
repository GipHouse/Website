# Serverconfig

The GiPHouse website runs on a [Amazon LightSail](https://aws.amazon.com/lightsail/) server which currently has the IPv4 address `35.157.118.162` (IPv6 is not supported by Amazon Lightsail yet). This server can be reached via SSH (only with publickey).

Some basic information about the server can be configured in the LightSail dashboard. This includes the firewall. 
We opened ports `22`, `80` and `443` to enable SSH, HTTP and HTTPS.

### Server Info
OS: Ubuntu 18.04
user: `ubuntu`

### DNS
Currently there are two domains, `{staging,testing}.giphouse.nl`, that point to `35.157.118.162`.
The DNS is managed by CnCZ (the ICT department of the Science Faculty of the Radboud).

### Continuous Deployment
Whenever a commit is merged into `master`, [`deploy.sh`](https://github.com/GipHouse/GiPHouse-Spring-2019/blob/master/resources/deploy.sh) is executed. This scripts runs on a Travis CI runner and gets certain secrets via the environment variables.

This script builds a new version of [the Docker image](https://hub.docker.com/r/giphouse/giphousewebsite) and pushes it to the Docker Hub Registry, fills in the right secrets into `docker-compose.yaml` and the database initialization file (`setup.sql`). 

### Setup steps
Some manuall steps are taken to setup the server. These steps are not done in the deployment script, because these steps are only necessary once.

1. Add the SSH public keys of engineers to the authorized keys of the `ubuntu` user. 
2. Disable SSH password login.
3. Install `docker`.
4. Install `nginx`.
5. Place the general `nginx` config (`nginx.conf`), the domain specific `nginx` config (`giphouse.conf`) and `dhparam.pem`.
6. Install `letsencrypt` and request a certificate using the `cerbot` `nginx` module.