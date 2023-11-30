# A puppet manifest that install Nginx web server


# Install Nginx
package { 'nginx':
  ensure => 'installed',
}

# Nginx config
file { '/etc/nginx/sites-available/default':
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
        return 301 http://www.frontendmentor.io/profile/gbabohernest;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html;
        internal;
    }
}",
}

# Create the root directory for Nginx
file { '/var/www/html':
  ensure => directory,
}

# A custom 404 page creation
file { '/var/www/html/404.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
}

# Restart Nginx service
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
