<script setup>
import CurrencyList from "./components/CurrencyList.vue";
import Footer from "./components/Footer.vue";
import CurrencyDetail from "./components/CurrencyDetail.vue";
import axios from 'axios';
import { ref, onMounted } from 'vue';

const currencies = ref([])
const getCurrency = async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/currencies/')
    currencies.value = res.data
    console.log(currencies.value);
  } catch (err) {
    console.log(err);
  }
}
onMounted(getCurrency())

</script>

<template>
  <div class="left">

  </div>
  <div class="right">
    <div class="container">
      <div class="row">
        <CurrencyDetail />
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
  background-color: #e6e1e1;
}
</style>
