import Vue from 'vue'
import App from './App'
import Example from './Example'
;[
  App,
  {
    name: 'example',
    ...Example
  }
  // if not component name
  // { name: 'component-name', ...Component }
].forEach(Component => {
  if (!Component.name) {
    throw new Error(`Not component name: ${Component}`)
  }

  Vue.component(Component.name, Component)
})
