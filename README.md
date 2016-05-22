sa-mysql
========

[![Build Status](https://travis-ci.org/softasap/sa-mysql.svg?branch=master)](https://travis-ci.org/softasap/sa-mysql)

classic mysql install from apt

Example of usage (all parameters are optional)

Simple

  roles:
    - {
        role: "sa-mysql"
      }


Advanced:


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




