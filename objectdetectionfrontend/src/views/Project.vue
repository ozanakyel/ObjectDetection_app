<template>
  <div class="project">
      <Navbar/>
      <ProjectArea/>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from '@/components/Navbar.vue'
import ProjectArea from '@/components/Project/ProjectArea.vue'
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Project',
  components: {
    Navbar,
    ProjectArea
  },
  data () {
    return {
      msg: ''
    }
  }
}
</script>
