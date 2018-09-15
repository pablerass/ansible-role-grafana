"""Defautl test module."""
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service(host):
    """Test service."""
    service = host.service("grafana-server")
    assert service.is_enabled
    assert service.is_running


def test_socket(host):
    """Test socket connection."""
    socket = host.socket("tcp://0.0.0.0:3000")
    assert socket.is_listening
