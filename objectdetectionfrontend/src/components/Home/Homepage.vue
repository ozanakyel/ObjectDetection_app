<template>
  <div class="middle">
    <div class="card">
      <div v-for="(item,index) in projects" class="cards" @click="goToProject($event)" :key="index">
        <div class="cards-inside">
          <div class="header">
            <h3>{{item.name}}</h3>
            <div class="span">Project Active<span style="position: absolute;background-color: green;width: 8px;height: 8px;border-radius: 100%;margin-left: 5px;margin-top: 5px;"></span></div>
          </div>
          <div class="body">
            <div>
              <div><p>Bypass Active<span style="color: green;font-size: 18px">&#10003;</span></p></div>
              <div><p>Process Result</p></div>
              <div><p>Last Process Time:</p><span>19.02.2022 10:32</span></div>
              <div><p>Kamera IP:</p> </div>
              <div><p>Plc IP:</p> </div>
            </div>
          </div>
          <div class="run-stop">
            <div class="change">
              <p class="change-text">RUN</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- <div class="project">
      <div class="showproject">
        <img id="video" src="http://127.0.0.1:8000/polls/video_feed">
      </div>
    </div> -->
  </div>
</template>

<script>
export default {
  name: 'Homepage',
  data () {
    return {
      projects: []
    }
  },
  methods: {
    goToProject (event) {
      if (event.target.className !== 'change-text') {
        this.$router.push({
          name: 'Project'
        })
      }
    }
  },
  created () {
    fetch('http://127.0.0.1:8000/get_projects', {
      method: 'GET'
    })
      .then(response => response.json())
      .then(data => {
        this.projects = data
      })
  },
  mounted () {
    if (Number(document.querySelector('.middle').offsetHeight) < Number(window.innerHeight)) {
      document.querySelector('.middle').style.height = (window.innerHeight - document.querySelector('.navbar').offsetHeight) + 'px'
    }
  }
}
</script>
