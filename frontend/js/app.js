import Vue from 'vue'
import store from './store'

import './plugins'
import './components'

Vue.config.productionTip = false

/* eslint-disable */
if ($('#app').length) {
  new Vue({
    el: '#app',
    store
  })
}
/* eslint-enable */
