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
        <p class="change-text" @click="popUpAdd">Proje Ekle +</p>
        <p class="change-text" @click="popUpUpdate">Proje Güncelle +</p>
      </div>
      <div class="pop-up-card add" @click="popUpClose($event)">
        <div class="cards-card">
            <div class="body">
              <div class="items">
                <div class="head">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-plus-circle"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="16"></line><line x1="8" y1="12" x2="16" y2="12"></line></svg>
                    <span>Proje Ekle</span>
                </div>
                <div class="inputs">
                  <div class="input" v-for="item in input_data" :key="item">
                    <div style="margin: 0;padding: 0;display: flex;align-items: baseline;justify-content: space-between;"><span style="font-weight: 400;margin-right: 5px">{{item}}:</span><template v-if="item == 'Plant'"><input type="number" min="0" :name="item"></template><template v-else-if="item == 'Kamera Tipi'"><select style="width: 201px;height: 30px;" :name="item"><option value="ipCamera">IP Kamera</option></select></template><template v-else><input type="text" :name="item"></template></div>
                  </div>
                </div>
                <div class="send kaydet">
                    <p @click="addProject">EKLE</p>
                </div>
              </div>
            </div>
        </div>
      </div>
      <div class="pop-up-card update" @click="popUpClose($event)">
        <div class="cards-card">
            <div class="body">
              <div class="items">
                <div class="head">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-stop-circle"><circle cx="12" cy="12" r="10"></circle><rect x="9" y="9" width="6" height="6"></rect></svg>
                    <span>Proje Güncelle</span>
                </div>
                <div class="inputs" style="grid-template-columns: auto auto auto;margin: 0">
                  <div class="input" style="padding: 0">
                    <select style="width: 221px;height: 30px;" @change="showconfig" name="projectconfigupdate">
                        <option value="default" selected="true" disabled="disabled" hidden>Proje Şeçin</option>
                        <option v-for="item,index in projects" :key="index" :name="item.projectID">{{item.name}}</option>
                    </select>
                  </div>
                  <div class="input configupdate" style="display: none;padding: 0;">
                    <select style="width: 221px;height: 30px;" name="configupdate">
                        <option value="default" selected="true" disabled="disabled" hidden>Değiştirilece Ayarı Şeçin</option>
                        <option v-for="item,index in configs" :key="index" :name="item.configKeyID">{{item.configName}}</option>
                    </select>
                  </div>
                  <div class="input configupdate" style="display: none;padding: 0">
                    <div style="margin: 0;padding: 0;display: flex;align-items: baseline;justify-content: space-between;"><span style="font-weight: 400;margin-right: 5px">Yeni Değer:</span><input type="text" name="newconfigvalue"></div>
                  </div>
                </div>
                <div class="send update">
                    <p @click="updateProject">GÜNCELLE</p>
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
      configs: [],
      video_feed: 'http://127.0.0.1:8000/video_feed/0',
      object_detection: 'http://127.0.0.1:8000/object_detection/',
      input_data: ['Plant', 'Proje Adı', 'Kamera IP', 'Kamera Tipi', 'Kullanıcı Adı', 'Kullanıcı Şifre']
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
    popUpAdd () {
      // document.querySelector('.pop-up-card .update').style.display = null
      document.querySelector('.add').style.display = 'flex'
    },
    popUpUpdate () {
      // document.querySelector('.pop-up-card .add').style.display = null
      document.querySelector('.update').style.display = 'flex'
    },
    popUpClose (event) {
      if (event.target.className.split(' ')[0] === 'pop-up-card') {
        document.querySelectorAll('.pop-up-card').forEach(element => {
          element.style.display = 'none'
        })
      }
    },
    showconfig () {
      document.querySelectorAll('.configupdate').forEach(element => {
        element.style.display = 'flex'
      })
    },
    addProject () {
      fetch('http://127.0.0.1:8000/get_projects', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          plant: document.querySelector('[name="' + this.input_data[0] + '"]').value,
          name: document.querySelector('[name="' + this.input_data[1] + '"]').value,
          cameraIP: document.querySelector('[name="' + this.input_data[2] + '"]').value,
          cameraType: document.querySelector('[name="' + this.input_data[3] + '"]').options[document.querySelector('[name="' + this.input_data[3] + '"]').selectedIndex].value,
          userName: document.querySelector('[name="' + this.input_data[4] + '"]').value,
          userPassword: document.querySelector('[name="' + this.input_data[5] + '"]').value
        })
      })
        .then(response => response.json())
        .then(data => {
          alert(data)
          location.reload()
        })
    },
    updateProject () {
      fetch('http://127.0.0.1:8000/get_configs', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          projectID_id: document.querySelector('[name="projectconfigupdate"]').options[document.querySelector('[name="projectconfigupdate"]').selectedIndex].attributes.name.value,
          configKeyID_id: document.querySelector('[name="configupdate"]').options[document.querySelector('[name="configupdate"]').selectedIndex].attributes.name.value,
          configValue: document.querySelector('[name="newconfigvalue"]').value
        })
      })
        .then(response => response.json())
        .then(data => {
          alert(data)
          location.reload()
        })
    }
  },
  created () {
    fetch('http://127.0.0.1:8000/get_projects', {
      method: 'GET'
    })
      .then(response => response.json())
      .then(data => {
        this.projects = data
        // console.log(data)
      })
    fetch('http://127.0.0.1:8000/get_configs', {
      method: 'GET'
    })
      .then(response => response.json())
      .then(data => {
        this.configs = data
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
