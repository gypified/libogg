# This file is used with the GYP meta build system.
# http://code.google.com/p/gyp
# To build try this:
#   svn co http://gyp.googlecode.com/svn/trunk gyp
#   ./gyp/gyp -f make --depth=. libogg.gyp
#   make
#   ./out/Debug/test

{
  'target_defaults': {
    'default_configuration': 'Debug',
    'configurations': {
      'Debug': {
        'defines': [ 'DEBUG', '_DEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 1, # static debug
          },
        },
      },
      'Release': {
        'defines': [ 'NDEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 0, # static release
          },
        },
      }
    },
    'msvs_settings': {
      'VCLinkerTool': {
        'GenerateDebugInformation': 'true',
      },
    },
  },

  'targets': [
    {
      'variables': { 'target_arch%': 'ia32' }, # default for node v0.6.x
      'target_name': 'ogg',
      'product_prefix': 'lib',
      'type': 'static_library',
      'sources': [
        'src/framing.c',
        'src/bitwise.c',
      ],
      'defines': [
        'PIC',
        'HAVE_CONFIG_H',
      ],
      'include_dirs': [
        # platform and arch-specific headers
        'config/<(OS)/<(target_arch)',
        'include',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          # platform and arch-specific headers
          'config/<(OS)/<(target_arch)',
          'include',
        ],
      },
    },

    {
      'target_name': 'test',
      'type': 'executable',
      'dependencies': [ 'ogg' ],
      'sources': [ 'test.c' ]
    },
  ]
}
