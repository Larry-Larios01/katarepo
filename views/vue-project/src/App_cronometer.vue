<script lang="ts">
import { defineComponent } from 'vue';
import cronometer from './components/cronometer.vue';


export default defineComponent({
  name: 'MainCronometer',
  components: {
    cronometer
  },
});
</script>

<template>

<cronometer laps="5">  </cronometer>

<cronometer>  </cronometer>

</template>