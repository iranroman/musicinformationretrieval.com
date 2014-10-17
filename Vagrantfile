# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = 'stevetjoa/stanford-mir'
  config.vm.box_version = '0.2.2'
  config.vm.hostname = 'stanford-mir'
  config.vm.boot_timeout = 60
  config.vm.synced_folder ".", "/vagrant", disabled: true
  config.vm.synced_folder ".", "/home/vagrant/stanford-mir"

  config.vm.network :forwarded_port, guest: 80, host: 8080
  config.vm.network :forwarded_port, guest: 8888, host: 8888

  config.ssh.forward_agent = true
  config.ssh.forward_x11 = true
end
