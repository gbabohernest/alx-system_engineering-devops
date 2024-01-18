# puppet code to fix wrong file extensions in the WordPress file 'web-setting.php'.

exec { 'fix_apache_issue':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-setting.php",
  path    => '/usr/local/bin/:bin/'
}
