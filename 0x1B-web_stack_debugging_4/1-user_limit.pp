# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.
exec { 'soft' :
  command => 'sed -i s/4/50000/ /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
exec { 'hard' :
  command => 'sed -i s/5/50000/ /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
