#Using Puppet, create a file in /tmp
package { 'puppet-lint':
          ensure  => ['2.1.1',
                    'created']
          require => Package['openssl']
      }
