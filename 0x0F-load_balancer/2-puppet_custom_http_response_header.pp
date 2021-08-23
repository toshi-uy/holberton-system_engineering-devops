# automate the task of creating a custom HTTP header response, but with Puppet

package { 'nginx':
    ensure => present,
    name   => 'nginx',
}

file_line { 'header':
    path    => '/etc/nginx/sites-available/default',
    after => 'root /var/www/html;',
    line    => "add_header X-Served-By ${hostname};",
    require => Package['nginx'],
}

exec { 'restart':
  ensure  => running,  
  enable => True,
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
  require => File_line['header'],
}
