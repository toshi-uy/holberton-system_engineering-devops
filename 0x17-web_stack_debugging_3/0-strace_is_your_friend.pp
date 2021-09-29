# Puppet Code to fix the error
exec{'fix-wordpress':
    command => "sed -i 's/phpp/php' /var/www/html/wp-settings.php",
    path    => "/usr/bin:/bin",
}
