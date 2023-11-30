# A puppet manifest that install Nginx web server

package { 'nginx':
  ensure => 'present',
}

exec { 'install':
  command  => 'sudo apt-get update && sudo apt-get -y install nginx',
  provider => shell,
}

exec { 'Hello':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec { 'redirect_config':
  command  =>
    'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \\/redirect_me {\\n\\t\\treturn 301 https:\\/\\/www.frontendmentor.io\\/profile/gbabohernest\\/;/\\n\\t}/" /etc/nginx/sites-available/default'
  ,
  provider => shell,
  require  => Exec['install'], # Ensure this runs after the 'install' exec
}

exec { 'run':
  command  => 'sudo service nginx restart',
  provider => shell,
  require  => Exec['redirect_config'], # Ensure this runs after the 'redirect_config' exec
}
