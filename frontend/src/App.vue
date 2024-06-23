<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
const currencies = ref([])



onMounted(async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/currencies/')
    console.log(res.data);
  } catch (err) {
    console.log(err);
  }
})
</script>

<template>
  <div class="left">
    <Header />
  </div>
  <div class="right">
    <div class="container">
      <div class="row">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Saepe, culpa harum! Ullam quod ducimus maxime, debitis
        unde, a sit quo, illo deleniti ratione provident incidunt esse optio autem magnam beatae excepturi reiciendis
        nihil error voluptatem quae! Dignissimos quae voluptatem ad ipsam eveniet ipsum eos quam alias porro sit nisi,
        fugit reprehenderit aspernatur ab ducimus voluptate suscipit perferendis dolorum, modi animi sunt numquam a?
        Deserunt, dolor officia. At, minima iusto reprehenderit totam nesciunt perspiciatis, ex consequatur id quam
        deleniti rem debitis fugit error dolores ut labore. Nam, unde quibusdam! Incidunt inventore optio corrupti alias
        dolores repellat cupiditate illum laboriosam soluta magni?
      </div>
    </div>
  <Footer />
  </div>

</template>

<style scoped>
.left {
  padding-block: 40px;
  height: 100vh;
  position: fixed;
  width: 20%;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f0f0f0;
}

.right {
  position: relative;
  margin-left: 20%;
  padding: 40px;
  min-height: 100vh;

}
</style>
