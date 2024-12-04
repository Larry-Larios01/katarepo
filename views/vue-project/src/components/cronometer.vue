<script>
import { ref } from 'vue'

export default {
  setup() {
    
    const count = ref(0)
    let cronometer = null
    function start() {
    cronometer = setInterval(() => {
    count.value++;
        }, 1000)
    }

    function stop() {
    clearInterval(cronometer)
    }

    // don't forget to expose the function as well.
    return {
      start,
      count,
      cronometer,
      stop
    }
  }
}




</script>

<template>
    <button @click="start"> start </button>
    <button @click="stop">stop</button>
    <p>{{ count }}</p>
</template>