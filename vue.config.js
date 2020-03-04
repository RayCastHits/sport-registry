const path = require('path')
const isProd = process.env.NODE_ENV === 'production'
const webpack = require('webpack')
const BundleTracker = require('webpack-bundle-tracker')

// Config
function initConfig() {
  const frontendDir = path.join(__dirname, 'frontend')
  const staticDir = path.join(frontendDir, 'static')
  const templatesDir = path.join(frontendDir, 'templates')
  return {
    staticDir: staticDir,
    templatesDir: templatesDir,
    jsDir: path.join(frontendDir, 'js'),
    distDir: path.join(staticDir, 'dist'),
    sassDir: path.join(frontendDir, 'sass'),
    webpackStatsDir: path.join('frontend', 'static', 'dist'),
    globalStyles: ['style/abstracts']
  }
}

const settings = initConfig()

function loadGlobalStyles() {
  return settings.globalStyles.map(path => `@import "${path}"`).join('\n')
}

module.exports = {
  publicPath: isProd ? '/static/dist' : 'http://localhost:8080/dist',
  outputDir: settings.distDir,
  css: {
    loaderOptions: {
      sass: {
        prependData: loadGlobalStyles()
      }
    }
  },
  chainWebpack: config => {
    config
      .entry('app')
      .clear()
      .add('./frontend/js/app.js')
      .end()
    config.plugins.delete('html')
    config.plugins.delete('preload')
    config.plugins.delete('prefetch')
    config.plugins.delete('copy')
    config.resolve.alias
      .set('@', settings.jsDir)
      .set('style', settings.sassDir)
      // .set('assets', settings.staticDir)
      .set('vue$', 'vue/dist/vue.esm.js')
    config.devServer
      .public('http://localhost:8080')
      .host('localhost')
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .contentBase(settings.templatesDir)
      .watchContentBase(true)
      .headers({ 'Access-Control-Allow-Origin': ['*'] })
  },
  configureWebpack: config => {
    config.plugins.push(
      new BundleTracker({
        path: settings.webpackStatsDir,
        filename: 'webpack-stats.json'
      })
    )
    config.plugins.push(
      new webpack.ProvidePlugin({
        $: 'jquery',
        jQuery: 'jquery',
        'windows.$': 'jquery',
        'windows.jQuery': 'jquery',
        'windows.JQuery': 'jquery'
      })
    )
  }
}
