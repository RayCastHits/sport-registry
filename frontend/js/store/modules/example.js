import Cookies from 'js-cookie'
import * as types from '../mutation-types'

export const state = {
  example: Cookies.get('example') || null
}

export const getters = {
  example: state => state.example,
  check: state => state.example !== null
}

export const mutations = {
  [types.EXAMPLE_ADD](state, { example }) {
    state.example = example
    Cookies.set('payload', example)
  },

  [types.EXAMPLE_REMOVE](state) {
    state.payload = null
    Cookies.remove('example')
  }
}
