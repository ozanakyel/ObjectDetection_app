<template>
  <div class="middle">
    <div class="card">
      <div v-for="n in 4" class="cards" :key="n">
        <div class="cards-inside">
          <div @click="goProject" class="header">
            <h3>OBJECT DETECTION</h3>
            <div class="span">Project Active<span style="position: absolute;background-color: green;width: 8px;height: 8px;border-radius: 100%;margin-left: 5px;margin-top: 5px;"></span></div>
          </div>
          <div @click="goProject" class="body">
            <div>
              <div><p>Bypass Active<span style="color: green;">&#10003;</span></p></div>
              <div><p>Process Result</p></div>
              <div><p>Last Process Time:</p><span>19.02.2022 10:32</span></div>
              <div><p>Kamera IP:</p> </div>
              <div><p>Plc IP:</p> </div>
            </div>
          </div>
          <div class="run-stop">
            <div class="change">
              <p>RUN</p>
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
      asd: 'asd'
    }
  },
  methods: {
    goProject () {
      this.$router.push({
        name: 'Project'
      })
    }
  },
  mounted () {
    if (Number(document.querySelector('.middle').offsetHeight) < Number(window.innerHeight)) {
      document.querySelector('.middle').style.height = (window.innerHeight - document.querySelector('.navbar').offsetHeight) + 'px'
    }
  }
}
</script>
