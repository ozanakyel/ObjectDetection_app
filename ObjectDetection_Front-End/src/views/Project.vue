<template>
  <div class="project">
      <Navbar/>
      <ProjectArea :data="data"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from '@/components/Navbar.vue'
import ProjectArea from '@/components/Project/ProjectArea.vue'
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'ProjectView',
  components: {
    Navbar,
    ProjectArea
  },
  data () {
    return {
      msg: '',
      data: []
    }
  },
  mounted () {
    document.querySelector('.navbar').style.display = 'none'
  }
}
</script>
