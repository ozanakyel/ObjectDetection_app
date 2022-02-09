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
        <div><img class="images" src="http://127.0.0.1:8000/video_feed" width="100%" height="630"></div>
        <div><img class="images" src="http://127.0.0.1:8000/object_detection" width="100%" height="630"></div>
      </div>
      <div class="footer">
        <div>
          <div class="info">
            <table style="width: 100%;">
              <tr>
                <th>Header</th>
                <th>Message</th>
                <th>Date</th>
              </tr>
              <tr>
                <td><span style="color: green;">&#10003;</span> Başarılı</td>
                <td>PLC'e operasyon tamamlandı biti setlendi DbAdres: DB5.DBX0.1</td>
                <td>01.02.2022 13:28:13</td>
              </tr>
              <tr>
                <td><svg xmlns="http://www.w3.org/2000/svg" width="9" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-arrow-right"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg> TipNo</td>
                <td>PLC'den tip numarası okundu. DbAdres : DB5.DBX0.0 Tip No: 3</td>
                <td>01.02.2022 13:28:11</td>
              </tr>
              <tr>
                <td><svg xmlns="http://www.w3.org/2000/svg" width="9" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-arrow-right"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg> Ürün</td>
                <td>Operasyon başlatıldı bilgisi okundu. DbAdres : DB5.DBX0.0</td>
                <td>01.02.2022 13:28:09</td>
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
    msg: String
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
  mounted () {
    // console.log(document.querySelector('.project-area').offsetHeight)
    // console.log(window.innerHeight)
    if (Number(document.querySelector('.project-area').offsetHeight) < Number(window.innerHeight)) {
      document.querySelector('.project-area').style.height = (window.innerHeight) + 'px'
    }
    // var images = document.querySelectorAll('.images')
    // console.log(images[0].offsetWidth)
    // if (images[0].attributes[1].isConnected === true) {
    //   document.querySelector('.loader-scene').style.display = 'none'
    // }
    // document.querySelector('.exit').addEventListener('click', this.goToHome())
    // console.log(document.querySelector('img.images').style.innerHeight)
  }
  // updated () {
  // }
}
</script>
