var app = new Vue({
    el: '#app',
    data: {
      message: 'Hello Vue!'
    }
  })
  
//var app4 = new Vue({
//  el: '#app-4',
//  data: {
//    todos: [
//      { text: 'Learn JavaScript' },
//      { text: 'Learn Vue' },
//      { text: 'Build something awesome' }
//    ]
//  }
//})

var app4 = new Vue({
    el: '#app-4',
    data: {
      inputs: [],
      seen:true,
      unseen:false
    },
    //Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
    created: function() {
          this.fetchInputList();
          this.timer = setInterval(this.fetchInputList, 10000);
    },
    methods: {
      fetchInputList: function() {
          // $.get('/suggestions/', function(suggest_list) {
          //     this.suggestions = suggest_list.suggestions;
          //     console.log(suggest_list);
          // }.bind(this));
          axios
            .get('/inputs/')
            .then(response => (this.inputs = response.data.inputs))
          console.log(this.inputs)
          this.seen=false
          this.unseen=true
      },
      cancelAutoUpdate: function() { clearInterval(this.timer) }
    },
    beforeDestroy() {
      // clearInterval(this.timer)
	  this.cancelAutoUpdate();
    }
  
})