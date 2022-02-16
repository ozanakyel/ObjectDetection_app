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
  name: 'Project',
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
    fetch('http://127.0.0.1:8000/get_projects', {
      method: 'GET'
    })
      .then(response => response.json())
      .then(data => {
        this.data = data
        document.querySelector('.data').innerHTML = this.data
      })
    // setInterval(function () {
    //   fetch('http://127.0.0.1:8000/get_projects', {
    //     method: 'GET'
    //   })
    //     .then(response => response.json())
    //     .then(data => {
    //       this.data = data
    //       document.querySelector('.data').innerHTML = this.data
    //     })
    // }, 15000)
  }
}
</script>
