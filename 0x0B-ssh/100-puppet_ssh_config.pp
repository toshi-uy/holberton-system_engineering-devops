# changes to our configuration file
file_line {
    path  => '/etc/ssh/ssh_config',
    line  => 'PasswordAuthentication no',
    match => 'PasswordAuthentication yes',
}
file_line {
    path  => '/etc/ssh/ssh_config',
    line  => 'IdentityFile ~/ssh/holberton',
    match => 'IdentityFile ~/ssh/id_rsa',
}
