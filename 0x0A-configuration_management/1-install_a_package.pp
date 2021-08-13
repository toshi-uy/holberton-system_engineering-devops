#Using Puppet, install puppet-lint
package { 'puppet-lint':
          require => '-y ruby',
          ensure  => ['gem install',
                      '2.1.1',
                      'created'],
      }
