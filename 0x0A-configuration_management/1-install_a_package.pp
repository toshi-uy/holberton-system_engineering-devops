#Using Puppet, install puppet-lint
package { 'gem install puppet-lint':
          require => '-v 2.1.1',
          ensure  => ['2.1.1',
                      'created'],
      }
