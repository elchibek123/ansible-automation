# PostgreSQL Installation Role

This role installs and configures PostgreSQL inside a Docker container using Docker Compose on an Ubuntu server.

## Requirements

- Ubuntu 20.04 or newer
- Docker pre-installed on the server
- Ansible 2.9 or newer

## Role Variables

The following variables can be customized when using this role:

- `postgresql_version`: The PostgreSQL version to install (default: `17`).
- `postgresql_container_name`: Name for the PostgreSQL Docker container (default: `postgres_db`).
- `postgresql_db_name`: The name of the PostgreSQL database to create (default: `postgres_db`).
- `postgresql_user`: The PostgreSQL user to create (default: `postgres`).
- `postgresql_password`: Password for the PostgreSQL user (default: `postgres123`).
- `postgresql_data_dir`: The directory where PostgreSQL data will be stored (default: `/opt/postgresql/data`).
- `postgresql_port`: The port PostgreSQL will be exposed on (default: `5432`).

## Usage

Add this role to your playbook like this:

```yaml
- hosts: servers
  roles:
    - role: ../roles/postgresql