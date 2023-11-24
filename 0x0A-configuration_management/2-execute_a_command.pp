# Executes the pkill command to kill a process named killmenow

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
}
