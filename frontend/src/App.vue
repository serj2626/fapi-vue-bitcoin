<script setup>
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
import Card from "./components/Card.vue";
</script>

<template>
  <div class="left">
    <Header />
  </div>
  <div class="right">
    <div class="container">
      <div class="row">
       <Card />
      </div>
    </div>
    <Footer />
  </div>
</template>

<style scoped>
.left {
  padding-block: 40px;
  position: fixed;
  top: 0;
  bottom: 0;
  min-height: 100vh;
  overflow-y: scroll;
  width: 20%;
}

.right {
  position: relative;
  margin-left: 20%;
  padding: 40px;
  min-height: 100vh;
}
</style>
