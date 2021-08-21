# changes to our configuration file
file_line { 'no_password':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/ssh/holberton',
}
file_line { 'change_key':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
}
