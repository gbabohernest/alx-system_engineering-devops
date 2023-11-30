# A puppet manifest that install Nginx web server

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Nginx config
file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => "# Nginx server configuration
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm;

    location / {
        echo 'Hello World!';
    }

    location /redirect_me {
        rewrite ^/redirect_me https://www.frontendmentor.io/profile/gbabohernest permanent;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html;
        internal;
    }
}",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Create the root directory for Nginx
file { '/var/www/html':
  ensure => directory,
}

# Create a custom 404 page
file { '/var/www/html/404.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
  require => File['/var/www/html'],
}

# Manage Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}

# Restart Nginx service when configuration changes
exec { 'nginx-restart':
  command     => '/usr/sbin/service nginx restart',
  path        => ['/usr/bin', '/usr/sbin'],
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-enabled/default'],
}
