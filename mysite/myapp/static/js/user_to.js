var app7 = new Vue({
    el: '#app-7',
    delimiters: ['[[', ']]'],
    data: {
      user_to_challenge: [],
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
          .get('/user_to/')
          .then(response => (this.user_to_challenge = response.data.user_to_challenge))
        console.log(this.user_to_challenge)
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