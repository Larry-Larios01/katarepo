<script>
import { ref } from 'vue'

export default {
  setup() {
    
    const count = ref(0)
    const interval = ref(0)

    function start() {
        count.value = count++
        interval.value = setInterval(count,1000)
    }

    // don't forget to expose the function as well.
    return {
      start,
      count,
      interval 
    }
  }
}




</script>

<template>
    <button @click="start">
    {{ interval }}
  </button>
</template>