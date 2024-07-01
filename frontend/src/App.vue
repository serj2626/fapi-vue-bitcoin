<script setup>
import CurrencyList from "./components/CurrencyList.vue";
import Footer from "./components/Footer.vue";
import CurrencyDetail from "./components/CurrencyDetail.vue";
import axios from 'axios';
import { ref, onMounted } from 'vue';
import Spinner from "./components/Spinner.vue";


const idCurrency = ref(null)


const updateIDCurrency = (value) => {
  idCurrency.value = value
}

</script>

<template>
  <div class="left">
    <KeepAlive include="CurrencyList">
      <CurrencyList @getCurrency="updateIDCurrency($event)" />
    </KeepAlive>

  </div>
  <div class="right">
    <div class="container">
      <div class="row">
        <div v-if="idCurrency">
          <CurrencyDetail :id="idCurrency" />
        </div>
        <div v-else>
          <Spinner />
        </div>
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
  background-color: #baa5a586;
}
</style>
