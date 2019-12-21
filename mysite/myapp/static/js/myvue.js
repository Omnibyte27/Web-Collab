var app5 = new Vue({
  el: '#app-5',
  delimiters: ['[[', ']]'],
  data: {
    players: [],
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
        .get('/players/')
        .then(response => (this.players = response.data.players))
      console.log(this.players)
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
