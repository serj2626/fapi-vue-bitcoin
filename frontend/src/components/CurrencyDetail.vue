<script setup>
import axios from 'axios';
import { ref, watchEffect, onMounted } from 'vue';

let props = defineProps({
    id: Number
})

const currency = ref({})
const price = ref(0)
const getCurrency = async () => {
    try {
        const res = await axios.get(`http://127.0.0.1:8000/currencies/${props.id}/`)
        console.log('detail', res.data);
        price.value = res.data.quote['USD'].price
        currency.value = res.data
    } catch (err) {
        console.log(err);
    }
}

watchEffect(getCurrency)


</script>


<template>
    <div class="w-75 mx-auto">
        <div class="card shadow-lg mb-3" >
            <div class="row g-0">
                <div class="col-md-4">
                    <img class="img-fluid rounded-start" alt="..." />
                </div>
                <div class="">
                    <div class="card-body">
                        <h5 class="card-title">{{ currency.name }}</h5>
                        <p class="card-text">
                            {{ Math.round(price, 3) }} $
                        </p>
                        <p class="card-text">
                            <small class="text-muted">{{ currency.date_added }}</small>
                        </p>
                        <p class="card-text">
                            <small class="text-muted">{{ currency.last_updated }}</small>
                        </p>
                    </div>
                </div>
            </div>
        </div>

    </div>

</template>

<style scoped>
.card {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: linear-gradient(to right, #f5f7fa, #c3cfe2);
}
</style>