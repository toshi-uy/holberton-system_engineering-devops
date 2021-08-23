# automate the task of creating a custom HTTP header response, but with Puppet

package { 'nginx':
  ensure => present,
  name   => 'nginx',
}

file_line { 'add_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _',
  line   => 'add_header X-Served-By "$HOSTNAME";',
}

exec { 'restart':
  ensure  => running,  
  enable => True,
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
  require => File_line['header'],
}
