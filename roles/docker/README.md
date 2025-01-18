# Docker Installation Role

This role installs Docker on an Ubuntu server.

## Requirements

- Ubuntu 20.04 or newer
- Ansible 2.9 or newer

## Role Variables

- `docker_packages`: List of Docker-related packages to install. The default list includes:
  - `docker-ce`
  - `docker-ce-cli`
  - `containerd.io`
  - `docker-buildx-plugin`
  - `docker-compose-plugin`
  
- `docker_version`: Docker version to install (default: `latest`)

## Usage

Add this role to your playbook like this:

```yaml
- hosts: servers
  roles:
    - role: ../roles/docker