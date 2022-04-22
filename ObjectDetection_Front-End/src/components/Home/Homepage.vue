<template>
  <div class="middle">
    <div class="card">
      <div v-for="(item,index) in projects" class="cards" @click="goToProject($event, index)" :key="index">
        <div class="cards-inside">
          <div class="header">
            <h3>{{item.name}}</h3>
            <div class="span">Project Active<span style="position: absolute;background-color: green;width: 8px;height: 8px;border-radius: 100%;margin-left: 5px;margin-top: 4px;"></span></div>
          </div>
          <div class="body">
            <div>
              <div><p>Bypass Active<span style="color: green;font-size: 18px">&#10003;</span></p></div>
              <!-- <div style="width: 100%"><img class="mini-image" src="" width="50%" height="100" style="object-fit: contain"><img class="mini-image" src="" width="50%" height="100" style="object-fit: contain"></div> -->
              <div><p>Process Result</p></div>
              <div><p>Last Process Time:</p><span style="font-weight: 400">19.02.2022 10:32</span></div>
              <div><p>Kamera IP:</p> </div>
              <div><p>Plc IP:</p> </div>
            </div>
          </div>
          <!-- <div class="run-stop">
            <div class="change">
              <p class="change-text">RUN</p>
            </div>
          </div> -->
        </div>
      </div>
      <div class="add-project">
      <div class="change">
        <p class="change-text" @click="popUp">Proje Ekle +</p>
      </div>
      <div class="pop-up-card" @click="popUpClose($event)">
        <div class="cards-card">
            <div class="body">
              <div class="items">
                <div class="head">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-plus-circle"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="16"></line><line x1="8" y1="12" x2="16" y2="12"></line></svg>
                    <span>Proje Ekle</span>
                </div>
                <div class="inputs">
                  <div class="input">
                    <div style="margin: 0;padding: 0;display: flex;align-items: baseline;justify-content: space-between;"><label for="pname">Proje Adı:</label><input type="text" id="pname" name="lname"></div>
                  </div>
                  <div class="input">
                    <div style="margin: 0;padding: 0;display: flex;align-items: baseline;justify-content: space-between;"><label for="pname">Proje Adı:</label><input type="text" id="pname" name="lname"></div>
                  </div>
                  <div class="input">
                    <div style="margin: 0;padding: 0;display: flex;align-items: baseline;justify-content: space-between;"><label for="pname">Proje Adı:</label><input type="text" id="pname" name="lname"></div>
                  </div>
                  <div class="input">
                    <div style="margin: 0;padding: 0;display: flex;align-items: baseline;justify-content: space-between;"><label for="pname">Proje Adı:</label><input type="text" id="pname" name="lname"></div>
                  </div>
                  <div class="input">
                    <div style="margin: 0;padding: 0;display: flex;align-items: baseline;justify-content: space-between;"><label for="pname">Proje Adı:</label><input type="text" id="pname" name="lname"></div>
                  </div>
                </div>
                <div class="send kaydet">
                    <p>EKLE</p>
                </div>
              </div>
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
    },
    popUp () {
      document.querySelector('.pop-up-card').style.display = 'flex'
    },
    popUpClose (event) {
      if (event.target.className === 'pop-up-card') {
        document.querySelectorAll('.pop-up-card').forEach(element => {
          element.style.display = 'none'
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
