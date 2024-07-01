<script setup>
import axios from 'axios';
import { ref, onMounted, defineEmits } from 'vue';
const currencies = ref([])

const emit = defineEmits(['getCurrency'])

const getCurrency = async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/currencies/')
    currencies.value = res.data
    console.log(currencies.value);
  } catch (err) {
    console.log(err);
  }
}
onMounted(getCurrency)


</script>

<template>
    <div class="logo">
        <img src="/logo.png" alt="">
        <p class="text">Криптовалюты</p>
    </div>

    <div class="list-group nav" v-for="currency in currencies" :key="currency.id">
        <a 
        @click="emit('getCurrency', currency.id)"
        class="list-group-item list-group-item-action">{{currency.name }}</a>
    </div>
</template>

<style scoped>
.logo {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    & .text {
        font-size: 26px;
        font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    }
}

.nav {
    text-align: center;
    margin-top: 1px;
}
</style>