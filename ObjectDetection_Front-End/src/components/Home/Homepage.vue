<template>
  <div class="middle">
    <div class="card">
      <div v-for="(item,index) in projects" class="cards" @click="goToProject($event, index)" :key="index">
        <div class="cards-inside">
          <div class="header">
            <h3>{{item.name}}</h3>
            <div class="span">Project Active<span style="position: absolute;background-color: green;width: 8px;height: 8px;border-radius: 100%;margin-left: 5px;margin-top: 5px;"></span></div>
          </div>
          <div class="body">
            <div>
              <div><p>Bypass Active<span style="color: green;font-size: 18px">&#10003;</span></p></div>
              <!-- <div style="width: 100%"><img class="mini-image" src="" width="50%" height="100" style="object-fit: contain"><img class="mini-image" src="" width="50%" height="100" style="object-fit: contain"></div> -->
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
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data () {
    return {
      projects: [],
      video_feed: 'http://127.0.0.1:8000/video_feed/0',
      object_detection: 'http://127.0.0.1:8000/object_detection/'
    }
  },
  methods: {
    goToProject (event, index) {
      if (event.target.className !== 'change-text') {
        this.$router.push({
          name: 'Project',
          params: { id: index }
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
        console.log(data)
      })
  },
  mounted () {
    if (Number(document.querySelector('.middle').offsetHeight) < Number(window.innerHeight)) {
      document.querySelector('.middle').style.height = (window.innerHeight - document.querySelector('.navbar').offsetHeight) + 'px'
    }
    // window.onload = function () {
    //   setInterval(() => {
    //     document.getElementsByClassName('mini-image')[0].src = 'http://127.0.0.1:8000/video_feed_single/0'
    //     console.log('Çalıştı')
    //   }, 1000)
    // }
  }
}
</script>
