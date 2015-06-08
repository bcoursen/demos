# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.landrush.enabled = true
  config.vm.define "tower" do |tower|
    tower.vm.box = "tower"
    tower.vm.box_url = "http://vms.ansible.com/ansible-tower-2.1.4-virtualbox.box"
    tower.vm.network "forwarded_port", guest: 80, host: 8080
    tower.vm.network "private_network", ip: "192.168.33.10"
    tower.vm.hostname = "ansible-tower.vagrant.dev"
    tower.landrush.host 'tower.vagrant.dev', '10.42.0.42'
    # config.vm.network "public_network"
    # config.vm.provider "virtualbox" do |vb|
    #   vb.memory = "1024"
    # end
    end
  config.vm.define "prdtrusty" do |trusty|
    trusty.vm.box = "ubuntu/trusty64"
    trusty.vm.network "private_network", ip: "192.168.33.11"
    trusty.vm.hostname = "trusty-host.vagrant.dev"
    # trusty.landrush.host 'trusty.vagrant.dev', '192.168.33.11'
    end
  config.vm.define "prdcentos" do |centos|
    centos.vm.box = "centos/7"
    centos.vm.network "private_network", ip: "192.168.33.12"
    centos.vm.hostname = "centos-host.vagrant.dev"
    # centos.landrush.host 'centos.vagrant.dev', '192.168.33.12'
  end
end
