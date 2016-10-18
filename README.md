sa-mysql
========

[![Build Status](https://travis-ci.org/softasap/sa-mysql.svg?branch=master)](https://travis-ci.org/softasap/sa-mysql)

classic mysql install from apt

Example of usage (all parameters are optional)

Simple

```
  roles:
    - {
        role: "sa-mysql"
      }
```

Advanced:

```
  roles:
    - {
        role: "sa-mysql",
        mysql_root_user: root,
        mysql_root_password: devroot,
      - mysql_databases:
        - name: app_db
          encoding: utf8
          collation: utf8_general_ci
      - mysql_users:
        - name: app_user
          host: "%"
          password: dYud8LHBBptGN96LSn0e
          priv: "app_db.*:ALL"
      }
```

Note: if you ever needed to downgrade mysql on xenial to 5.6 rather than default 5.7 available now - follow this dirty path:

https://gist.github.com/Voronenko/31161ab292c7967fcd38c092335a99e1

If there will be demand, I will include it into provisioning magic.  At present moment I had one request only.


