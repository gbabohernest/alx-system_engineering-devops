# puppet code to fix wrong file extensions in the WordPress file 'web-setting.php'.

$path_file = '/var/www/html/wp-settings.php'

exec { 'replace_in_place':
  command => "sed -i 's/phpp/php/g' ${path_file}",
  path    => ['/bin','/usr/bin']
}
