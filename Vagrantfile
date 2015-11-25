# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.landrush.enabled = true
  config.vm.define "tower" do |tower|
    tower.vm.box = "tower"
    tower.vm.box_url = "http://vms.ansible.com/ansible-tower-2.1.4-virtualbox.box"
    tower.vm.network "forwarded_port", guest: 80, host: 80
    tower.vm.network "forwarded_port", guest: 8080, host: 8080
    tower.vm.network "private_network", ip: "192.168.33.10"
    tower.vm.hostname = "ansible-tower.vagrant.vag"
    tower.landrush.host 'tower.vagrant.vag', '10.42.0.42'
    # config.vm.network "public_network"
    # config.vm.provider "virtualbox" do |vb|
    #   vb.memory = "1024"
    # end
    end
  config.vm.define "trusty" do |trusty|
    trusty.vm.box = "ubuntu/trusty64"
    trusty.vm.network "private_network", ip: "192.168.33.11"
    trusty.vm.hostname = "trusty-host.vagrant.vag"
    trusty.landrush.host 'trusty.vagrant.vag', '192.168.33.11'
    trusty.vm.provision "ansible" do |ansible|
      ansible.playbook = "site.yml"
      ansible.tags = "auth_keys"
      end
    end
  config.vm.define "centos" do |centos|
    centos.vm.box = "centos/7"
    centos.vm.network "private_network", ip: "192.168.33.12"
    centos.vm.hostname = "centos-host.vagrant.vag"
    centos.landrush.host 'centos.vagrant.vag', '192.168.33.12'
    centos.vm.provision "ansible" do |ansible|
      ansible.playbook = "site.yml"
      ansible.tags = "auth_keys"
      end
    end
end
