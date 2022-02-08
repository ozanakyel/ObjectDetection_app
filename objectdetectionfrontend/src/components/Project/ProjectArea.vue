<template>
  <div class="project-area">
    <div class="project-view">
      <div class="top">
        <div class="shower">
          MIFI - Object Detection / SafetyZone
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
        <div><img src="@/assets/favicon.png" width="100%"></div>
        <div><img src="@/assets/favicon.png" width="100%"></div>
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
        asd
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProjectArea',
  props: {
    msg: String
  },
  methods: {
    settings () {
      document.querySelector('.settings-show').style.display = 'block'
    },
    hideSettings (event) {
      if (event.target.className === 'settings-show') {
        document.querySelector('.settings-show').style.display = 'none'
      }
    }
  }
}
</script>
