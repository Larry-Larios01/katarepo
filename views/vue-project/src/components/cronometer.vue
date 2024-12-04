<script>
import { ref } from 'vue'

export default {
  setup() {
    const interval = ref(setInterval(start,1000))

    function start() {
      
    }

    // don't forget to expose the function as well.
    return {
      interval
    }
  }
}




</script>

<template>
    <p>{{ interval }}</p>
</template>