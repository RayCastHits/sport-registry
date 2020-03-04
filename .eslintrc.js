module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: ['plugin:vue/essential', '@vue/standard'],
  rules: {
    'template-curly-spacing': 'off',
    'space-before-function-paren': 0,
    'vue/script-indent': [
      'error',
      2,
      {
        baseIndent: 1,
        switchCase: 0,
        ignores: []
      }
    ],
    indent: 'off',
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off'
  },
  parserOptions: {
    parser: 'babel-eslint'
  }
}
