<template>
  <div class="project-area">
    <Loader/>
    <div class="project-view">
      <div class="top">
        <div @click="check" class="shower" style="position: relative;">
          MIFI - Object Detection / SafetyZone
          <div @click="goToHome" class="exit" style="position:absolute;right:0;top: -8px;text-align: right;padding:8px 12px 8px 5px;cursor: pointer;">
            <span style="font-size: 11px; color: red;margin-right: 3px;">Çıkış</span><svg xmlns="http://www.w3.org/2000/svg" style="color: red" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-log-out"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
          </div>
        </div>
        <div>
          <div class="butons">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-activity"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg><span style="margin-left: 5px;">Connect</span>
          </div>
          <div class="butons">
              <img src="@/assets/eraser.png" width="24" height="24"/><span style="margin-left: 5px;">Clear</span>
          </div>
          <div class="checkbox">
            <input type="checkbox" id="bypass" name="bypass" value="ByPass">
            <label for="bypass" style="font-size: 14px;cursor: pointer;">ByPass</label><br>
          </div>
          <div @click="settings" class="butons settings">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-settings"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg><span style="margin-left: 5px;">Settings</span>
          </div>
        </div>
      </div>
      <div class="body">
        <div><img class="images" width="100%" height="630" :src="video_feed"></div>
        <div><img class="images" width="100%" height="630" :src="object_detection"></div>
      </div>
      <div class="ok-nok">
        <template>
          <div class="butons" v-for="(item,index) in ok_nok" :key="index">
              <span class="status"></span><span style="margin-left: 3px;margin-right: 6px;" class="text">OK</span>
          </div>
        </template>
          <!-- <div class="butons">
              <span class="status"></span><span style="margin-left: 3px;margin-right: 6px;">OK</span>
          </div>
          <div class="butons">
              <span class="status"></span><span style="margin-left: 3px;margin-right: 6px;">OK</span>
          </div>
          <div class="butons">
              <span class="status"></span><span style="margin-left: 3px;margin-right: 6px;">OK</span>
          </div> -->
        </div>
      <!-- {{data}} -->
      <div class="footer">
        <div>
          <div class="info">
            <table style="width: 100%;">
              <tr>
                <th>Header</th>
                <th>Message</th>
                <th>Date</th>
              </tr>
              <tr v-for="(item,index) in data" :key="index">
                <td><span style="color: green;">&#10003;</span> Başarılı</td>
                <td>PLC'e operasyon tamamlandı biti setlendi DbAdres: DB5.DBX0.1</td>
                <td>01.02.2022 13:28:13</td>
              </tr>
              <tr >
                <td><span style="color: green;">&#10003;</span> Başarılı</td>
                <td>PLC'e operasyon tamamlandı biti setlendi DbAdres: DB5.DBX0.1</td>
                <td>01.02.2022 13:28:13</td>
              </tr>
              <tr></tr>
              <tr>
                <td><span style="color: green;">&#10003;</span> Başarılı</td>
                <td id="messages"></td>
                <td>01.02.2022 13:28:13</td>
              </tr>
            </table>
          </div>
        </div>
      </div>
    </div>
    <div @click="hideSettings($event)" class="settings-show">
      <div class="settings">
        <div>
          <div class="header">
            <div><svg xmlns="http://www.w3.org/2000/svg" style="margin-bottom: 2px;" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-settings"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg></div>
            <div><span style="margin-left: 3px;">Settings</span></div>
          </div>
          <div class="body">
            <div id="inputs">
              <div id="inputs-1">
                <div class="inputs"><div>Kamera IP Adresi:</div> <div><input v-model="cameraIp" disabled/></div></div>
                <div class="inputs"><div>PLC IP Adresi:</div> <div><input v-model="plcIp" disabled/></div></div>
                <div class="inputs"><div>Tahminleme Min Oran %:</div> <div><input v-model="minOran" type="number" step="1" disabled/></div></div>
                <div class="inputs"><div>Maksimum Deneme Sayısı:</div> <div><input v-model="denemeSayisi" type="number" step="1" disabled/></div></div>
                <div class="inputs"><div>İstasyon Db Adres:</div> <div><input v-model="dbAdres" disabled/></div></div>
                <div class="inputs"><div>Operasyon Başladı mı DB:</div><div> <input v-model="basladimi" disabled/></div></div>
                <div class="inputs"><div>Operasyon Tamamlandı mı DB:</div> <div><input v-model="tamamlandimi" disabled/></div></div>
              </div>
              <div id="inputs-2">
                <div class="crop">
                  <span class="head">Crop</span>
                  <div class="inputs"><div>Başlangıç X:</div> <div><input v-model="x" type="number" step="1" disabled/></div></div>
                  <div class="inputs"><div>Başlangıç Y:</div> <div><input v-model="y" type="number" step="1" disabled/></div></div>
                  <div class="inputs"><div>X Mesafesi:</div> <div><input v-model="xRange" type="number" step="1" disabled/></div></div>
                  <div class="inputs"><div>Y Mesafesi:</div> <div><input v-model="yRange" type="number" step="1" disabled/></div></div>
                </div>
              </div>
            </div>
            <div class="footer">
              <div>
                <div id="inputs-2" style="width: 100%">
                  <div class="inputs"><div>Resim Klasörü: </div> <div style="width: 85%"><input v-model="x" type="number" step="1" disabled/></div></div>
                  <div class="inputs"><div>Log Dosyası:</div> <div style="width: 85%"><input v-model="y" type="number" step="1" disabled/></div></div>
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
import Loader from '@/components/Loader.vue'

export default {
  name: 'ProjectArea',
  props: {
    msg: String,
    data: Array
  },
  data () {
    return {
      connection: null,
      ok_nok: 2,
      video_feed: 'http://127.0.0.1:8000/video_feed/' + this.$route.params.id,
      object_detection: 'http://127.0.0.1:8000/object_detection/' + this.$route.params.id
    }
  },
  components: {
    Loader
  },
  methods: {
    settings () {
      document.querySelector('.settings-show').style.display = 'flex'
    },
    hideSettings (event) {
      if (event.target.className === 'settings-show') {
        document.querySelector('.settings-show').style.display = 'none'
      }
    },
    goToHome () {
      this.$router.push({
        name: 'Home'
      })
    },
    check () {
      var images = document.querySelectorAll('.images')
      console.log(images[0].offsetWidth)
      // console.log(images[0].attributes[1].isConnected)
    }
  },
  created () {
    console.log(this.$route.params.selectedProject)
    const url = 'ws://127.0.0.1:8081/ws/socket-server/'

    const chatSocket = new WebSocket(url)

    chatSocket.onmessage = function (e) {
      const data = JSON.parse(e.data)
      var parser = JSON.parse(data.message.replaceAll('\'', '"'))
      // const html = '<div class="butons"><span class="status"></span><span style="margin-left: 3px;margin-right: 6px;">OK</span></div>'
      // console.log('Data:', parser[0])

      if (data.type === 'chat') {
        const messages = document.querySelectorAll('.ok-nok .butons .status')
        const OkNok = document.querySelectorAll('.ok-nok .butons .text')
        if (parser[0].PollyIsIn[parser[0].PollyIsIn.length - 1] === 'True') {
          messages[0].style.backgroundColor = 'red'
          OkNok[0].innerText = 'NOK'
        } else {
          messages[0].style.backgroundColor = 'green'
          OkNok[0].innerText = 'OK'
        }
        if (parser[0].PollyIsIn[parser[0].PollyIsIn.length - 2] === 'True') {
          messages[1].style.backgroundColor = 'red'
          OkNok[1].innerText = 'NOK'
        } else {
          messages[1].style.backgroundColor = 'green'
          OkNok[1].innerText = 'OK'
        }
        // for (var i = 0; i < parser[0].PollyIsIn.length; i++) {
        //   messages.insertAdjacentHTML('afterbegin', '<div class="butons"><span class="status"></span><span style="margin-left: 3px;margin-right: 6px;">OK</span></div>')
        //   // messages.innerHTML = html
        // }
        // messages.insertAdjacentHTML('beforeend', `<div>
        //                         <p>${data.message}</p>
        //                     </div>`)
      }
    }
    // let form = document.getElementById('form')
    // form.addEventListener('submit', (e)=> {
    //     e.preventDefault()
    //     let message = e.target.message.value
    //     chatSocket.send(JSON.stringify({
    //         'message':message
    //     }))
    //     form.reset()
    // })
  },
  mounted () {
    // console.log(document.querySelector('.project-area').offsetHeight)
    // console.log(window.innerHeight)
    if (Number(document.querySelector('.project-area').offsetHeight) < Number(window.innerHeight)) {
      document.querySelector('.project-area').style.height = (window.innerHeight) + 'px'
    }
    // fetch('http://127.0.0.1:8000/get_projects', {
    //   method: 'GET'
    // })
    //   .then(response => response.json())
    //   .then(data => {
    //     this.data = data
    //     document.querySelector('.data').innerHTML = this.data
    //   })
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
    // var images = document.querySelectorAll('.images')
    // console.log(images[0].offsetWidth)
    // if (images[0].attributes[1].isConnected === true) {
    //   document.querySelector('.loader-scene').style.display = 'none'
    // }
    // document.querySelector('.exit').addEventListener('click', this.goToHome())
    // console.log(document.querySelector('img.images').style.innerHeight)
  }
}
</script>
