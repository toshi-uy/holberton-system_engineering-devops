# automate the task of creating a custom HTTP header response, but with Puppet

package { 'nginx':
    ensure => present,
    name   => 'nginx',
}

file_line { 'header':
    ensure  => present,
    path    => '/etc/nginx/sites-available/default',
    after   => 'listen 80 default_server;',
    line    => "add_header X-Served-By ${hostname};",
    require => Package['nginx'],
}

exec { 'restart':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
  require => File_line['header'],
}
