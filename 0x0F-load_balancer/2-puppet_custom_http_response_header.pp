# automate the task of creating a custom HTTP header response, but with Puppet

package { 'nginx':
    ensure => installed,
    name   => 'nginx',
}

file { 'index.html':
    ensure  => present,
    path    => '/var/www/html/index.html',
    content => 'Holberton School\n',
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
