<script lang="ts">
import { ref } from 'vue'

export default {
  setup() {
    
    const count = ref(0)
    let cronometer : number;
    const numbers = ref<number[]>([]);
    function start() {
    cronometer = setInterval(() => {
    count.value++;
        }, 1000)
    }

    function pause() {
    clearInterval(cronometer)
    }

    function stop() {
    count.value = 0
    clearInterval(cronometer)
    numbers.value = []
    }

    function lap() {
        numbers.value.push(count.value)
    
    }

    // don't forget to expose the function as well.
    return {
      start,
      count,
      stop,
      pause, 
      lap,
      numbers
    }
  }
}




</script>

<template>
    <button @click="start"> start </button>
    <button @click="pause">pause</button>
    <button @click="stop"> stop </button>
    <button @click="lap">lap</button>
    <p>{{ count }}</p>

    <li v-for="lap in numbers">
        {{ lap }}
    </li>   

</template>