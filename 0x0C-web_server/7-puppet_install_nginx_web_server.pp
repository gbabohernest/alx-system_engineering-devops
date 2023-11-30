# A puppet manifest that install Nginx web server

# Install Nginx
package { 'nginx':
  ensure => installed,
}

file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server; ',
  line   => 'rewrite ^/redirect_me https://www.frontendmentor.io/profile/gbabohernest permanent; ',
}

file { '/var/www/html/':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
