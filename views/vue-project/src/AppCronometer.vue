<script lang="ts">
import { defineComponent } from 'vue';
import Competition from './components/Competition.vue';


export default defineComponent({
  name: 'MainCronometer',
  components: {
    Competition
  },
});
</script>

<template>

<Competition players="6"></Competition>

</template>