module.exports = {
  ident: 'postcss',
  plugins: [
    require('autoprefixer'),
    require('css-mqpacker'),
    require('cssnano')({
      preset: [
        'default',
        {
          discardComments: {
            removeAll: true
          }
        }
      ]
    })
  ]
}
