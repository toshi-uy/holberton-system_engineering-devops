# changes to our configuration file
file_line { 'change key':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
    match  => 'PasswordAuthentication yes',
}
file_line { 'no password':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/ssh/holberton',
    match  => 'IdentityFile ~/ssh/id_rsa',
}
