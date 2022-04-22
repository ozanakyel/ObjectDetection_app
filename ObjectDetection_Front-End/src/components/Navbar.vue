<template>
  <div class="navbar">
    <div class="logo">
      <router-link to="/"><img src="@/assets/favicon.png" width="165" height="64" style="float: left;margin-left: 15px"></router-link>
    </div>
    <div class="add-project">
      <div class="change">
        <router-link to="/"><p class="change-text">RUN</p></router-link>
      </div>
    </div>
    <!-- <div class="menu">
      <a href="#">Ana Sayfa</a>
      <a href="#">Randevu al</a>
    </div> -->
  </div>
</template>

<script>
export default {
  name: 'NavbarTemplate',
  props: {
    msg: String
  }
}
</script>
