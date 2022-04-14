<template>
  <div class="home">
    <!-- <img id="video" src="http://127.0.0.1:8000/polls/video_feed"> -->
    <Navbar/>
    <Homepage/>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from '@/components/Navbar.vue'
import Homepage from '@/components/Home/Homepage.vue'

export default {
  name: 'HomeView',
  components: {
    Navbar,
    Homepage
  },
  data () {
    return {
      msg: ''
    }
  }
  // mounted () {
  // }
}
</script>
