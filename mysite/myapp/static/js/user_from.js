var app6 = new Vue({
  el: '#app-6',
  delimiters: ['[[', ']]'],
  data: {
    user_from_challenge: [],
    seen: true,
    unseen: false
  },
  //Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
  created: function () {
    this.fetchInputList();
    this.timer = setInterval(this.fetchInputList, 10000);
  },
  methods: {
    fetchInputList: function () {
      axios
        .get('/user_from/')
        .then(response => (this.user_from_challenge = response.data.user_from_challenge))
      console.log(this.user_from_challenge)
      this.seen = false
      this.unseen = true
    },
    cancelAutoUpdate: function () {
      clearInterval(this.timer)
    }
  },
  beforeDestroy() {
    this.cancelAutoUpdate();
  }

})