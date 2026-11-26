sa-mysql
========

Installs MySQL from the official `repo.mysql.com` repositories
(Debian/Ubuntu via apt, EL 8/9/10 via yum) — LTS (8.4 / 9.7) by
default, with optional hardening, database/user management and console
colorizer.

Release selection
-----------------

```YAML
  roles:
    - role: "sa-mysql"                # newest MySQL 8.4 LTS (default)
```

```YAML
  roles:
    - role: "sa-mysql"
      mysql_lts_family: "9"           # newest MySQL 9.7 LTS
      mysql_release: "8.4"            # or concrete series
      # mysql_release: "8.4.13"       # or pinned version (apt glob)
      # mysql_release: innovation     # or the innovation series
```

Full parameter list (all optional):

| Variable              | Default    | Description                                            |
|-----------------------|------------|--------------------------------------------------------|
| `mysql_release`       | `lts`      | `lts`, `innovation`, series (`"8.4"`) or pinned version (`"8.4.13"`) |
| `mysql_lts_family`    | `"8"`      | LTS family when `mysql_release: lts` — `8` → 8.4 LTS, `9` → 9.7 LTS |
| `mysql_apt_component` | derived    | Override the repo.mysql.com apt component directly      |
| `mysql_state`         | `latest`   | Package state (`latest` tracks the enabled series)      |
| `mysql_root_user`     | `root`     | Administrative user                                     |
| `mysql_root_password` | `Devroot#1` | Root password ("development root"; must satisfy validate_password MEDIUM on EL — preseeded via debconf on Debian, temp-password ALTER on EL) |
| `option_harden_mysql` | `true`     | Remove anonymous users, remote root, test database      |
| `mysql_mysqld_settings`| `{}`      | Rendered into `/etc/mysql/mysql.conf.d/99-sa-mysql.cnf` |
| `mysql_databases`     | `[]`       | Databases to create                                     |
| `mysql_users`         | `[]`       | Users to create                                         |

Advanced:

```YAML
  roles:
    - role: "sa-mysql"
      mysql_root_password: "s3cr3t"
      mysql_mysqld_settings:
        max_connections: 200
        bind-address: "0.0.0.0"
      mysql_databases:
        - name: app_db
          encoding: utf8mb4
          collation: utf8mb4_general_ci
      mysql_users:
        - name: app_user
          host: "%"
          password: dYud8LHBBptGN96LSn0e
          priv: "app_db.*:ALL"
```

Testing
-------

- libvirt acceptance matrix (every supported OS × both LTS families):
  `make molecule-libvirt`
- docker scenario (CI parity): `make molecule-docker`

Usage with ansible galaxy workflow
----------------------------------

If you installed the sa-mysql role using the command
`ansible-galaxy install softasap.sa_mysql`, add the role to your playbook:

    - hosts: servers
      roles:
        - role: softasap.sa_mysql

Dependencies
------------

- `community.mysql` collection (database/user management).
- PyMySQL on the target (installed by the role).
