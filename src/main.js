import Vue from 'vue'
import App from './App.vue'
import axios from 'axios';
import router from './router'

Vue.prototype.$http = axios
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
