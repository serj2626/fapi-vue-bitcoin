<script setup>
import axios from 'axios';
import { ref, onMounted, watchEffect } from 'vue';

let props = defineProps({
    id: Number
})

const currency = ref({})

const getCurrency = async () => {
    try {
        const res = await axios.get(`http://127.0.0.1:8000/currencies/${props.id}/`)
        currency.value = res.data
        console.log(currency.value);
    } catch (err) {
        console.log(err);
    }
}

onMounted(getCurrency())


</script>


<template>
    <div class="card shadow-lg mb-3" style="max-width: 540px">
        <div class="row g-0">
            <div class="col-md-4">
                <img src="..." class="img-fluid rounded-start" alt="..." />
            </div>
            <div class="col-md-8">
                <div class="card-body">
                    <h5 class="card-title">Card title</h5>
                    <p class="card-text">
                        This is a wider card with supporting text below as a natural
                        lead-in to additional content. This content is a little bit
                        longer.
                    </p>
                    <p class="card-text">
                        <small class="text-muted">Last updated 3 mins ago</small>
                    </p>
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
}
</style>