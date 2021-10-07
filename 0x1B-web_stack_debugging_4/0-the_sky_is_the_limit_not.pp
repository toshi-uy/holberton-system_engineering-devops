# Puppet Code to fix the error
exec { 'fix_ngnix':
  command => 'sed -i s/15/4096/ /etc/default/nginx',
  path => '/usr/bin:/bin',
}
exec { 'restart_nginx':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
  require => Exec['fix_ngnix'],
}
