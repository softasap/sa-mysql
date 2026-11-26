import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_mysql_server_installed(host):
    pkg = host.package('mysql-community-server')

    assert pkg.is_installed


# NOTE: testinfra tests run via `pytest` against the molecule inventory.
# They require the paramiko package (in pyproject.toml) and resolvable
# SSH targets — prefer the ansible verifier (verify.yml) which runs
# inside the molecule inventory context.
