{
  'targets': [
    {
      'target_name': 'kinect',
      'sources': [
        'src/kinect.cc',
      ],
      'libraries': [
         '/usr/local/lib/libfreenect.a',
      ],
      'conditions': [
        ['OS=="mac"', {
          'include_dirs': ['/usr/local/include'],
          'library_dirs': ['/usr/local/lib'],
        }],
      ]
    }
  ]
}
