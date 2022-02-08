<template>
  <div class="project">
      <Navbar/>
      <div class="top">
          <div>
              <div class="butons">
                  Connect
              </div>
          </div>
      </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from '@/components/Navbar.vue'
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Project',
  components: {
    Navbar
  },
  data () {
    return {
      msg: ''
    }
  }
}
</script>
