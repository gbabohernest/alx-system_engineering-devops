# Install flask verion 2.1.0 from pip3
package { 'flask':
  enure    => '2.1.0',
  provider => 'pip3',
}
