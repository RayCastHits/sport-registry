import axios from 'axios'
import Cookies from 'js-cookie'

axios.interceptors.request.use(request => {
  request.headers.common['X-CSRFToken'] = Cookies.get('csrftoken')
  request.baseURL = '/api/v1'
  return request
})
